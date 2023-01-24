import logging

from random import randint, choice
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator
from aiogram.dispatcher.filters import Text
from database import Database
from buttons import languages, lan_buttons
from config import API_TOKEN, admin # API_Token va Adminlar idlari

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
translator = Translator()
db = Database()

#---------------------------------------------------------------------------------

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    data = db.select_users(message.from_user.id)
    if data:	
    	await message.answer(f"🇺🇿 Assalomu alaykum <b>{message.chat.first_name}</b>\n      Tarjima qilish uchun so'zni kiriting:\n🇷🇺 Здравствуйте <b>{message.chat.first_name}</b>\n      Введите слово для перевода:\n🏴󠁧󠁢󠁥󠁮󠁧󠁿 Hello <b>{message.chat.first_name}</b>\n      Enter the word to translate:", parse_mode="HTML")
    else:
    	tel_id = message.from_user.id
    	name = message.from_user.first_name
    	db.insert_users(tel_id, name)

@dp.message_handler(commands=['users'], user_id=admin)
async def count(message: types.Message):
	data = db.count_users()
	await message.answer(f"Foydalanuvchilar soni: {data[0]} ta")

#---------------------------------------------------------------------------------

@dp.message_handler()
async def echo(message: types.Message):
	global user_message
	user_message = message.text
	btn = await lan_buttons()
	await message.answer("🇺🇿 Tilni tanlang/🇷🇺 Выберите язык/🏴󠁧󠁢󠁥󠁮󠁧󠁿 Select a language: ", reply_markup=btn)

#---------------------------------------------------------------------------------

@dp.callback_query_handler(Text(startswith="key_"))
async def translate(call: types.CallbackQuery):
	index = call.data.index("_")
	til = call.data[index+1:]
	for key, value in languages.items():
		if til == key:
			tarjima = translator.translate(user_message, dest = til)
			await call.message.answer(f"<b>{tarjima.text}</b>", parse_mode="HTML")

#---------------------------------------------------------------------------------

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

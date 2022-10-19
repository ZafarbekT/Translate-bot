import logging
from random import randint, choice
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator

API_TOKEN = '5779013887:AAGOiAYLE_6SxDV6y2YQPSVtJOP6LumMQZE'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
translator = Translator()

#---------------------------------------------------------------------------------

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer(f"🇺🇿 Assalomu alaykum <b>{message.chat.first_name}</b>\n      Tarjima qilish uchun so'zni kiriting:\n🇷🇺 Здравствуйте <b>{message.chat.first_name}</b>\n      Введите слово для перевода:\n🏴󠁧󠁢󠁥󠁮󠁧󠁿 Hello <b>{message.chat.first_name}</b>\n      Enter the word to translate:", parse_mode="HTML")

#---------------------------------------------------------------------------------

@dp.message_handler()
async def echo(message: types.Message):
	global user_message
	user_message = message.text


	# markup = types.InlineKeyboardMarkup(row_width=3)
	# button_uz = types.InlineKeyboardMarkup(text="🇺🇿 O'zbekcha", callback_data='uz')
	# button_ru = types.InlineKeyboardMarkup(text="🇷🇺 Руский", callback_data='ru')
	# button_en = types.InlineKeyboardMarkup(text="🏴󠁧󠁢󠁥󠁮󠁧󠁿English", callback_data='en')
	# markup.add(button_uz, button_ru, button_en)


	markup = types.InlineKeyboardMarkup(
		inline_keyboard=[
			[
				types.InlineKeyboardMarkup(text="🇺🇿 O'zbekcha", callback_data='uz'),
				types.InlineKeyboardMarkup(text="🇷🇺 Руский", callback_data='ru'),
				types.InlineKeyboardMarkup(text="🏴󠁧󠁢󠁥󠁮󠁧󠁿 English", callback_data='en')
			],
			[
				types.InlineKeyboardMarkup(text="🇩🇪 Deutsch", callback_data='de'),
				types.InlineKeyboardMarkup(text="🇸🇦 عربي", callback_data='ar'),
				types.InlineKeyboardMarkup(text="🇺🇦 Українська", callback_data='uk')
			],
			[
				types.InlineKeyboardMarkup(text="🇮🇹 Italiano", callback_data='it'),
				types.InlineKeyboardMarkup(text="🇯🇵 日本語", callback_data='ja'),
				types.InlineKeyboardMarkup(text="🇨🇳 中文简体", callback_data='zh-CN')
			],
			[
				types.InlineKeyboardMarkup(text="🇰🇷 한국어", callback_data='ko'),
				types.InlineKeyboardMarkup(text="🇮🇳 हिन्दी", callback_data='hi'),
				types.InlineKeyboardMarkup(text="🇫🇷 Français", callback_data='fr')
			],
			[
				types.InlineKeyboardMarkup(text="🇹🇷 Türkçe", callback_data='tr'),
				types.InlineKeyboardMarkup(text="🇦🇱 Shqip", callback_data='sq'),
				types.InlineKeyboardMarkup(text="🇦🇲 Հայերէն", callback_data='hy')
			],
			[
				types.InlineKeyboardMarkup(text="🇦🇿 آذربایجان دیلی", callback_data='az'),
				types.InlineKeyboardMarkup(text="🇧🇾 Беларуская", callback_data='be'),
				types.InlineKeyboardMarkup(text="🇧🇬 Български", callback_data='bg')
			],
			[
				types.InlineKeyboardMarkup(text="🇪🇸 Español", callback_data='es'),
				types.InlineKeyboardMarkup(text="🇸🇮 Slovensko", callback_data='sl'),
				types.InlineKeyboardMarkup(text="🇸🇪 Svenska", callback_data='sv')
			],
			[
				types.InlineKeyboardMarkup(text="🇨🇿 Čeština", callback_data='cs'),
				types.InlineKeyboardMarkup(text="🇩🇰 Dansk", callback_data='da'),
				types.InlineKeyboardMarkup(text="🇳🇱 Nederlands", callback_data='nl')
			],
			[
				types.InlineKeyboardMarkup(text="🇪🇪 Eesti keel", callback_data='et'),
				types.InlineKeyboardMarkup(text="🇵🇭 Filipino", callback_data='tl'),
				types.InlineKeyboardMarkup(text="🇫🇮 	Suomi", callback_data='fi')
			],
			[
				types.InlineKeyboardMarkup(text="🇬🇪 	ქართული", callback_data='ka'),
				types.InlineKeyboardMarkup(text="🇬🇷 Ελληνικά", callback_data='el'),
				types.InlineKeyboardMarkup(text="🇭🇹 Kreyòl ayisyen", callback_data='ht')
			]
		]
	)

	await message.answer("🇺🇿 Tilni tanlang/🇷🇺 Выберите язык/🏴󠁧󠁢󠁥󠁮󠁧󠁿 Select a language: ", reply_markup=markup)

#---------------------------------------------------------------------------------

@dp.callback_query_handler(text="uz")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="ru")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="en")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="de")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="ar")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="uk")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="it")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="ja")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="zh-CN")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="ko")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="hi")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="fr")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="tr")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="sq")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="hy")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="az")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="be")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="bg")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="es")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="sl")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="sv")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="cs")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="da")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="nl")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="et")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="tl")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="fi")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="ka")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="el")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="ht")
async def translate(call: types.CallbackQuery):
	tarjima = translator.translate(user_message, dest = call.data)
	await call.message.answer(tarjima.text)

#---------------------------------------------------------------------------------

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

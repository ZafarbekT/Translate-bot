from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

languages = {
	'uz': "🇺🇿 O'zbekcha",
	'ru': "🇷🇺 Руский",
	'en': "🏴󠁧󠁢󠁥󠁮󠁧󠁿 English",
	'de': "🇩🇪 Deutsch",
	'ar': "🇸🇦 عربي",
	'uk': "🇺🇦 Українська",
	'it': "🇮🇹 Italiano",
	'ja': "🇯🇵 日本語",
	'zh-CN': "🇨🇳 中文简体",
	'ko': "🇰🇷 한국어",
	'hi': "🇮🇳 हिन्दी",
	'fr': "🇫🇷 Français",
	'tr': "🇹🇷 Türkçe",
	'sq': "🇦🇱 Shqip",
	'hy': "🇦🇲 Հայերէն",
	'az': "🇦🇿 آذربایجان دیلی",
	'be': "🇧🇾 Беларуская",
	'bg': "🇧🇬 Български",
	'es': "🇪🇸 Español",
	'sl': "🇸🇮 Slovensko",
	'sv': "🇸🇪 Svenska",
	'cs': "🇨🇿 Čeština",
	'da': "🇩🇰 Dansk",
	'nl': "🇳🇱 Nederlands",
	'et': "🇪🇪 Eesti keel",
	'tl': "🇵🇭 Filipino",
	'fi': "🇫🇮 	Suomi",
	'ka': "🇬🇪 	ქართული",
	'el': "🇬🇷 Ελληνικά",
	'ht': "🇭🇹 Kreyòl ayisyen"
}

async def lan_buttons():
	markup = InlineKeyboardMarkup(row_width=3)
	for key, value in languages.items():
		markup.insert(InlineKeyboardButton(text=value,callback_data=f"key_{key}"))
	return markup
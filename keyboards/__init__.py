from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from keyboards.reply import menu_keyboard, profile_keyboard
from keyboards.inline import currencies_keyboard, categories_keyboard, last_operations_keyboard


menu_kb: ReplyKeyboardMarkup = menu_keyboard.create_menu_keyboard()
profile_kb: ReplyKeyboardMarkup = profile_keyboard.create_profile_keyboard()

currencies_kb: InlineKeyboardMarkup = currencies_keyboard.create_currencies_keyboard()
last_operations_kb: InlineKeyboardMarkup = last_operations_keyboard.create_last_operations_keyboard()
# income_categories_kb: Dynamic keyboard.
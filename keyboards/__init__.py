from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from keyboards.reply import menu
from keyboards.inline import currencies_keyboard, categories_keyboard


menu_kb: ReplyKeyboardMarkup = menu.create_menu_keyboard()

currencies_kb: InlineKeyboardMarkup = currencies_keyboard.create_currencies_keyboard()
# income_categories_kb: Dynamic keyboard.
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.types import Message, ReplyKeyboardRemove

import config

from keyboards.inline import categories_keyboard, currencies_keyboard, last_operations_keyboard
from keyboards.reply import menu_keyboard, settings_keyboard


categories_kb: InlineKeyboardMarkup = categories_keyboard.create_categories_keyboard()
# currencies_kb: Dynamic keyboard.
last_operations_kb: InlineKeyboardMarkup = last_operations_keyboard.create_last_operations_keyboard()

menu_kb: ReplyKeyboardMarkup = menu_keyboard.create_menu_keyboard()
settings_kb: ReplyKeyboardMarkup = settings_keyboard.create_settings_keyboard()
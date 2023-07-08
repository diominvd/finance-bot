from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from keyboards.reply import menu_keyboard, profile_keyboard, settings_keyboard, categories_type_keyboard, edit_categories_mode_keyboard, add_categories_keyboard
from keyboards.inline import currencies_keyboard, categories_keyboard, last_operations_keyboard


MenuKeyboard: ReplyKeyboardMarkup = menu_keyboard.create_menu_keyboard()
ProfileKeyboard: ReplyKeyboardMarkup = profile_keyboard.create_profile_keyboard()
SettingsKeyboard: ReplyKeyboardMarkup = settings_keyboard.create_settings_keyboard()
CategoriesTypeKeyboard: ReplyKeyboardMarkup = categories_type_keyboard.create_categories_type_keyboard()
EditCategoriesModeKeyboard: ReplyKeyboardMarkup = edit_categories_mode_keyboard.create_edit_categories_mode_keyboard()
AddCategoriesKeyboard: ReplyKeyboardMarkup = add_categories_keyboard.create_add_categories_keyboard()

CurrenciesKeyboard: InlineKeyboardMarkup = currencies_keyboard.create_currencies_keyboard()
LastOperationsKeyboard: InlineKeyboardMarkup = last_operations_keyboard.create_last_operations_keyboard()
# CategoriesKeyboard: Dynamic keyboard.
# CategoriesForDeleteKeyboard: Dynamic keyboard.
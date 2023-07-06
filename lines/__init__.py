import config
import emoji

import database
import storage
from storage import bot_storage

keyboards_lines: dict = {
    'menu_keyboard': {
        'income': '📈 | Доход',
        'expense': '📉 | Расход',
        'profile': '👤 | Профиль',
        'settings': '⚙️ | Настройки'
    },
    'currencies_keyboard': {
        'RUB': {
            'name': 'RUB',
            'title': '🇷🇺 | RUB (₽)',
            'callback_data': 'currency_RUB',
            'text': '₽'
        },
        'BYN': {
            'name': 'BYN',
            'title': '🇧🇾 | BYN (Br)',
            'callback_data': 'currency_BYN',
            'text': 'Br'
        },
        'UAH': {
            'name': 'UAH',
            'title': '🇺🇦 | UAH (₴)',
            'callback_data': 'currency_UAH',
            'text': '₴'
        },
        'KZT': {
            'name': 'KZT',
            'title': '🇰🇿 | KZT (₸)',
            'callback_data': 'currency_KZT',
            'text': '₸'
        },
        'USD': {
            'name': 'USD',
            'title': '🇺🇸 | USD ($)',
            'callback_data': 'currency_USD',
            'text': '$'
        },
        'EUR': {
            'name': 'EUR',
            'title': '🇪🇺 | EUR (€)',
            'callback_data': 'currency_EUR',
            'text': '€'
        }
    },
    'profile_keyboard': {
        'last_operations': '🕐 | Последние операции',
        'statistic': '📊 | Статистика',
        'main_menu': '🏠 | Главное меню'
    },
    'last_operations_keyboard': {
        'delete_last': {
            'title': 'Удалить последнюю операцию',
            'callback_data': 'delete_last'
        },
        'cancel': {
            'title': 'Отмена',
            'callback_data': 'cancel'
        }
    }
}

commands_lines: dict = {
    'command_text_help': 'Список основных функций бота:\n\n'
                         '1. <b>Добавить операцию</b> - Позволяет добавить операцию с последующим выбором категории и суммы. '
                         'Операция сохраняется в базу данных.\n\n'
                         '2. <b>Последние операции</b> - Отображает последние 5 операций с возможностью '
                         'удалить последнюю добавленную операцию.\n\n'
                         '3. <b>Профиль</b> - Отображает вашу статистику по всем категориям за отчётный период.\n\n'
                         '4. <b>Настройки</b> - Дополнительные функции.\n'
                         '4.1 <b>Очистить историю операций</b> - Удаляет всю историю операций. При этом сбрасывается отчётный период. '
                         'Чтобы начать новый период добавьте новую операцию.',
    'command_text_info': f'<b>Finance Bot v{config.version}</b>.\n'
                         f'Исходный код проекта на Git Hub: clck.ru/34qJYm\n'
                         f'Официальная группа: @diominvdev\n'
                         f'Developer: @diominvd',
    'command_text_start': 'Добро пожаловать в Finance Bot 💲\n\n'
                          'Этот бот поможет вести учёт расходов. '
                          'Вы можете классифицировать все операции по категориям, '
                          'просматривать последние операции и формировать отчёт за определённый период.\n\n'
                          'Для получения дополнительной информации напишите команду "/help."',
}


first_start_lines: dict = {
    'error_text_incorrect_categories': 'Некорректный ввод. Повторите попытку.',
    'error_text_wrong_balance': 'Некорректное значение. Повторите попытку',

    'text_set_currency': 'Перед использованием настроим бота. Выберите валюту, которая будет использована в дальнейших операциях.',
    'text_set_balance': 'Отлично. Теперь укажите текущий баланс.',
    'text_set_income_categories': 'Теперь создадим категории для доходов. Отправьте список категорий в формате:\n\n'
                                  'Название категории emoji\n'
                                  'Название категории emoji\n\n'
                                  'Между названием категории и emoji должен быть пробел.',
    'text_set_expense_categories': 'Теперь отправьте категории расходов в таком же формате, как и категории доходов.',
    'text_first_start_complete': 'Отлично. Первичная настройка завершена.'
}


def category_set(user_id: int) -> str:
    return f'Выбрана категория: {bot_storage[user_id]["category"]} {bot_storage[user_id]["emoji"]}.'


def value_set(user_id: int) -> str:
    return f'Сумма операции: {bot_storage[user_id]["value"]} {bot_storage[user_id]["currency"]}'


def operation_complete(user_id: int) -> str:
    return f'Операция успешно сохранена 📌\n' \
           f'Тип операции: {operations_types[bot_storage[user_id]["operation_type"]]}\n' \
           f'Категория: {bot_storage[user_id]["category"]} {bot_storage[user_id]["emoji"]}\n' \
           f'Сумма операции: {bot_storage[user_id]["value"]} {bot_storage[user_id]["currency"]}'


operations_types: dict = {
    'income': 'Доход',
    'expense': 'Расход'
}


new_operation_lines: dict = {
    'def_text_category_set': category_set,
    'def_text_value_set': value_set,
    'def_text_operation_complete': operation_complete,

    'error_text_incorrect_value': 'Ошибка ввода. Неверное значение. Повторите попытку.',

    'text_choose_income_category': 'Выберите категорию для операции.',
    'text_choose_operation_value': 'Теперь укажите сумму операции.'
}


def load_profile(data: tuple) -> str:
    return f'Пользователь: @{data[0]}\n' \
           f'Баланс: {data[2]} {data[1]}'


profile_lines: dict = {
    'profile_info': load_profile,
}


def last_operations(user_id: int, operations_list: list) -> str:

    message_text: str = ''

    for operation in operations_list:
        if operation[0] == 'income':
            sign: str = '+'
            categories: dict = database.load_categories(user_id, operation_type='income')
        elif operation[0] == 'expense':
            sign: str = '-'
            categories: dict = database.load_categories(user_id, operation_type='expense')

        message_text += f'{sign}{operation[3]} {operation[1]} | {categories[operation[2]]["title"]} {emoji.emojize(categories[operation[2]]["emoji"])} | {operation[4]}\n'

    return message_text


last_operations_lines: dict = {
    'def_text_last_operations': last_operations,

    'error_text_last_operations_empty': 'Список последних операций пуст.'
}

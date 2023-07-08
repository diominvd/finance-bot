import datetime
import emoji

import config
import database.load
import storage
from storage import bot_storage


keyboards_lines: dict = {
    'menu-keyboard': {
        'income': '📈 | Доход',
        'expense': '📉 | Расход',
        'profile': '👤 | Профиль',
        'settings': '⚙️ | Настройки'
    },
    'currencies-keyboard': {
        'RUB': {
            'title': '🇷🇺 | RUB (₽)',
            'callback_data': 'currency_RUB',
        },
        'BYN': {
            'title': '🇧🇾 | BYN (Br)',
            'callback_data': 'currency_BYN',
        },
        'UAH': {
            'title': '🇺🇦 | UAH (₴)',
            'callback_data': 'currency_UAH',
        },
        'KZT': {
            'title': '🇰🇿 | KZT (₸)',
            'callback_data': 'currency_KZT',
        },
        'USD': {
            'title': '🇺🇸 | USD ($)',
            'callback_data': 'currency_USD',
        },
        'EUR': {
            'title': '🇪🇺 | EUR (€)',
            'callback_data': 'currency_EUR',
        }
    },
    'profile-keyboard': {
        'last_operations': '🕐 | Последние операции',
        'statistic': '📊 | Статистика',
        'main_menu': '🏠 | Главное меню'
    },
    'last-operations-keyboard': {
        'delete_last': {
            'title': 'Отменить последнюю операцию',
            'callback_data': 'delete_last'
        },
        'cancel': {
            'title': '« Назад в профиль',
            'callback_data': 'cancel'
        }
    },
    'settings-keyboard': {
        'edit-categories': '✏️ | Редактировать категории',
        'main-menu': '🏠 | Главное меню'
    },
    'categories-type-keyboard': {
        'income': '📈 | Категории доходов',
        'expense': '📉 | Категории расходов',
        'cancel': 'Назад в настройки'
    },
    'edit-categories-mode-keyboard': {
        'add': '➕ | Добавить категории',
        'delete': '➖ | Удалить категории',
        'cancel': 'Назад в настройки'
    },
    'add-categories-keyboard': {
        'cancel': 'Назад в настройки'
    }
}

currencies: dict = {
    'RUB': {
        'name': 'RUB',
        'symbol': '₽',
    },
    'BYN': {
        'name': 'BYN',
        'symbol': 'Br',
    },
    'UAH': {
        'name': 'UAH',
        'symbol': '₴',
    },
    'KZT': {
        'name': 'KZT',
        'symbol': '₸',
    },
    'USD': {
        'name': 'USD',
        'symbol': '$',
    },
    'EUR': {
        'name': 'EUR',
        'symbol': '€',
    }
}
operations_types: dict = {
    'income': 'Доход 📈',
    'expense': 'Расход 📉'
}

"""
c = command; t = text; d = def.
"""
commands_lines: dict = {
    'c-t-help': 'Список основных функций бота:\n\n'
                '1. <b>Доход</b>, <b>Расход</b> - Позволяет добавить операцию с последующим выбором категории и суммы. '
                'Операция сохраняется в базу данных.\n\n'
                '2. <b>Профиль</b> - Отображает текущий баланс.\n'
                '2.1. <b>Последние операции</b> - Отображает последние 10 операций и позволяет отменить последнюю операцию.\n'
                '2.1.1. <b>Отменить последнюю операцию</b> - Удаляет последнюю операцию из базы данных с соответствующим изменением баланса.\n'
                '2.2. <b>Статистика</b> - Отображает статистику по всем операциям.\n'
                'При отсутствии операций период не будет определён.\n\n'
                '3. <b>Настройки</b> - Дополнительные функции.\n'
                '3.1 <b>Редактировать категории</b> - Позволяет создавать свои категории и удалять существующие.\n'
                'При удалении категории она исчезает из "Статистики", но отображается в списке последних операций с соответствующим '
                'emoji 🚫. Вы можете удалить ее из списка последних операций.',
    'c-t-info': f'<b>Finance Bot v{config.version}</b>.\n'
                f'Исходный код проекта на Git Hub: clck.ru/34qJYm\n'
                f'Официальная группа: @diominvdev\n'
                f'Developer: @diominvd',
    'c-t-start': 'Добро пожаловать в Finance Bot 💲\n\n'
                 'Этот бот поможет вести учёт ваших финансов. '
                 'Вы можете классифицировать все операции по категориям, '
                 'просматривать последние операции и формировать отчёт за определённый период.\n\n'
                 'Для получения дополнительной информации напишите команду "/help."',
}

"""
e = error; t = text; d = def.
"""
first_start_lines: dict = {
    'e-t-incorrect-categories': 'Невозможно обработать категории. Повторите попытку.',
    'e-t-wrong-balance': 'Некорректное значение. Повторите попытку',

    't-choose-currency': 'Перед использованием настроим бота. Выберите валюту, которая будет использована в дальнейших операциях.',
    't-currency-set': 'Выбрана валюта: ',
    't-choose-balance': 'Отлично. Теперь укажите текущий баланс.',
    't-balance-set': 'Установлен баланс: ',
    't-set-income-categories': 'Теперь создадим категории для доходов. Отправьте список категорий в формате:\n\n'
                               'Название категории emoji\n'
                               'Название категории emoji\n\n'
                               'Между названием категории и emoji должен быть пробел. Например:\n\n'
                               'Работа 💰\n'
                               'Вторая работа 🛠',
    't-set-expense-categories': 'Теперь отправьте категории расходов в таком же формате, как и категории доходов.',
    't-initial-setup-complete': 'Отлично. Первичная настройка завершена.'
}


def category_set(category: str, emoji: str) -> str:
    return f'Выбрана категория: {category} {emoji}.'


def value_set(value: float, currency: str) -> str:
    return f'Сумма операции: {value} {currency}'


def operation_complete(user_id: int) -> str:
    # Load operation data from bot storage.
    operation_type: str = operations_types[bot_storage[user_id]["operation_type"]]
    operation_category: str = bot_storage[user_id]["category"]
    operation_category_emoji: str = bot_storage[user_id]["emoji"]
    operation_value: float = bot_storage[user_id]["value"]
    operation_currency: str = bot_storage[user_id]["currency"]

    return f'📌 Операция успешно сохранена.\n' \
           f'Тип операции: {operation_type}\n' \
           f'Категория: {operation_category} {operation_category_emoji}\n' \
           f'Сумма операции: {operation_value} {operation_currency}'


"""
e = error; t = text; d = def.
"""
new_operation_lines: dict = {
    'd-t-category-set': category_set,
    'd-t-value-set': value_set,
    'd-t-operation-complete': operation_complete,

    'e-t-categories-empty': 'Невозможно добавить операцию. Список категорий пуст. Добавьте хотя бы одну категорию и повторите попытку.',
    'e-t-incorrect-value': 'Ошибка ввода. Неверное значение. Повторите попытку.',
    'e-r-operation-canceled': 'Операция отменена.',
    'e-t-not-enough-balance': 'Невозможно добавить операцию. Недостаточно средств.',

    't-choose-category': 'Выберите категорию для операции.',
    't-choose-value': 'Теперь укажите сумму операции.'
}


def load_profile(data: tuple) -> str:
    return f'Пользователь: @{data[0]}\n' \
           f'Баланс: {data[2]} {data[1]}'


def load_statistic(income: dict, expense: dict, currency: str, first_date: str) -> str:
    current_date: list = list(reversed(str(datetime.date.today()).split('-')))
    current_date: str = '.'.join(current_date)

    total_income: float = 0
    total_expense: float = 0

    message_text: str = f'Статистика доходов:\n'
    for key, value in income.items():
        message_text += f'∟ {value["title"]} {emoji.emojize(value["emoji"])}: {value["value"]} {currency}\n'
        total_income += value["value"]
    message_text += f'<b>Всего получено</b>: {total_income} {currency}\n'

    message_text += f'\nСтатистика расходов:\n'
    for key, value in expense.items():
        message_text += f'∟ {value["title"]} {emoji.emojize(value["emoji"])}: {value["value"]} {currency}\n'
        total_expense += value["value"]
    message_text += f'<b>Всего потрачено</b>: {total_expense} {currency}\n'

    if first_date == 'Период не определён':
        message_text += f'\nПериод: <b>{first_date}</b>\n' \
                        f'Так как отсутствуют операции.'
    else:
        message_text += f'\nПериод: <b>{first_date}</b> - <b>{current_date}</b>'

    return message_text


profile_lines: dict = {
    'd-t-load-statistic': load_statistic,
    'd-t-profile-info': load_profile,
}


def last_operations(user_id: int, operations_list: list) -> str:
    message_text: str = ''

    for operation in operations_list:
        if operation[0] == 'income':
            categories: dict = database.load.load_categories(user_id, 'income')
            sign: str = '+'

        elif operation[0] == 'expense':
            categories: dict = database.load.load_categories(user_id, 'expense')
            sign: str = '-'

        operation_value: float = operation[3]
        operation_currency: str = operation[1]

        # If category deleted emoji will be like 🚫.
        try:
            operation_category: str = categories[operation[2]]["title"]
            category_emoji: str = emoji.emojize(categories[operation[2]]["emoji"])
        except:
            operation_category: str = operation[2]
            category_emoji: str = '🚫'

        operation_date: str = operation[4]

        message_text += f'{sign}{operation_value} {operation_currency} | {operation_category} {category_emoji} | {operation_date}\n'

    return message_text


last_operations_lines: dict = {
    'd-t-last-operations': last_operations,

    'e-t-last-operations-empty': 'Список последних операций пуст.'
}

def category_deleted(category_name: str, category_emoji: str) -> str:
    return f'Категория "{category_name} {emoji.emojize(category_emoji)}" успешно удалена.'


edit_categories_lines: dict = {
    'd-t-category-deleted': category_deleted,
    'e-t-categories-empty': 'Список категорий пуст.',
    'e-t-incorrect-category': 'Ошибка при создании категории. Неверный формат. Повторите попытку.',

    't-choose-categories-type': 'Выберите тип категорий для редактирования.',
    't-choose-edit-mode': 'Выберите соответсвующую функцию.',
    't-categories-for-add': 'Отправьте категорию / категории в формате:\n\n'
                            'Название категории emoji\n'
                            'Название категории emoji\n\n'
                            'Между названием категории и emoji должен быть пробел!',
    't-categories-for-delete': 'Нажмите на соответсвующую категорию для её удаления.',
    't-category-added': 'Список категорий успешно обновлён.',

}


other_lines: dict = {
    't-back-to-main-menu': 'Возвращаюсь в главное меню.',
    't-back-to-profile': 'Возвращаюсь в профиль.',
    't-open-settings': 'Открываю настройки.',
    't-back-to-settings': 'Возвращаюсь в настройки.',
}

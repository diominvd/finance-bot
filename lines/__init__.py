import pydantic.main
import datetime

import config
from config import bot_storage
from data import database

keyboards_lines: dict = {
    'categories_keyboard': {
        'products': {
            'title': 'Продукты',
            'callback_data': 'category_products'
        },
        'cafes': {
            'title': 'Кафе',
            'callback_data': 'category_cafe'
        },
        'auto': {
            'title': 'Автомобиль',
            'callback_data': 'category_auto'
        },
        'transport': {
            'title': 'Транспорт',
            'callback_data': 'category_transport'
        },
        'home': {
            'title': 'Дом',
            'callback_data': 'category_home'
        },
        'entertainment': {
            'title': 'Развлечения',
            'callback_data': 'category_entertainment'
        },
        'sport': {
            'title': 'Спорт',
            'callback_data': 'category_sport'
        },
        'health': {
            'title': 'Здоровье',
            'callback_data': 'category_health'
        },
        'education': {
            'title': 'Образование',
            'callback_data': 'category_education'
        },
        'gifts': {
            'title': 'Подарки',
            'callback_data': 'category_gifts'
        },
        'beauty': {
            'title': 'Красота',
            'callback_data': 'category_beauty'
        },
        'clothes': {
            'title': 'Одежда',
            'callback_data': 'category_clothes'
        },
        'technic': {
            'title': 'Техника',
            'callback_data': 'category_technic'
        },
        'subscriptions': {
            'title': 'Подписки',
            'callback_data': 'category_subscriptions'
        },
        'menu': {
            'title': 'Главное меню',
            'callback_data': 'menu'
        }
    },
    'last_operations_keyboard': {
        'delete_last_operation': {
            'title': 'Удалить последнюю операцию',
            'callback_data': 'delete_last'
        },
        'menu': {
            'title': 'Главное меню',
            'callback_data': 'menu'
        }
    },
    'menu_keyboard': {
        'add_operation': 'Добавить операцию',
        'last_operations': 'Последние операции',
        'profile': 'Профиль',
        'settings': 'Настройки'
    },
    'settings_keyboard': {
        'clear_all_operations': 'Очистить список операций',
        'menu': 'Главное меню'
    },
}

categories: dict = {
    'products': 'Продукты',
    'cafes': 'Кафе',
    'auto': 'Автомобиль',
    'transport': 'Транспорт',
    'home': 'Дом',
    'entertainment': 'Развлечения',
    'sport': 'Спорт',
    'health': 'Здоровье',
    'education': 'Образование',
    'gifts': 'Подарки',
    'beauty': 'Красота',
    'clothes': 'Одежда',
    'technic': 'Техника',
    'subscriptions': 'Подписки'
}

commands_lines: dict = {
    'text_help_command': 'Список основных функций бота:\n\n'
                         '1. <b>Добавить операцию</b> - Позволяет добавить операцию с последующим выбором категории и суммы. '
                         'Операция сохраняется в базу данных.\n\n'
                         '2. <b>Последние операции</b> - Отображает последние 5 операций с возможностью '
                         'удалить последнюю добавленную операцию.\n\n'
                         '3. <b>Профиль</b> - Отображает вашу статистику по всем категориям за отчётный период.\n\n'
                         '4. <b>Настройки</b> - Дополнительные функции.\n'
                         '4.1 <b>Очистить историю операций</b> - Удаляет всю историю операций. При этом сбрасывается отчётный период. '
                         'Чтобы начать новый период добавьте новую операцию.',
    'text_start_command': 'Добро пожаловать в Finance Bot 💲\n\n'
                          'Этот бот поможет вести учёт расходов. '
                          'Вы можете классифицировать все операции по категориям, '
                          'просматривать последние операции и формировать отчёт за определённый период.\n\n'
                          'Для получения дополнительной информации напишите команду "/help."',
    'text_info_command': f'<b>Finance Bot v{config.version}</b>.\n'
                         f'Исходный код проекта на Git Hub: clck.ru/34qJYm\n'
                         f'Официальная группа: @diominvdev\n'
                         f'Developer: @diominvd',
}


def last_operations(user_id: int) -> str:
    operations_list: list = database.select_operations_from_database_operations(user_id=user_id, limit=5)
    message_text: str = f'Последние операции:\n'

    for operation in operations_list:
        category: str = operation[0]
        value: float = operation[1]
        date: str = operation[2]
        message_text += f'{value} ₽ | {categories[category]} | {date}\n'

    return message_text


last_operations_lines: dict = {
    'def_text_last_operations': last_operations,

    'error_text_last_operations_empty': 'Список последних операций пуст.',
}


def category(category: str = None) -> str:
    return f'Выбрана категория: {categories[category]}'


def value(value: str = None) -> str:
    return f'Сумма операции: {float(value)} ₽'


def def_text_operation_complete(user_id: int) -> str:
    return f'📌 Операция успешно добавлена.\n' \
           f'Категория: {categories[bot_storage[user_id]["category"]]}\n' \
           f'Сумма: {bot_storage[user_id]["value"]} ₽\n' \
           f'Дата создания: {bot_storage[user_id]["date"]}\n\n'


new_operation_lines: dict = {
    'def_text_category_chosen': category,
    'def_text_operation_complete': def_text_operation_complete,
    'def_text_value_inputted': value,

    'error_text_incorrect_value': 'Неверное значение суммы операции. Повторите попытку.',

    'text_choose_category': 'Пожалуйста, укажите категорию для операции.',
    'text_input_value': 'Пожалуйста, укажите сумму операции.',
}


def current_date_formation() -> str:
    date: list = str(datetime.date.today()).split('-')
    date: str = f'{date[2]}.{date[1]}.{date[0]}'

    return date


def output_statistic(username: str, user_id: int) -> str:
    operations_list: list = database.select_operations_from_database_operations(user_id=user_id)
    current_date: str = current_date_formation()

    try:
        first_date: str = operations_list[0][2]
    except:
        reporting_period: str = 'Отсутствует.'
    else:
        reporting_period: str = f'{first_date} - {current_date}'
    finally:
        categories_values: dict = {
            'products': {
                'title': 'Продукты',
                'value': 0
            },
            'cafes': {
                'title': 'Кафе',
                'value': 0
            },
            'auto': {
                'title': 'Автомобиль',
                'value': 0
            },
            'transport': {
                'title': 'Транспорт',
                'value': 0
            },
            'home': {
                'title': 'Дом',
                'value': 0
            },
            'entertainment': {
                'title': 'Развлечения',
                'value': 0
            },
            'sport': {
                'title': 'Спорт',
                'value': 0
            },
            'health': {
                'title': 'Здоровье',
                'value': 0
            },
            'education': {
                'title': 'Образование',
                'value': 0
            },
            'gifts': {
                'title': 'Подарки',
                'value': 0
            },
            'beauty': {
                'title': 'Красота',
                'value': 0
            },
            'clothes': {
                'title': 'Одежда',
                'value': 0
            },
            'technic': {
                'title': 'Техника',
                'value': 0
            },
            'subscriptions': {
                'title': 'Подписки',
                'value': 0
            }
        }
        total_sum: float = 0

        # Summ all values in categories.
        for operation in operations_list:
            categories_values[operation[0]]['value'] += operation[1]
            total_sum += operation[1]

        message_text = f'Пользователь: @{username}\n' \
                       f'Ваши расходы по категориям.\n' \
                       f'📅 Период: {reporting_period}\n\n' \
                       f'{categories_values["products"]["title"]}: {categories_values["products"]["value"]} ₽\n' \
                       f'{categories_values["cafes"]["title"]}: {categories_values["cafes"]["value"]} ₽\n' \
                       f'{categories_values["auto"]["title"]}: {categories_values["auto"]["value"]} ₽\n' \
                       f'{categories_values["transport"]["title"]}: {categories_values["transport"]["value"]} ₽\n' \
                       f'{categories_values["home"]["title"]}: {categories_values["home"]["value"]} ₽\n' \
                       f'{categories_values["entertainment"]["title"]}: {categories_values["entertainment"]["value"]} ₽\n' \
                       f'{categories_values["sport"]["title"]}: {categories_values["sport"]["value"]} ₽\n' \
                       f'{categories_values["health"]["title"]}: {categories_values["health"]["value"]} ₽\n' \
                       f'{categories_values["education"]["title"]}: {categories_values["education"]["value"]} ₽\n' \
                       f'{categories_values["gifts"]["title"]}: {categories_values["gifts"]["value"]} ₽\n' \
                       f'{categories_values["beauty"]["title"]}: {categories_values["beauty"]["value"]} ₽\n' \
                       f'{categories_values["clothes"]["title"]}: {categories_values["clothes"]["value"]} ₽\n' \
                       f'{categories_values["technic"]["title"]}: {categories_values["technic"]["value"]} ₽\n' \
                       f'{categories_values["subscriptions"]["title"]}: {categories_values["subscriptions"]["value"]} ₽\n\n' \
                       f'Всего потрачено: {total_sum} ₽'

        return message_text


profile_lines: dict = {
    'def_text_statistic': output_statistic
}

settings_lines: dict = {
    'error_text_operations_list_empty': 'Очистка не требуется.\nСписок операций пуст.',
    'text_settings': 'Перехожу в настройки.',
    'text_all_operations_deleted': 'Список операций очищен.'
}

other_lines: dict = {
    'text_back_menu': 'Возвращаюсь в главное меню.'
}

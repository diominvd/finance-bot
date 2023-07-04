keyboards_lines: dict = {
    'currencies_keyboard': {
        'RUB': {
            'title': '🇷🇺 | RUB (₽)',
            'callback_data': 'currency_₽'
        },
        'BYN': {
            'title': '🇧🇾 | BYN (Br)',
            'callback_data': 'currency_Br'
        },
        'UAH': {
            'title': '🇺🇦 | UAH (₴)',
            'callback_data': 'currency_₴'
        },
        'KZT': {
            'title': '🇰🇿 | KZT (₸)',
            'callback_data': 'currency_₸'
        },
        'USD': {
            'title': '🇺🇸 | USD ($)',
            'callback_data': 'currency_$'
        },
        'EUR': {
            'title': '🇪🇺 | EUR (€)',
            'callback_data': 'currency_€'
        },
        'cancel': {
            'title': 'Отмена',
            'callback_data': 'cancel'
        }
    },
    'categories_keyboard': {
        'products': {
            'title': '🍞 | Продукты',
            'callback_data': 'category_products'
        },
        'cafes': {
            'title': '🍔 | Кафе',
            'callback_data': 'category_cafes'
        },
        'auto': {
            'title': '🚘 | Автомобиль',
            'callback_data': 'category_auto'
        },
        'transport': {
            'title': '🚃 | Транспорт',
            'callback_data': 'category_transport'
        },
        'home': {
            'title': '🏡 | Дом',
            'callback_data': 'category_home'
        },
        'entertainment': {
            'title': '🎡 | Развлечения',
            'callback_data': 'category_entertainment'
        },
        'sport': {
            'title': '🏓 | Спорт',
            'callback_data': 'category_sport'
        },
        'health': {
            'title': '💊 | Здоровье',
            'callback_data': 'category_health'
        },
        'education': {
            'title': '📚 | Образование',
            'callback_data': 'category_education'
        },
        'gifts': {
            'title': '🎁 | Подарки',
            'callback_data': 'category_gifts'
        },
        'beauty': {
            'title': '💄 | Красота',
            'callback_data': 'category_beauty'
        },
        'clothes': {
            'title': '👕 | Одежда',
            'callback_data': 'category_clothes'
        },
        'technic': {
            'title': '🖥 | Техника',
            'callback_data': 'category_technic'
        },
        'subscriptions': {
            'title': '📲 | Подписки',
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
        'add_operation': '➕ | Добавить операцию',
        'last_operations': '🕔 | Последние операции',
        'profile': '👤 | Профиль',
        'settings': '⚙️ | Настройки'
    },
    'settings_keyboard': {
        'clear_all_operations': '🗑 | Очистить список операций',
        'change_currency': '💱 | Изменить валюту',
        'menu': '🏠 | Главное меню'
    },
}

menu_keyboard: dict = {
    'income': '📈 | Доход',
    'expense': '📉 | Расход',
    'profile': '👤 | Профиль',
    'settings': '⚙️ | Настройки'
}
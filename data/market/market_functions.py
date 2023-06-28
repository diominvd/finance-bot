from bs4 import BeautifulSoup

import strings
from data import cursor, connection
import requests


def insert_new_user_into_database_market(user_id: int) -> None:
    try:
        cursor.execute('INSERT INTO market VALUES (?, ?)', (user_id, ''))
    except:
        print(f'> insert user {user_id} into database/market: error.')
    else:
        connection.commit()
        print(f'> insert user {user_id} into database/market: success.')


def check_new_ticker_existence(ticker_name: str) -> bool:
    response = requests.get(f'https://www.tinkoff.ru/invest/stocks/{ticker_name}/')
    soup = BeautifulSoup(response.content, 'html.parser')
    ticker_value = soup.find('span', class_='SecurityInvitingScreen__priceValue_c1Ah9')

    try:
        ticker_value = ticker_value.text.strip()
    except:
        return False
    else:
        return True


def check_new_ticker_in_database_market_user_tickers(ticker_name: str, user_id: int) -> bool:
    cursor.execute('SELECT tickers FROM market WHERE user_id = ?', (user_id,))
    user_tickers_from_db = cursor.fetchall()[0][0].split(',')

    if ticker_name in user_tickers_from_db:
        return True
    else:
        return False


def check_user_tickers_limit(tickers_list: list) -> bool:
    if len(tickers_list) == 10:
        return True
    else:
        return False


def add_new_ticker_for_user_in_database_market(user_id: int, new_ticker_name: str) -> str:
    if check_new_ticker_existence(ticker_name=new_ticker_name):
        if not check_new_ticker_in_database_market_user_tickers(ticker_name=new_ticker_name, user_id=user_id):
            user_tickers: list = select_all_user_tickers_from_database_market(user_id=user_id)

            # Formatting string with all tickers
            user_tickers_string: str = f''

            for ticker in user_tickers:
                user_tickers_string += f'{ticker},'

            # Add new ticker in user_tickers_string
            user_tickers_string += new_ticker_name

            # Update user tickers in database/market.
            try:
                cursor.execute('UPDATE market SET tickers = ? WHERE user_id = ?', (user_tickers_string, user_id))
            except:
                print(f'> add ticker {new_ticker_name} to user {user_id}: error.')
            else:
                connection.commit()
                print(f'> add ticker {new_ticker_name} to user {user_id}: success.')
                return strings.market['ticker_added'](ticker_name=new_ticker_name)
        else:
            return strings.market['ticker_exists']
    else:
        return strings.market['nonexistent_ticker_name']


def parse_ticker(ticker_name: str) -> str:
    response = requests.get(f'https://www.tinkoff.ru/invest/stocks/{ticker_name}/')

    # Check success of request.
    if response.status_code == 200:
        # Parse page.
        soup = BeautifulSoup(response.content, 'html.parser')
        ticker_value = soup.find('span', class_='SecurityInvitingScreen__priceValue_c1Ah9')
        ticker_value = ticker_value.text.strip()

        return ticker_value
    else:
        print(f'> parsing ticker value: error.', response.status_code)
        return 'Ошибка при получении значения.'


def select_all_user_tickers_from_database_market(user_id: int) -> list:
    cursor.execute(f'SELECT tickers FROM market WHERE user_id = ?', (user_id, ))
    user_tickers: list = cursor.fetchall()[0][0].split(',')

    if user_tickers[0] == '':
        user_tickers.pop(0)
    else:
        pass

    return user_tickers
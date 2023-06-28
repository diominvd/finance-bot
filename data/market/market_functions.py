from bs4 import BeautifulSoup
from data import cursor, connection
import requests


def insert_new_user_into_database_market(user_id: int) -> None:
    try:
        cursor.execute('INSERT INTO market (user_id) VALUES (?)', (user_id, ))
    except:
        print(f'> insert user {user_id} into database/market: error.')
    else:
        connection.commit()
        print(f'> insert user {user_id} into database/market: success.')


def add_new_ticker_for_user_in_database_market(user_id: int, new_ticker: str) -> bool:
    cursor.execute('SELECT tickers FROM market WHERE user_id = ?', (user_id, ))
    user_tickers_from_db = cursor.fetchall()[0][0]

    if user_tickers_from_db is None:
        user_tickers_from_db = f''
        updated_user_tickers: str = f'{user_tickers_from_db}{new_ticker}'
    else:
        # Check ticker in user_tickers_from_db
        if new_ticker in user_tickers_from_db:
            return False
        else:
            # Add ticker in user tickers from database.
            updated_user_tickers: str = f'{user_tickers_from_db},{new_ticker}'

    # Update user tickers in database/market.
    try:
        cursor.execute('UPDATE market SET tickers = ? WHERE user_id = ?', (updated_user_tickers, user_id))
    except:
        print(f'> add ticker {new_ticker} to user {user_id}: error.')

        return False
    else:
        connection.commit()
        print(f'> add ticker {new_ticker} to user {user_id}: success.')

        return True


def parse_ticker_value(ticker_name: str) -> str:
    url = f'https://www.tinkoff.ru/invest/stocks/{ticker_name}/'
    response = requests.get(url)

    # Check success of request.
    if response.status_code == 200:
        # Parse page.
        soup = BeautifulSoup(response.content, 'html.parser')
        ticker_value = soup.find('span', class_='SecurityInvitingScreen__priceValue_c1Ah9')
        ticker_value = ticker_value.text.strip()

        print(f'> parsing ticker value: success.')

        return ticker_value
    else:
        print(f'> parsing ticker value: error.', response.status_code)

        return 'Ошибка при получении значения.'
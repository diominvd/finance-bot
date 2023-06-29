from bs4 import BeautifulSoup
import json
import requests

from data import cursor, connection
import lines


def insert_new_user_into_database_market(user_id: int) -> None:
    try:
        cursor.execute('INSERT INTO market VALUES (?, ?)', (user_id, '[]'))
    except:
        print(f'> insert user {user_id} into database/market: error.')
    else:
        connection.commit()
        print(f'> insert user {user_id} into database/market: success.')


def check_new_ticker_existence(ticker: str) -> bool:
    response = requests.get(f'https://www.tinkoff.ru/invest/stocks/{ticker}/')
    content = BeautifulSoup(response.content, 'html.parser')
    ticker_value = content.find('span', class_='SecurityInvitingScreen__priceValue_c1Ah9')

    try:
        ticker_value = ticker_value.text.strip()
    except:
        return False
    else:
        return True


def check_new_ticker_in_database_market_user_tickers(ticker: str, user_id: int) -> bool:
    cursor.execute('SELECT tickers FROM market WHERE user_id = ?', (user_id,))

    user_tickers_from_db = select_user_tickers_from_database_market(user_id=user_id)

    if ticker in user_tickers_from_db:
        return True
    else:
        return False


def check_user_tickers_limit(tickers_list: list) -> bool:
    if len(tickers_list) == 10:
        return True
    else:
        return False


def select_user_tickers_from_database_market(user_id: int) -> list:
    cursor.execute(f'SELECT tickers FROM market WHERE user_id = ?', (user_id, ))

    # Parse tickers list: str from database and convert it to list
    user_tickers: list = json.loads(str(cursor.fetchall()[0][0].replace("'", '"')))

    return user_tickers


def tickers_line_constructor(tickers_list: list, new_ticker: str) -> str:
    tickers_list.append(new_ticker)
    
    tickers_line: str = str(json.dumps(tickers_list))

    return tickers_line

def add_new_ticker_for_user_in_database_market(user_id: int, new_ticker: str) -> str:
    if check_new_ticker_existence(ticker=new_ticker):
        if not check_new_ticker_in_database_market_user_tickers(ticker=new_ticker, user_id=user_id):

            # Fetch user tickers for check limit and formatted final message
            user_tickers: list = select_user_tickers_from_database_market(user_id=user_id)

            if not check_user_tickers_limit(tickers_list=user_tickers):

                # Generate tickers line for insert into database.
                tickers_line: str = tickers_line_constructor(tickers_list=user_tickers, new_ticker=new_ticker)

                try:
                    # Update user tickers in database/market.
                    cursor.execute('UPDATE market SET tickers = ? WHERE user_id = ?', (tickers_line, user_id))
                except:
                    print(f'> add ticker {new_ticker} to user {user_id}: error.')

                    return 'Error'
                else:
                    connection.commit()

                    print(f'> add ticker {new_ticker} to user {user_id}: success.')

                    return lines.market_lines['def_text_ticker_added'](ticker=new_ticker)
            else:
                return lines.market_lines['error_text_tickers_limit']
        else:
            return lines.market_lines['error_text_ticker_exists']
    else:
        return lines.market_lines['error_text_nonexistent_ticker']


def parse_ticker(ticker: str) -> str:
    response = requests.get(f'https://www.tinkoff.ru/invest/stocks/{ticker}/')

    # Check success of request.
    if response.status_code == 200:
        # Parse page.
        content = BeautifulSoup(response.content, 'html.parser')
        ticker_value = content.find('span', class_='SecurityInvitingScreen__priceValue_c1Ah9').text.strip()

        return ticker_value
    else:
        print(f'> parsing ticker value: error.', response.status_code)

        return 'Ошибка при получении значения.'
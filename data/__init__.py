import sqlite3


connection = sqlite3.connect('data/database.db')
cursor = connection.cursor()

# Database -> users.
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
	user_id INTEGER PRIMARY KEY UNIQUE,
	products REAL,
	cafes REAL,
	auto REAL,
	transport REAL,
	home REAL,
	entertainment REAL,
	sport REAL,
	health REAL,
	education REAL,
	gifts REAL,
	beauty REAL,
	clothes REAL,
	technic REAL,
	subscriptions REAL,
	total REAL)''')
# Database -> operations.
cursor.execute('''CREATE TABLE IF NOT EXISTS operations(
	operation_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	user_id INTEGER,
	category TEXT,
	value REAL,
	date TEXT,
	FOREIGN KEY (user_id) REFERENCES users (user_id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS market(
    user_id INTEGER UNIQUE,
    tickers TEXT,
    FOREIGN KEY (user_id) REFERENCES users (user_id))''')
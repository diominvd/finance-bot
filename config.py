import aiogram
import os


# API_TOKEN - variable of virtual environment.
bot: aiogram.Bot = aiogram.Bot(token=os.environ['API_TOKEN'], parse_mode='HTML')
dispatcher: aiogram.Dispatcher = aiogram.Dispatcher()

version: str = '2.1.0'
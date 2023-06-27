import aiogram
import os


# API_TOKEN - variable of virtual environment.
# For deploy bot on server replace 'os.environ['API_TOKEN']' to bot token.
bot: aiogram.Bot = aiogram.Bot(token=os.environ['API_TOKEN'], parse_mode='HTML')
dispatcher: aiogram.Dispatcher = aiogram.Dispatcher()

# BOT_ROM is necessary to monitor active operations that are in the process of being created.
bot_storage: dict = {}
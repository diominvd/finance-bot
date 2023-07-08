import asyncio
import logging
import time

from config import bot, dispatcher
import handlers
import database


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot, allowed_updates=dispatcher.resolve_used_update_types())

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    while True:
        try:
            asyncio.run(main())
        except Exception as e:
            time.sleep(3)
            print(e)
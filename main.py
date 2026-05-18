from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from handlers.routes import router
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(router)

async def main():
    bot = Bot(token=TOKEN)
    print("started")

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

bot.delete_webhook()

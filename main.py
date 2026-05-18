import asyncio
from aiogram import Bot, Dispatcher
from handlers.routes import router

TOKEN ="8687657673:AAFwiA1N0dKBVAXhCJD66-WECx0pNkfTG5k"

dp = Dispatcher()
dp.include_router(router)

async def main():
    bot = Bot(token=TOKEN)
    print("started")

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

bot.delete_webhook()

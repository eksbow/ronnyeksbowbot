import os
import asyncio
from aiogram import Bot, Dispatcher, types
from handlers.routes import router

# Инициализация бота и диспетчера
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Подключаем ваши хэндлеры
dp.include_router(router)

# Функция-обработчик для Cloudflare (Asynchronous Invocations)
async def fetch(request, env, ctx):
    # Если запрос пришел методом POST (это Telegram отправляет нам апдейт)
    if request.method == "POST":
        try:
            # Получаем данные апдейта от Telegram
            payload = await request.json()
            update = types.Update(**payload)
            
            # Передаем апдейт в aiogram на обработку
            await dp.feed_update(bot, update)
        except Exception as e:
            print(f"Error processing update: {e}")
            
    # Cloudflare Workers обязательно должны возвращать Response объект
    return Response.new("OK", status=200)

import os
from aiogram import Bot, Dispatcher, types
from handlers.routes import router

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(router)

async def on_fetch(request, env, ctx):
    if request.method == "POST":
        try:
            payload = await request.json()
            update = types.Update(**payload)
            await dp.feed_update(bot, update)
        except Exception as e:
            print(f"Error: {e}")
    
    return Response.new("OK", status=200)


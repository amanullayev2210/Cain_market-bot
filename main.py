from aiogram import Bot, Dispatcher
import asyncio

from handlers import handler, product

# bu yerga @BotFather dan yaratgan botingizni tokenini qo'ying
bot = Bot(token="7844588841:AAFWckK5NiAvaldtIYz3hJph6fUpitxFjow")

dp = Dispatcher()

dp.include_routers(handler.root, product.roots)

async def main():
    await dp.start_polling(bot)


asyncio.run(main())
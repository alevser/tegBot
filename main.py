import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import BOT_TOKEN
import time


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=BOT_TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я - Каори, будем знакомы! Меня создали для того, чтобы сделать мир лучше. Отправь сообщения и я подскажу, какой твой ID. ")

@dp.message()
async def message_handler(msg: types.Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
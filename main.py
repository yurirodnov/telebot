from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
import config
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.api_key)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Started!")

@dp.message(F.text == "Hello")
async def message_hello_handler(message: Message) -> None:
    await message.answer("Hello there!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
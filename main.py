from aiogram import Bot, Dispatcher, Router, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.types import Message
import texts.texts
import asyncio
import config
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.api_key)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Started!")
    
@dp.message(Command("me"))
async def command_me_handler(message: Message) -> None:
    await message.answer(f"Ты {message.from_user.id}")
    
@dp.message(F.text == 'Юра')
async def message_filter_handler(message:Message):
    await message.answer('Привет, Юра!')
    
@dp.message()
async def echo_message(message: Message):
    await message.answer(f"Нет ты {message.text}!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
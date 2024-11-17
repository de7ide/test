#echo bot stepik
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


BOT_TOKEN = 'TOKEN_BOT'


bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def hello_messae(message: Message):
    await message.answer("Hi")


@dp.message()
async def echo_mes(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)

import random
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message


BOT_TOKEN = '7149680283:AAHnk9FfQNuYmqBHdeKhXL_eSiY7Alq8JLU'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

#The number of attempts available to the user in the game
ATTAMPTS = 5

#The dictionary in which the user data will be stored
user = {'in_game': False,
        'secret_number': None,
        'attampts': None,
        'total_games': 0,
        'wins': 0}

#A function that returns a random integer from 1 to 100
def ret_random_num() -> int:
    return random.randint(1, 100)


@dp.message(Command('start'))
async def hello_func(message: Message):
    await message.answer(
        'Hello!\nDo you want to play a game "Choosi"?\n\n'
        'To get the rules of the game & a list of '
        'available commands - send the /help'
        f'\n\nYour statistiks:\nTotal games - {user['total_games']}\nWins - {user['wins']}'
    )
    if user['total_games'] == 0:
        await message.answer("Your win percentage is ZERO!")
    else:
        f'\n\nYour win percentage: {user['wins']/user['total_games']*100} %'


@dp.message(Command('help'))
async def help_func(message: Message):
    await message.answer(
        f'The rules of the game:\n\nI guess a number from 1 to 100,'
        f'and you have to guess it\nYou have {ATTAMPTS} attampts'
        f'\n\nCommands: \n/help - the rule of the game & a list'
        f'of commands\n/cancel - quit the game\n/start - view'
        f'statistics\n\nDo you want to play with me))))))))?'

    )


@dp.message(Command('cancel'))
async def cancel_func(message: Message):
    if user['in_game']:
        user['in_game'] == False
        await message.answer('You leave the game. If you want to play, write to me about it')
    else:
        await message.answer('We are not playing now.\n'
                            'Do you want to play?'
        )


@dp.message(F.text.lower().in_(['yes', 'yep', 'да', 'y', 'давай', 'play']))
async def yes_answer(message: Message):
    if not user['in_game']:
        user['in_game'] = True
        user['secret_number'] = ret_random_num()
        user['attampts'] = ATTAMPTS
        await message.answer(
            'I thought of a number from 1 to 100'
        )
    else:
        await message.answer('While we are playing the game'
                            'I can only react to numbers '
                            'from 1 to 100 & commands'
                            '/cancel & /start'
        )


@dp.message(F.text.lower().in_(['no', 'n', 'nop', 'нет', 'неа', 'н']))
async def no_func(message: Message):
    if not user['in_game']:
        await message.answer(
            'Too bad((\n\nIf you want to play'
            ' - just write about it))'
        )
    else:
        await message.answer('We are playing now...')


@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def num_answer(message: Message):
    if user['in_game']:
        if int(message.text) == user['secret_number']:
            user['in_game'] = False
            user['total_games'] += 1
            user['wins'] += 1
            await message.answer('CONGRAT!\nYOU WIN!!!'
                            'Do you want to play again?'
                            f'You did it in {5 - user['attampts']} attempts!'
            )
            num_answer()
        elif int(message.text) > user['secret_number']:
            user['attampts'] -= 1
            await message.answer(f'My num is lower\nYou have {user['attampts']} attampts')
        elif int(message.text) < user['secret_number']:
            user['attampts'] -= 1
            await message.answer(f'My num is higher\nYou have {user['attampts']} attampts')

        if user['attampts'] == 0:
            user['in_game'] = False
            user['total_games'] += 1
            await message.answer(
                'Unfortunately, you have no more'
                f'attempts. You lost...((\n\n My'
                f'num was {user['secret_number']}\n\n'
                f'Do you want to play again?'
                )
    else:
        await message.answer('We are do not playing now'
                            'Do you want to play?'
        )


@dp.message()
async def other_words_func(message: Message):
    if user['in_game']:
        await message.answer(
            'We are playing now....'
        )
    else:
        await message.answer('I do not understand you...((')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.run_polling(bot)
import logging
import requests
from extract import json_extract
from aiogram import Bot, Dispatcher, executor, types
# from googletrans import Translator

API_TOKEN = '971667728:AAHhQHwyZHebw7Xp5vc_cCC2tKFuu574Xms'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hello, my friend! \nType your word if you want to find the definition")


@dp.message_handler()
async def echo(message: types.Message):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{message.text}'
    response = requests.get(url)
    data = response.json()
    definition = json_extract(data, 'definition')

    await message.answer(f'Word: {message.text} \nDefinition of the word: \n{definition}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

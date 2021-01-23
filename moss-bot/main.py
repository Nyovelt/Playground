# dependencies
import os
import logging
import asyncio
import re
import time

# telegram bot framework https://github.com/aiogram/aiogram
from aiogram import *

# mark status
INIT, BASE_FILE, STUDENT_FILE = {
    0, 1, 2
}


# environment, init etc.
API_TOKEN = os.environ["API_TOKEN"]
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def save_file(message: types.file):
    # receieve file
    file_id = message.document.file_id
    await message.reply("file receieved. You can send me more.")

    # store file
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_name = re.search(
        "[^/\\\\<>*?|\"]+\\.[^/\\\\<>*?|\"]+", str(file_path)).group(0)  # get filename by regex
    
    # mkdir
    os.system("mkdir -p ./users/{}/{} ".format(message.from_user.id,
                                               status[message.from_user.id]))
    
    # download file
    await bot.download_file(file_path, "./users/{}/{}/{}".format(message.from_user.id, status, file_name))

    logging.debug("{} has sent file {} and stored in {}".format(message.from_user.id, file_name,
                                                                "./users/{}/{}/{}".format(message.from_user.id, status[message.from_user.id], file_name)))


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply('''Hi!\nI'm EchoBot!\nPowered by aiogram.\n 
                        Type /student to send student files one after another. i.e. the files needed moss \n
                        Then type /finish to get result''')


@dp.message_handler(commands=['base'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/base` command
    which is used for store base file
    position is at "{user.id}/base_file/"
    """
    logging.debug("{} is sending base file".format(message.from_user.id))

    # mark status as BASE_FILE
    status[message.from_user.id] = BASE_FILE

    await message.reply("Hello, {}, now send me the base file".format(message.from_user.id))


@dp.message_handler(commands=['student'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/student` command
    which is used for store student files
    i.e. the files needed examine
    position is at "{user.id}/student_file/"
    """
    logging.debug("{} is sending student files".format(message.from_user.id))

    # mark status as STUDENT_FILE
    status[message.from_user.id] = STUDENT_FILE

    await message.reply("Hello, {}, now send me the student file".format(message.from_user.id))


@dp.message_handler(commands=['finish'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/finish`  command
    Send files to standford moss and return an url
    Then remove the dir
    """
    await message.reply("Hello, {}, here is the result".format(message.from_user.id))
    result = os.popen(
        "./moss/moss   {} ".format("./users/{}/STUDENT_FILE/*".format(message.from_user.id)))

    # only url is useful
    for i in result.readlines():
        if "http" in i:
            print(i)
            await message.reply(i)
            logging.debug("Moss result \n {}: {}".format(message.from_user.id, i))

    # init
    status[message.from_user.id] = INIT
    os.system("rm -rf ./users/{}".format(message.from_user.id))
    


if __name__ == '__main__':
    status = dict()  # To store the status of users
    logging.basicConfig(level=logging.DEBUG)
    executor.start_polling(dp, skip_updates=True)

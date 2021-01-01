import json, os
from dotenv import load_dotenv
import telegram
from telegram.ext import Updater
load_dotenv()

TOKEN = os.getenv('API_TOKEN')
CHAT_ID = -428895876

# Start the bot
updater = Updater(TOKEN, use_context=True)

# counter starts at 2 because the link to Chapter 1 is at 02
with open("counter.txt","r") as f2:
    counter = json.load(f2)

with open("taleof2cities.txt","r") as f:
    chapters = f.readlines()
    link = "http://www.gutenberg.org/files/98/98-h/98-h.htm#link2H_4_00"

    # chapter 8 and 33 are section headers and should be skipped
    if counter == 8:
        counter = 9
    if counter == 33:
        counter = 34
    if len(str(counter)) == 1:
        chapter_num = '0' + str(counter)
    else:
        chapter_num = str(counter)
    # counter is always 2 more than the position in list 
    # e.g. chapters[0] = 2 in counter = Chapter 2
    current_chapter = counter - 2
    message = chapters[current_chapter] + " " + link + chapter_num

with open("counter.txt","w") as f2:
    counter += 1
    # len(chapters) = 45
    # chapters[44] is the last element in list = 46 is the last counter
    # loop back to 1 if count to 47 
    if counter >= len(chapters)+2:
        counter = 2
    json.dump(counter,f2)

bot = telegram.Bot(token = TOKEN)
bot.sendMessage(chat_id = CHAT_ID, text = message, parse_mode="HTML")

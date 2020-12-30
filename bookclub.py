import json, os
from dotenv import load_dotenv
import telegram
from telegram.ext import Updater
load_dotenv()

TOKEN = os.getenv('API_TOKEN')
CHAT_ID = -428895876

# Start the bot
updater = Updater(TOKEN, use_context=True)

with open("taleof2cities.txt","r") as f:
    story = f.read()
    # chapters[0] is empty
    chapters = story.split("CHAPTER")

with open("counter.txt","r") as f2:
    counter = json.load(f2)

with open("counter.txt","w") as f2:
    counter += 1
    if counter > len(chapters)-1:
        counter = 1
    json.dump(counter,f2)

new_chapter = chapters[counter]

bot = telegram.Bot(token = TOKEN)
bot.sendMessage(chat_id = CHAT_ID, text = new_chapter, parse_mode="Markdown")

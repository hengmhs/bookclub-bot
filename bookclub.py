import json, os
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

print(API_TOKEN)

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

#print(chapters[counter])



import json

with open("taleof2cities.txt","r") as f:
    story = f.read()
    # chapters[0] is empty
    chapters = story.split("CHAPTER")

with open("counter.txt","r") as f2:
    counter = json.load(f2)
    counter += 1
    if counter > len(chapters):
        counter = 1

with open("counter.txt","w") as f2:
    json.dump(counter,f2)



print(chapters[counter])



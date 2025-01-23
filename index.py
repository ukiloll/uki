import requests
import json

res = requests.get("https://minecraft.fandom.com/wiki/Crafting")
data = res.json()
f = open("db/user.json","w")
f.write(data)
f.close()

f = open("db/user.json","r")
obj = json.load(f.readlines())
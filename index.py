import requests
import os

res = requests.get("https://minecraft.fandom.com/wiki/Crafting")
data = res.json()
f = open("db/user.json","w")
f.write(data)
f.close()
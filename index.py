import requests

res = requests.get("https://minecraft.fandom.com/wiki/Crafting")
data = res.content
import discord
from discord.ext import commands , tasks
import requests
import json
import asyncio
intents = discord.Intents.default()  
client = commands.Bot(command_prefix = '$',intents=intents)

async def status_task():
    while True:
        try :
            getir = requests.get("https://api.binance.com/api/v3/avgPrice?symbol=USDTTRY").text
            getir = json.loads(getir)
            print(getir)
            getir_usd = round(float(getir["price"]),2)
            print(getir_usd)
            await asyncio.sleep(15)
            for guild in client.guilds:
                await guild.me.edit(nick=f"₺{getir_usd:n}")
        except :
            continue
            
try :
    @client.event
    async def on_ready():   
        client.loop.create_task(status_task())
        print('Bot hazir!')
except :
    False

client.run("bot-token")

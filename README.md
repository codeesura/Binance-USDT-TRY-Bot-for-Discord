# Binance USDT-TRY Bot for Discord

## Description

This is a discord bot that retrieves the current average price of USDT in TRY (Turkish Lira) from the Binance API every 15 seconds, and then changes its nickname in every server (guild) it's in to reflect that price.

## How to Use

1. **Install Python:** Make sure you have Python installed on your machine. The bot is written in Python, specifically version 3.8 or newer.

2. **Install the necessary Python packages:** This bot uses the discord, discord.ext, requests, and json Python packages. You can install them with pip by running the command: `pip install discord.py requests`.

3. **Configure your bot:** Replace `"bot-token"` with your actual bot token, which you can get from the Discord developer portal.

4. **Run the bot:** Run the bot with the command `python bot.py` (or whatever you've named the .py file). 

## Code

```python
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
            getir_usd = round(float(getir["price"]),2)
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
```

## Notes

- This bot's only command prefix is "$", although it doesn't have any commands in its current state.
- The bot uses Discord's new Intents system, which allows bots to subscribe to certain types of events. In this case, the bot uses the default intents, which includes events like message sends and reactions.
- The bot has a main task (`status_task`) that runs in the background when the bot is started up.This task retrieves the current USDT price, waits for 15 seconds, and then updates the bot's nickname. If it encounters an error (like a failed API call), it will continue to the next iteration of the loop.
- The `on_ready` event handler is a function that's called when the bot has successfully connected to Discord. - This is where the background task is started.
- Be careful not to share your bot token with anyone, as it can be used to take control of your bot. If you ever accidentally share your bot token, be sure to regenerate it in the Discord developer portal.

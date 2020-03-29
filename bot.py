# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('NjkzNTUwMDU2NjI4MDI3NDc1.Xn_vJA.1Sh7sJmWXQ_GDtRiLnQJZX9En2k')

client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has booted up!')
  
client.run(TOKEN)

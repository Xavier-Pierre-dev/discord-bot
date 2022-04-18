# This is a sample Python script.
import discord
from discord.ext import tasks
from discord.ext import commands
import os
from dotenv import load_dotenv, find_dotenv
import asyncio


load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")
BOT_CHANNEL = os.getenv("BOT_CHANNEL")
print("Your token : " + TOKEN)
print("Your bot channel id : " + BOT_CHANNEL)


bot = commands.Bot(command_prefix="!", case_insensitive=True)



@bot.command(name="hello", description="hello command description")
async def hello(message):
    await message.send(f"Hello {message.author.name} my friend!")

bot.run(TOKEN)
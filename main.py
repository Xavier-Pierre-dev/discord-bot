# This is a sample Python script.
import discord
from discord.ext import tasks
from discord.ext import commands
import os
from dotenv import load_dotenv, find_dotenv
import asyncio
import threading
import time
from concurrent.futures import ThreadPoolExecutor


load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")
BOT_CHANNEL = os.getenv("BOT_CHANNEL")
print("Your token : " + TOKEN)
print("Your bot channel id : " + BOT_CHANNEL)


client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


# called every 10 seconds
@tasks.loop(seconds=10)
async def my_background_task():
    await client.wait_until_ready()
    myChannel = client.get_channel(id=int(BOT_CHANNEL))
    embedMessage = discord.Embed(title="Title ALERT notification!", description="my message", color=discord.Color.blue())
    await myChannel.send(embed=embedMessage)
    await myChannel.send('embedMessage')

# called once
@tasks.loop(count=1)
async def test():
    await client.wait_until_ready()
    myChannel = client.get_channel(id=int(BOT_CHANNEL))
    embedMessage = discord.Embed(title="test : Title ALERT notification!", description="my message", color=discord.Color.blue())
    await myChannel.send(embed=embedMessage)
    await myChannel.send('embedMessage')
    await myfunc()



    while True:

        await asyncio.sleep(30)
        await myChannel.send("after 30second")
        embedMessage = discord.Embed(title="every 30sec : Title ALERT notification!", description="my message",
                                     color=discord.Color.blue())
        await myChannel.send(embed=embedMessage)

@tasks.loop(count=1)
async def sendMessage(message):
    await client.wait_until_ready()
        #myChannel = client.get_channel(id=int(BOT_CHANNEL))
        #embedMessage = discord.Embed(title="test : sendMessage !", description=message, color=discord.Color.blue())
        #await myChannel.send(embed=embedMessage)




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


async def myfunc():
    print("this is my treatment")


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

def myThread(text):
    asyncio.get_event_loop().create_task(sendMessage("my message !!!"))



def run(corofn, *args):
    loop = asyncio.new_event_loop()
    try:
        coro = corofn(*args)
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(coro)
    finally:
        loop.close()

loop = asyncio.get_event_loop()
executor = ThreadPoolExecutor(max_workers=5)



test.start()
my_background_task.start()

client.run(TOKEN)

print("hello world ! will not be printed")


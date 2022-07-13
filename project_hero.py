from asyncio import events
from email import message
from urllib import response
import discord
import random

TOKEN = ''

client = discord.Client()
@client.event
async def on_ready():
    print("{0.user} is online!".format(client))
    
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({message})')
    
    if message.author == client.user:
        return

    if message.channel.name == 'bot-testing':
        if user_message.lower() == 'hello':
            await message.channel.send(f"Hello {username}!")
            return
        elif username.lower() == "bye":
            await message.channel.send(f"Goodbye {username}!")
            return
        
        elif user_message.lower() == "!random":
            response = f"This is your random number: {random.randrange(1000000)}"
            await message.channel.send(response)
            return
        elif user_message.lower() == "!shutdown":
            response = "Turning Off!"
            await message.channel.send(response)
            exit()
    

client.run(TOKEN)

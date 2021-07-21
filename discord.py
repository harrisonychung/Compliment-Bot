#starting my discord bot which compliments a user. In the future I'd like it to remind the user to drink water every x minutes.

import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$Hello'):
    await message.channel.send('Hello!')


client.run(os.environ['TOKEN'])

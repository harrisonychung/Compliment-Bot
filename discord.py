#starting my discord bot which compliments a user. In the future I'd like it to remind the user to drink water every x minutes.

import discord
import os
import requests
import json


client = discord.Client()

def get_quote(): 
  response = request.get
  ("htttps://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote #q stands for quote / key in zenquote api

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$Hello'):
    await message.channel.send('You look great today!')


client.run(os.environ['TOKEN'])

#starting my discord bot which compliments a user. In the future I'd like it to remind the user to drink water every x minutes.

import discord
import os
import requests
import json
import random

client = discord.Client()

sad_words = ["depressed", "unhappy", "sad", "melancholy", "miserable", "downcast", "dejected"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there!",
  "You are a great person!"
]

def get_quote(): 
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " —" + json_data[0]['a']
  return(quote) #q stands for quote / key in zenquote api

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))


client.run(os.environ['TOKEN'])

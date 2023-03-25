from decouple import config
import discord

symbol = '!'
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith(symbol + 'hi'):
    await message.channel.send(f'Hello, {message.author}! \nHere {client.user}, what can i do for you?')

  if message.content.startswith(symbol + 'bye'):
    await message.channel.send(f'Bye {message.author}, have a nice day!')

client.run(config('M_TOKEN'))
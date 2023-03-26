from decouple import config
import discord
from discord.ext import commands
import datetime

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '!', intents = intents)

#Events
@bot.event
async def on_ready():
  await bot.change_presence(activity = discord.Streaming(name = "Gimme Money", url = "https://www.twitch.tv/juankicr"))
  print(f'We have logged in as {bot.user}')
  print(f"The Bot Is Loaded And Ready")

#Hi Message  
@bot.command()
async def Hi(cxt):  
  await cxt.send(f'Hello! {cxt.author}! \nThis is your helper bot {bot.user}, what can i do for you?')

#Test
@bot.command()
async def Ping(ctx):
  await ctx.send('Pong')
    
#Stats Message
@bot.command()
async def Stats(ctx):
    embed = discord.Embed(
      title = "SERVER_INFO",
      description = f'! + hi: Command #1 \n ! + Ping: Command #2', 
      timestamp = datetime.datetime.utcnow(), 
      color = discord.Color.purple())
    embed.add_field(name = "Server Owner", value = "@JuankiCR")
    embed.add_field(name = "Server Region", value = "Mexico")
    embed.set_thumbnail(url = "https://i.pinimg.com/originals/52/fd/67/52fd6714a21542abdfc167bc67969c8a.jpg")
    await ctx.send(embed = embed)

bot.run(config('M_TOKEN'))




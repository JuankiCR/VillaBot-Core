from decouple import config
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def dev_taunt(ctx, user:str = '<@500769239779770394>'):
  embed = discord.Embed(
    title='Feeling blue DEV?',
    description=f'Ohh poor little {user}',
    color=discord.Color.blurple()
  )
  embed.set_thumbnail(url='https://i.pinimg.com/564x/84/d0/21/84d0215cd93345f4c8db43139ec361ca.jpg')
  await ctx.send(embed = embed)

bot.run(config('M_TOKEN'))
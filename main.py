from decouple import config
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(description='Say hello to user or bot')
async def hi(ctx, target:discord.Member = None):
  user = ctx.message.author.mention
  if not target:
    await ctx.send(f'Hello {user}, here {bot.user.name}\nWhat can i do for you?')
  else:
    await ctx.send(f'{user} say hello to {target.mention}')

@bot.command(description='Say bye to user or bot')
async def bye(ctx, target:discord.Member = None):
  user = ctx.message.author.mention
  if not target:
    await ctx.send(f'See you {user}, have a nice day')
  else:
    await ctx.send(f'{user} say bye to {target.mention}')
  

@bot.command(description='Make a taunt to a DEV member')
async def dev_taunt(ctx, user:str = '<@500769239779770394>'):
  embed = discord.Embed(
    title='Feeling blue DEV?',
    description=f'Ohh poor little {user}',
    color=discord.Color.blurple()
  )
  embed.set_thumbnail(url='https://i.pinimg.com/564x/84/d0/21/84d0215cd93345f4c8db43139ec361ca.jpg')
  await ctx.send(embed = embed)

bot.run(config('M_TOKEN'))
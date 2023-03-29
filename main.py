from decouple import config
import datetime
import discord
from discord.ext import commands, tasks
from discord import app_commands

import functions.taunts as taunts
import functions.user_info as user_info
import functions.events as events

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

class Group(app_commands.Group):
  ...
taunts_group = Group(name='taunt', description='Commands to make jokes between members')
getting_start = Group(name='i', description='Commands set user info')

@bot.event
async def on_ready():
  print('Bot is up!')
  try:
    bot.tree.add_command(taunts_group)
    bot.tree.add_command(getting_start)
    synced  = await bot.tree.sync()
    print(f'Syced {len(synced)} command(s)')
  except Exception as e:
    print(e)
  once_a_day.start()

# ---------- Greetings commands ----------
@bot.tree.command(name='hello', description='Say hello to user or bot')
async def hello(interaction:discord.Interaction, member:discord.Member = None):
  user = interaction.user.mention
  if not member  or member == bot.user:
    await interaction.response.send_message(f'Hello {user}, here {bot.user.name}\nWhat can i do for you?', ephemeral=True)
  else:
    await interaction.response.send_message(f'{user} say hello to {member.mention}')

@bot.tree.command(name='bye', description='Say bye to user or bot')
async def bye(interaction:discord.Interaction, member:discord.Member = None):
  user = interaction.user.mention
  if not member or member == bot.user:
    await interaction.response.send_message(f'See you {user}, have a nice day', ephemeral=True)
  else:
    await interaction.response.send_message(f'{user} say bye to {member.mention}')

# ---------- Taunt commands ----------
@taunts_group.command(name='dev', description='Make a taunt to a DEV member')
async def dev_taunt(interaction:discord.Interaction, dev:discord.Member = None):
  user = bot.user.mention if not dev else dev.mention
  await interaction.response.send_message(embed = taunts.make_dev_taunt(user))

# ---------- Start commands ----------
@getting_start.command(name='am', description='Tell me who you are')
async def who_im (interaction:discord.Interaction, name:str, call_me:str = None):
  if (interaction.channel.id != 1089642319789174915):
    msg = f'Sorry, This does not seem to work here.'
  else:
    guild_id = interaction.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
    msg, role = await user_info.set_name(name, call_me, interaction.user, guild)
    if role:
      await interaction.user.add_roles(role)
  await interaction.response.send_message(msg, ephemeral=True)

# ---------- Programmed commands ----------
@tasks.loop(hours= 24)
async def once_a_day():
  channel = bot.get_channel(1089727087734165596)
  now = datetime.datetime.now()
  date = now.strftime("%Y-%m-%d")
  await channel.send(f'---------- {date} events ----------')

  for event in events.daily_update(date):
    await channel.send(embed = event)

bot.run(config('M_TOKEN'))
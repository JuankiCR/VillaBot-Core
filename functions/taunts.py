import discord

def make_dev_taunt(dev):
  embed = discord.Embed(
    title='Feeling blue DEV?',
    description=f'Ohh poor little {dev}',
    color=discord.Color.blurple()
  )
  embed.set_thumbnail(url='https://i.pinimg.com/564x/84/d0/21/84d0215cd93345f4c8db43139ec361ca.jpg')
  return embed
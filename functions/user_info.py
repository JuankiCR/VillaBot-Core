import discord

async def set_name(name = None, nick = None, user:discord.Member = None, guild = None):
    if guild:
        role = discord.utils.get(guild.roles, name = 'Users')
    else:
        role = None
    
    if name and nick:
        await user.edit(nick=nick)
        return f'{user.mention} thank you for telling me your name, now we will all call you "{nick}"\n Welcome to the server! ＼(=^‥^)/', role
    elif name and not nick:
        return f'{user.mention} thank you for telling me your name, I will not change your nickname.\n Welcome to the server! ฅ•ω•ฅ', role
    else:
        return f'Sorry {user.mention}, i need your name to this command. /ᐠᵕ̩̩̥ ‸ᵕ̩̩̥ ᐟ\\\ﾉ', role
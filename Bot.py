#imports
import discord 
from discord.ext import commands



#prefix
bot = commands.Bot(command_prefix='!')



#commands
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#events
@bot.event
async def on_ready():
    print('bot ready')




#token
bot.run('token')

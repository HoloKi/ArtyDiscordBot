import discord
import os
from discord.ext import commands
import time


client = commands.Bot(command_prefix = '.')
client.remove_command('help')

game = discord.Streaming(name='Animal Crossing: New Horizons', url='https://www.youtube.com/watch?v=HO8ctP_QNZc',game='Animal Crossing: New Horizons')
      

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('Il bot è pronto e funzionante.')
    print(client.user.name)
    print(client.user.id)
    print('------')



#check if there is a .py inside the cogs directory and load it
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



client.run('token')




import discord
from discord.ext import commands

class Purge(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Purge is online.")

    #COMANDO PER PURGARE I MESSAGGI
    @commands.command()
    @commands.has_permissions(manage_messages= True)
    async def clear(self, ctx, arg, bulk=True):
        try:
            await ctx.channel.purge(limit=int(arg))
        except ValueError:
            await ctx.send("Devi inserire un numero!")

def setup(client):
    client.add_cog(Purge(client))

import discord
from discord.ext import commands
from googlesearch import *

class Search(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Search is online.")

    #comando per la ricerca in web
    @commands.command()
    async def cerca(self,ctx, *args):
        try:
            for url in search(*args, stop=1,lang='it',country='it'):
                await ctx.send(url)
        except:
            await ctx.send("Non vedi che ho da fare!. Dopo")

def setup(client):
    client.add_cog(Search(client))

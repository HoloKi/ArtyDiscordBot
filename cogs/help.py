import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help is online.")

    # COMANDO HELP PER VEDERE QUALI COMANDI DEL BOT CI SONO

    @commands.command(pass_context = True)    
    async def help(ctx):
        embed = discord.Embed(
            color = discord.Colour.orange()  
        )
        
        embed.set_author(name='Help')
        embed.add_field(name = '.cerca', value = 'Invia il primo risultato della ricerca', inline=False)
        embed.add_field(name = '.rose', value = 'Le migliori gif di Rose', inline=False)
        embed.add_field(name = '.arty', value = 'Il meglio di Arty', inline=False)
        embed.add_field(name = '.cappu', value = 'Le migliori gif di Cappu', inline=False)
        embed.add_field(name = '.fire', value = 'Le migliori gif di Firemage', inline=False)
        embed.add_field(name = '.petty', value = 'I migliori proverbi dal mondo', inline=False)
        embed.add_field(name = '.evan', value = 'La frase meno iconica di Evan', inline=False)
        embed.add_field(name = '.nic', value = 'La miglior gif di Nic', inline=False)
        embed.add_field(name = '.clear', value = 'Permette di default di cancellare 5 messaggi precedenti, Admin only', inline=False)
        embed.add_field(name = '.yoda', value = 'Alcune gif divertenti su r6', inline=False)
        embed.add_field(name = '.canny', value = 'Le sue gif preferite', inline=False)
        embed.add_field(name = '.ping', value = 'Controlla quanto lagga Arty', inline=False)
        embed.add_field(name = 'Il bot è semplice e sviluppato col culo, abbiate pazienza.', value = 'Imparerò a programmare, lo giuro', inline=False)
        
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Help(client))

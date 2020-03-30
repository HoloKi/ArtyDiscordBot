import discord
from discord.ext import commands
random = __import__("random")

class Funny(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Funny is online.")

    #COMANDO PING
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

    #COMANDO PER FIRE
    @commands.command()
    async def fire(self, ctx):
        responses = ['https://i.kym-cdn.com/photos/images/newsfeed/001/505/718/136.jpg', #gattoschifomado
                     'https://res.cloudinary.com/lmn/image/upload/c_limit,h_360,w_640/e_sharpen:100/f_auto,fl_lossy,q_auto/v1/gameskinnyc/b/i/t/bit-heroes-skeleton-key-0dd37.png', #bit heroes
                     'https://imgur.com/a/zNHwlcp', #imgur bhchiesa crossover 
                     'https://imgur.com/a/J9iUd5L', #notre chiesa bh
                     'https://cdn02.nintendo-europe.com/media/images/10_share_images/games_15/nintendo_switch_download_software_1/H2x1_NSwitchDS_Warframe_image1600w.jpg'] #warframe
        await ctx.send(random.choice(responses))

    #COMANDO PER ROSE
    @commands.command()
    async def rose(self, ctx):
        responses = ['https://i.kym-cdn.com/photos/images/original/000/862/912/fdf.gif', #anime ass
                     'https://media.giphy.com/media/6CBGoJnEBbEWs/giphy.gif', #red taiga
                     'https://media.giphy.com/media/jTU09JLRaYCt2/giphy.gif', #taiga sfrontata
                     'https://media.giphy.com/media/wUf0jPd2ksY92/giphy.gif', #jojo balls
                     'https://media.giphy.com/media/gDciyiNcDhYXu/giphy.gif', #ohmygod joo reference
                     'https://i.kym-cdn.com/photos/images/newsfeed/000/869/852/a28.gif', #n'altro culo
                     'https://i.pinimg.com/originals/d5/8b/5b/d58b5be495a07dfda4672aaf7aa2e35b.gif', #donnasenzabocce
                     'https://media.giphy.com/media/SpzdWtMmREEaA/giphy.gif'] #taiga felice
        await ctx.send(random.choice(responses))

    #COMANDO PER CAPPU
    @commands.command()
    async def cappu(self, ctx):
        responses = ['https://tenor.com/y8kZ.gif', #ragazzo cool
                    'https://tenor.com/rpCn.gif'] #sguardo sexy
        await ctx.send(random.choice(responses))

    #COMANDO PER ARTY
    @commands.command()
    async def arty(self, ctx):
        responses = ['Lasciami stare',
                     'Vuoi un ban?',
                     'https://media.giphy.com/media/uC9e2ojJn1ZXW/giphy.gif',
                     'https://media.giphy.com/media/qPD4yGsrc0pdm/giphy.gif',
                     'Te la sei cercata',
                     'Continua cosi e ti banno',
                     'Sono pigro daiiii']
        await ctx.send(random.choice(responses))


    #COMANDO PER LE FRASI FILOSOFICHE DI PETTI
    @commands.command()
    async def petty(self, ctx):
        embed = discord.Embed(
            color = discord.Colour.red()  
        )
        
        embed.set_author(name='Saggio Petti')
        responses = ['Quando il dito indica la luna lo stolto guarda il dito',
                     'Cadi sette volte, rialzati otto',
                     'Quando piove lo stolto impreca contro gli dei, il saggio si procura un ombrello',
                     'Una coscienza pulita è il cuscino migliore',
                     'Il momento migliore per piantare un albero era 20 anni fa. Il secondo miglior momento è ora',
                     'Il nostro primo insegnante è il nostro cuore',
                     'La donna è detta creatura debole, ma un suo pelo tira più di una coppia di elefanti.',
                     'In un buon libro il meglio è tra le righe',
                     'Anche con una sella dorata un asino non diventa un cavallo',
                     'Una buona risata allunga la vita',
                     'Amare ed essere saggi è impossibile']
        embed.add_field(name = 'dile:', value = (random.choice(responses)), inline=False)
        await ctx.send(embed=embed)

    #COMANDO PER NIC
    @commands.command()
    async def nic(self, ctx):
        await ctx.send('https://media.giphy.com/media/3h40Gfu1mwk5xFAfcN/giphy.gif') #hanzo

    #COMANDO PER YODA
    @commands.command()
    async def yoda(self, ctx):
        responses = ['https://media0.giphy.com/media/26vIeEarfjFwKCEow/giphy.gif', #rainbow6
                     'https://thumbs.gfycat.com/HotElatedIbizanhound-max-1mb.gif'] #rainbowmemes
        await ctx.send(random.choice(responses))



    #COMANDO PER EVAN
    @commands.command()
    async def evan(self, ctx):
        await ctx.send('Sei bello Rose!')

    #COMANDO PER LA GIF DI CANNELLA
    @commands.command()
    async def canny(self, ctx):
        await ctx.send('https://media0.giphy.com/media/1jadHTB4xIMBgNT0xd/giphy.gif')


def setup(client):
    client.add_cog(Funny(client))

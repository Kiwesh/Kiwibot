import discord
from discord.ext import commands, tasks
from Kiwi import Kiwibot

# bot events and commands
bot = commands.Bot(command_prefix='$')
kiwibot = Kiwibot()

@tasks.loop(hours=2)
async def twitchDropsAlert():
    channel = bot.get_channel(992761127677198386)
    liveChanWithDrops = kiwibot.getTwitchDrops('Sea of Thieves')
    if len(liveChanWithDrops):
        await channel.send(len(liveChanWithDrops)+ ' streams avec des drops trouvés. Tappez $kiwidrops pour voir la liste.')

@bot.event
async def on_ready():
    twitchDropsAlert.start()

@bot.command()
async def kiwihelp(ctx):
    await ctx.send(kiwibot.kiwiHelp())

@bot.command()
async def kiwiblague(ctx):
    await ctx.send(kiwibot.kiwiBlague())

@bot.command()
async def kiwidrops(ctx):
    liveChanWithDrops = kiwibot.getTwitchDrops('Sea of Thieves')
    if not liveChanWithDrops:
        await ctx.channel.send('- Aucun drop trouvé')
    else:
        for channel in liveChanWithDrops:
            await ctx.channel.send('- '+channel)

bot.run(kiwibot.TOKEN)
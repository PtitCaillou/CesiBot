import discord
import CesiBot
from discord.ext import commands
from discord.utils import get
import os

BOT_PREFIX = '/'

bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.command(pass_context=True, aliases=['i', 'issou'])
async def issou(ctx):

    song_there = os.path.isfile("issou.mp3")
  
    #await ctx.send("Getting everything ready now")

    voice = get(bot.voice_clients, guild=ctx.guild)

    for file in os.listdir("./resources/song"):
        if file.endswith(".mp3"):
            name = file

    voice.play(discord.FFmpegPCMAudio("issou.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.5

    nname = name.rsplit("-", 2)
    #await ctx.send(f"Playing: {nname[0]}")
    print("playing\n")
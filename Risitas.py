import discord
import CesiBot
from CesiBot import bot
from discord.ext import commands
from discord.utils import get
import os


@bot.command(pass_context=True, aliases=['i', 'issou'])
async def issou(ctx):

    song_there = os.path.isfile("issou.mp3")
  
    voice = get(bot.voice_clients, guild=ctx.guild)

    for file in os.listdir("resources/song"):
        if file.endswith(".mp3"):
            name = file

    voice.play(discord.FFmpegPCMAudio("issou.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.5

    nname = name.rsplit("-", 2)
    print("playing\n")
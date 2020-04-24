import discord
from discord.utils import get
import os

async def _issou(ctx, bot):
    filename = "issou.mp3"
    filepath = os.getcwd() + "/resources/song/" + filename
    
    if os.path.isfile(filepath):
        voice = get(bot.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio(filepath), after=lambda e: print("Song ready!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.5
    
    for file in os.listdir("resources/song"):
        if file.endswith(".mp3"):
            name = file

    name = name.rsplit("-", 2)
    print("playing {}".format(name))
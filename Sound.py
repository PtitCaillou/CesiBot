import os, random

import discord
from discord.utils import get

import SoundList



async def _sound(ctx, bot, message):
    if message == None:
        _, path = random.choice(list(SoundList.sound.items()))
    else:
        if message in SoundList.sound:
            path = SoundList.sound[message]
        else:
            await ctx.send("SoundList.sound {} not found...".format(message))
            return
    
    filepath = os.getcwd() + path
    
    if os.path.isfile(filepath):
        voice = get(bot.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio(filepath), after=lambda e: print("Sound is ready!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.5

    ctx.send("Playing Sound : {}".format(message))
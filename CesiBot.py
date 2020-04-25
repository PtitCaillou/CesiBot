# Native imports


# Third party imports
import discord
from discord.ext import commands
from discord.utils import get

# Local imports
import Games, Minecraft, Sound, SoundList, Weather

bot = commands.Bot(".")



@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    dealer = Games.Dealer()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command(aliases=['j', 'joi'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Joined {channel}")

@bot.command(aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Left {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Don't think I am in a voice channel")

@bot.command(aliases=["minecraft"])
async def mc(ctx):
    await Minecraft._mc(ctx, bot)

@bot.command()
async def ftb(ctx):
    await Minecraft._ftb(ctx, bot)

@bot.command(aliases=["s", "snd", "sou"])
async def sound(ctx, message = None):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await Sound._sound(ctx, bot, message)

@bot.command(aliases=["sl", "slist", "sndlist"])
async def soundlist(ctx):
    sounds = "List of sounds :\n" + ", ".join([sound for sound in SoundList.sound])
    await ctx.send(sounds)

@bot.command(aliases=["meteo", "météo"])
async def weather(ctx, message = None):
    await Weather._weather(ctx, message)
    
@bot.command(aliases=["d", "deal"])
async def dealer(ctx, message = None):
    if message == None:
        await ctx.send("Incorrect command...")
    else:
        await Games._dealer(ctx, message)

bot.run('NzAzMTg1MzQ0NDA0OTE0MjY3.XqK6aA.b3hjFQZxb0YjgeX4UhdO211_-gY')
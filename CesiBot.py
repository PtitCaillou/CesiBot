import discord
from discord.ext import commands

bot = commands.Bot(".")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.command()
async def aled(ctx):
    await ctx.send("ALED")

bot.run('NzAzMTg1MzQ0NDA0OTE0MjY3.XqK6aA.b3hjFQZxb0YjgeX4UhdO211_-gY')
import discord, json, requests
from discord.utils import get
import os

async def _mc(ctx, bot):
    req = requests.get("https://api.mcsrvstat.us/2/ptitcaillou.tk:25565")
    await mc_process(ctx, bot, req)

async def _ftb(ctx, bot):
    req = requests.get("https://api.mcsrvstat.us/2/ptitcaillou.tk:25566")
    await mc_process(ctx, bot, req)

async def mc_process(ctx, bot, req):
    result = req.json()

    if "online" in result:
        state = ((result["online"] and "Le serveur est en ligne\n") or (not result["online"] and "Le serveur est hors-ligne\n"))
        if int(result["players"]["online"]) == 0: 
            players = "Il n'y a aucun joueur en ligne"
        elif int(result["players"]["online"]) == 1:
            players = "Il y a un joueur en ligne : " + ", ".join(result["players"]["list"])
        else:
            players = "Il y a {} joueurs en ligne : ".format(int(result["players"]["online"])) + ", ".join(result["players"]["list"])
        
        await ctx.send(state + players)
    else:
        await ctx.send("Error in fetching datas")
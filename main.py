import discord
from discord.ext import commands
import requests
import os
import webserver

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= "$", intents=intents)

@bot.command()
async def test(ctx, *args):
    respuesta = ' '.join(args)
    await ctx.send(respuesta)

@bot.event
async def on_ready():
    print (f"Hello! I'm {bot.user}, and I am here to help.")

webserver.keep_alive()
bot.run(DISCORD_TOKEN)

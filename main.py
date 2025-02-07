import discord
from discord.ext import commands
import requests
import os
import webserver
import asyncio
import datetime
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= "$", intents=intents)

channel_id = 1337213020467761329

@bot.command()
async def test(ctx, *args):
    respuesta = ' '.join(args)
    await ctx.send(respuesta)

@bot.command()
async def millicomvpn(ctx):
    respuesta = f"Hello {ctx.author.mention}, here you can find Millicom's vpn access: https://wiki.axiros.com/display/PMR/Infraestructure+and+VPN+Access"
    await ctx.send(respuesta)

@bot.command()
async def docsaxiros(ctx):
    respuesta = f"Hello {ctx.author.mention}, here you can find Axiros documentation: https://docs.axiros.com/"
    await ctx.send(respuesta)

@bot.event
async def on_ready():
    print (f"Hello! I'm {bot.user}, and I whiling to help.")

webserver.keep_alive()
bot.run(DISCORD_TOKEN)

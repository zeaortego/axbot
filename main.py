import discord
from discord.ext import commands
import requests
import os
import webserver #Keep the bot alive, check webserver.py
import asyncio
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN") #Variable stored using dotenv

intents = discord.Intents.default()
intents.message_content = True

#Discord channel in which it responds (optional)
channel_id = 1337213020467761329

#Bot command prefix
bot = commands.Bot(command_prefix= "$", intents=intents)

#Command list
@bot.command()
async def commandls(ctx):
    response = f"Hello {ctx.author.mention}, this is the list of commands you can use:"
    list ="""
    - $commandls: Command list.

    - $vpns: Link to Axiros vpns.

    - $millicomvpn: Link to Millicom's vpn access.

    - $docsaxiros: Link to Axiros's documentation.

    - $devinstances: Link to Development Instances.

    - $accesscustomersupp: Link to Access and Customer support.

    - $products: Link to Axiros's products.

    - $internal: Link to Axiros's internal user git repositories.

    - $pythonhelp: List of the best sites to learn python.
    
    """
    await ctx.send(f'{response}\n```diff\n{list}\n```')
#Test
@bot.command()
async def test(ctx, *args):
    response = ' '.join(args)
    await ctx.send(response)

#VPN Commands:
@bot.command()
async def vpns(ctx):
    response = f"Hello {ctx.author.mention}, here you can find a link to a list of vpns used: https://wiki.axiros.com/display/AC/VPNs+Axiros+LATAM"
    await ctx.send(response)

@bot.command()
async def millicomvpn(ctx):
    response = f"Hello {ctx.author.mention}, here you can find a link to Millicom's vpn access: https://wiki.axiros.com/display/PMR/Infraestructure+and+VPN+Access"
    await ctx.send(response)

@bot.command()
async def telecentrovpn(ctx):
    response = f"Hello {ctx.author.mention}, here you can find a link to Telecentro's vpn access: https://wiki.axiros.com/pages/viewpage.action?spaceKey=EO&title=New+Telecentro%3A+VPN+ACCESS"
    await ctx.send(response)    

#Documentation commands:
@bot.command()
async def docsaxiros(ctx):
    response = f"Hello {ctx.author.mention}, here you can find a link to Axiros's documentation: https://docs.axiros.com/"
    await ctx.send(response)

@bot.command()
async def products(ctx):
    response = f"Hello {ctx.author.mention}, here you can find a link to Axiros's list of products: https://wiki.axiros.com/display/PDC/Product+Information+Hub"
    await ctx.send(response)

@bot.command()
async def internal(ctx):
    response = f"Hello {ctx.author.mention}, here you can find a link to Axiros's Internal information: https://wiki.axiros.com/display/DEV/Axiros+internal+user+git+repositories"
    await ctx.send(response)

@bot.command()
async def devinstances(ctx):
    response = f"Hello {ctx.author.mention}, here you can find a link to Axiros's Development Instances: https://wiki.axiros.com/pages/viewpage.action?spaceKey=AC&title=Development+Instances"
    await ctx.send(response)

@bot.command()
async def accesscustomersupp(ctx):
    response = f"Hello {ctx.author.mention}, here you can find a link to Axiros's Access and Custommer support: https://wiki.axiros.com/display/AC/Access+and+Customer+on+Support"
    await ctx.send(response) 

#Misc
@bot.command()
async def pythonhelp(ctx):
    response = f"""Hello {ctx.author.mention},
    there are several excellent resources to learn Python, depending on your learning style and goals. Here are some of the top websites for learning Python:
    - **Python.org**

    - **Real Python**

    - **W3Schools**

    - **Codecademy**

    - **freeCodeCamp**

    - **LeetCode**

    - **SoloLearn**

    - **The Python Tutorial by Python Software Foundation**

    """
    await ctx.send(response)

    
@bot.event
async def on_ready():
    print (f"Hello! I'm {bot.user}, and I whiling to help.")

webserver.keep_alive()
bot.run(DISCORD_TOKEN)

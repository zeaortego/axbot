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

async def send_friday_message():
    await client.wait_until_ready()
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send("¡El bot está en línea y enviando mensajes de prueba! 🎉")
    while not client.is_closed():
        # Obtener el día de la semana actual (0=lunes, 1=martes, ..., 4=viernes)
        now = datetime.datetime.now()
        # Si es viernes (4), envia el mensaje
        if now.weekday() == 4:  # 4 es viernes
            channel = client.get_channel(channel_id)
            if channel:
                await channel.send("It's friday! do not forget to log your working ours 🎉")
            # Espera 1 semana (604800 segundos) para enviar el mensaje el siguiente viernes
            await asyncio.sleep(604800)
        else:
            # Si no es viernes, esperar hasta el próximo viernes
            days_until_friday = (4 - now.weekday()) % 7  # Días restantes hasta el viernes
            await asyncio.sleep(days_until_friday * 86400)  # Espera los días restantes

@bot.command()
async def test(ctx, *args):
    respuesta = ' '.join(args)
    await ctx.send(respuesta)

@bot.command()
async def millicomvpn():
    print ("Here you can find Millicom's vpn access: https://wiki.axiros.com/display/PMR/Infraestructure+and+VPN+Access")
    await ctx.send(respuesta)

@bot.event
async def on_ready():
    print (f"Hello! I'm {bot.user}, and I whiling to help.")

webserver.keep_alive()
bot.run(DISCORD_TOKEN)


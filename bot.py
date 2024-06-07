import discord
from discord.ext import commands
import re
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

# Reklam engellemeyi açıp kapatan değişken
reklam_engel = True

@client.event
async def on_ready():
    print(f'Bot {client.user} olarak giriş yaptı!')

@client.command()
async def naber(ctx):
    await ctx.send(f'İyiyim sen {ctx.author.mention}')

@client.command()
async def selam(ctx):
    await ctx.send('aleykümselam')

@client.command()
async def reklamengel(ctx):
    global reklam_engel
    reklam_engel = not reklam_engel
    await ctx.send(f'Reklam engelleme: {reklam_engel}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if reklam_engel:
        # Linkleri kontrol etmek için regex kullanımı
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        if re.search(regex, message.content):
            await message.delete()
            msg = await message.channel.send(f"{message.author.mention}, link paylaşmak yasaktır!")
            await asyncio.sleep(3)
            await msg.delete()

    await client.process_commands(message)

TOKEN = 'BOT_TOKEN'
client.run(TOKEN)

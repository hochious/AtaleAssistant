import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")  # 之後會用環境變數方式存 token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(TOKEN)
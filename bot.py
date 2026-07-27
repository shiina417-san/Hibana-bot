import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

import random

hibana_replies = [
    "こんひばな〜！どうどう？元気かな〜？",
    "こ〜んひ〜ばな〜！今日も楽しそうだね〜！",
    "こんひばな〜！今日の配信も頑張るよ〜！！",
    "こんひばな〜！ヒバナーのみんな…ヒバナが居なくて暇だったよね？",
    "こ〜んひ〜ばな〜！！チャンネル登録、高評価…よろしくね！！",
    "こんひばな〜！暇人なのかな〜？"
]

@bot.event
async def on_ready():
    print(f"{bot.user} がログインしました！")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if "こんひばな" in message.content.lower():
        await message.channel.send(random.choice(hibana_replies))

    await bot.process_commands(message)

import os

bot.run(os.environ["DISCORD_TOKEN"])

import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

import random

hibana_replies = [
    "それな〜！",
    "卑猥すぎるとBANされちゃう！",
    "えっちじゃない！",
    "それでよし！",
    "正解！",
]

@bot.event
async def on_ready():
    print(f"{bot.user} がログインしました！")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if "えろくない" in message.content.lower():
        await message.channel.send(random.choice(hibana_replies))

    await bot.process_commands(message)

import os

bot.run(os.environ["DISCORD_TOKEN"])

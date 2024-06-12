import discord
from discord.ext import commands
from answering import get_answer

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
    print('Готово!')


@client.event
async def on_message(message: discord.Message):
    if message.mentions and message.mentions[0] == client.user:
        msg = get_answer(message.content)
        await message.reply(msg, mention_author=False)


client.run('token')  # <-- Токен бота !

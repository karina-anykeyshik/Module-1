import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def pasw(ctx, length=10):
await ctx.send(gen_pass(length))
@bot.command()
async def joined(ctx, member: discord.Member):
"""Says when a member joined."""
await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

bot.run("MTE0MTU5Nzk5MTk5Njc1NjA0MA.GpxL86.kepJ8_TiGVdQzWWxE2o2sMF5aTsS6LIEwEJ1VA")

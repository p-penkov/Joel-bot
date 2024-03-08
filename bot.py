import discord
from discord.ext import commands
from config import TOKEN
import random

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is up and ready!")
    try: 
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello {interaction.user.mention}, how are you?")

@bot.tree.command(name="thoughts")
async def drug(interaction: discord.Interaction):
    drug = random.randint(1, 5)
    if drug == 1:
        await interaction.response.send_message("I feel happy talking to a friend.")
    elif drug == 2:
        await interaction.response.send_message("I'm scared of chickens. Why do they have beaks?")
    elif drug == 3:
        await interaction.response.send_message("I want to be a bird.")
    elif drug == 4:
        await interaction.response.send_message("I've been thinking about the universe. What if it was made by a goose and a bear at the end of time?")
    elif drug == 5:
        await interaction.response.send_message("Having thought about the world a lot lately, it is safe to say it is wonderful, my friend.")

bot.run(TOKEN)
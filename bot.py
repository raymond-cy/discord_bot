import os
import discord
from discord.ext import commands

token = os.getenv("DISCORD_BOT_TOKEN")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

class PlayView(discord.ui.View):
    def get_content(self, label):
        counter = {
            "scissors":"stone",
            "stone":"paper",
            "paper":"scissors"
        }
        return f"You choose x{label}, Bot! choose{counter[label]}, you lost"
    
    @discord.ui.button(label="scissors", style=discord.ButtonStyle.green, emoji="✂")
    async def scissors(self, interaction: discord.Interaction, button:discord.ui.Button):
        await interaction.response.edit_message(content=self.get_content(button.label))
    
    @discord.ui.button(label="stone", style=discord.ButtonStyle.green, emoji="🧱")
    async def stone(self, interaction: discord.Interaction, button:discord.ui.Button):
        await interaction.response.edit_message(content=self.get_content(button.label))
    
    @discord.ui.button(label="paper", style=discord.ButtonStyle.green, emoji="📄")
    async def paper(self, interaction: discord.Interaction, button:discord.ui.Button):
        await interaction.response.edit_message(content=self.get_content(button.label))
    
    @discord.ui.button(label="quit", style=discord.ButtonStyle.red)
    async def stop(self, interaction: discord.Interaction, button:discord.ui.Button):
        await interaction.response.edit_message(content="You stop the game", view=None)
    
@bot.command()
@commands.has_permissions(administrator=True)
async def synccommands(ctx):
    await bot.tree.sync()
    await ctx.send("Sync Success")

@bot.hybrid_command()
async def ping(ctx):
    """check whether the robot is online or not"""
    await ctx.send("pong")

@bot.hybrid_command()
async def add(ctx, a:int, b:int):
    """add two number"""
    await ctx.send(a+b)

@bot.hybrid_command()
async def play(ctx):
    """paper, scissors, and stone"""
    await ctx.send("Make your choice", view = PlayView())

bot.run(token)
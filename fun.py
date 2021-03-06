from discord.ext.commands import Cog, command
from random import choice

class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(aliases=["funny"])
    async def meme(self, ctx):
        """
        Sends a very meaningful statistic
        """
        await ctx.send("Every 60 seconds, a minute passes in Africa.")

    @command(aliases=["watchdoggo", "dog", "doggo"])
    async def watchdog(self, ctx):
        """
        Interact with the doggo
        """
        await ctx.send(choice["Bark", "Woof"])

    @command(aliases=["test", "game"])
    async def quiz(self, ctx):
        """
        Test your knowledge!
        """
        await ctx.send("hello")

    @command(aliases=["funfact", "funfacts"])
    async def trivia(self, ctx):
        """
        Sends a random fun fact
        """
        await ctx.send("hello") # inside parentheses: choice[...]

def setup(bot):
    bot.add_cog(Fun(bot))

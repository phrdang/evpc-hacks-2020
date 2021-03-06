from discord.ext.commands import Cog, command


class Utility(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def cmd5(self, ctx):
        """
        Add docstring here
        """
        await ctx.send("hello")


def setup(bot):
    bot.add_cog(Utility(bot))

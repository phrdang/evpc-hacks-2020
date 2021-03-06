from discord.ext.commands import Cog, command


class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def cmd1(self, ctx):
        """
        Add docstring here
        """
        await ctx.send("hello")


def setup(bot):
    bot.add_cog(Fun(bot))

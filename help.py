from discord.ext.commands import Cog, command


class Help(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def cmd2(self, ctx):
        """
        Add docstring here
        """
        await ctx.send("hello")


def setup(bot):
    bot.add_cog(Help(bot))

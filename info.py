from discord.ext.commands import Cog, command, MissingRequiredArgument
from typing import Optional


class Info(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def warcrimes(self, ctx, *query: Optional[str]):
        """
        Sends info about war crimes
        """
        # if-else with if query is None for example
        await ctx.send("hello")

    @command()
    async def warlaws(self, ctx, *query: Optional[str]):
        """
        Sends info about laws or int'l agreements relating to wars
        """
        await ctx.send("hello")


def setup(bot):
    bot.add_cog(Info(bot))

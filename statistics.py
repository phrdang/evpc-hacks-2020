from discord.ext.commands import Cog, command


class Statistics(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def deaths(self, ctx, *name: Optional[str]):
        """
        Sends the # of total estimated deaths in the specified war
        """
        await ctx.send("hello")

    @command()
    async def war(self, ctx, *name: Optional[str]):
        """
        Sends info about the specified war
        """
        await ctx.send("hello")

    @command(aliases=["period"])
    async def era(self, ctx, *name: Optional[str]):
        """
        Sends info about wars in the specified era
        """
        await ctx.send("hello")

    @command(aliases=["time", "date", "dates", "years"])
    async def when(self, ctx, *name: Optional[str]):
        """
        Sends date range for the specified war
        """
        await ctx.send("hello") # show start date-end date

    @command(aliases=["place", "location", "area", "region"])
    async def where(self, ctx, *name: Optional[str]):
        """
        Sends the regions for where the specified war happened
        """
        await ctx.send("hello")

    @command(aliases=["combatants", "sides"])
    async def who(self, ctx, *name: Optional[str]):
        """
        Sends the combatants/countries involved in the specified war
        """
        await ctx.send("hello")

    @command(aliases=["desc", "description", "notes", "about"])
    async def what(self, ctx, *name: Optional[str]):
        """
        Sends a description of the specified war
        """
        await ctx.send("hello")

    # parsing war names and numbers -- method, no async

def setup(bot):
    bot.add_cog(Statistics(bot))

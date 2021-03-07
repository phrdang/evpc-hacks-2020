from discord.ext.commands import Cog, command
from colors import DARK_GREEN, LIGHT_GREEN, RUST
from discord import Embed
from typing import Optional

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

    @command(aliases=["credits"])
    async def sources(self, ctx):
        """
        Sends the sources we used for statistics
        """
        await ctx.send("hello")

    @command(aliases=["fought_wars", "involvedin", "involved_in"])
    async def foughtwars(self, ctx, country):
        """
        Sends a list of wars a country/group was involved in
        """
        await ctx.send("hello")

    @command(aliases=["max", "maximum", "maximumdeaths", "max_deaths"])
    async def maxdeaths(self, ctx, country):
        """
        Sends war with highest total deaths
        """
        await ctx.send("hello")

    @command(aliases=["min", "minimum", "minimumdeaths", "min_deaths"])
    async def mindeaths(self, ctx, country):
        """
        Sends war with lowest total deaths
        """
        await ctx.send("hello")

    @command(aliases=["avg", "average", "averagedeaths", "average_deaths"])
    async def avgdeaths(self, ctx, country):
        """
        Sends average death total
        """
        await ctx.send("hello")

    @command(aliases=["med", "median", "meddeaths", "median_deaths", "med_deaths"])
    async def mediandeaths(self, ctx, country):
        """
        Sends median death total
        """
        await ctx.send("hello")

    @command(aliases=["graph", "graphic"])
    async def chart(self, ctx, *, query: Optional[str]):
        """
        Sends a visual of a certain statistic
        """

        options = [
        "1. Non-state: Conflicts by year (1989-2019)",
        "2. Non-state: Conflicts by region (1989-2019)",
        "3. Non-state: Fatalities by year (1989-2019)",
        "4. Non-state: Fatalities by region (1989-2019)",
        "5. One-sided: Fatalities by year (including Rwanda 1994) (1989-2019)"]

        URL = ["https://ucdp.uu.se/downloads/charts/graphs/png_20/nsconf_per_year.png",
        "https://ucdp.uu.se/downloads/charts/graphs/png_20/nsconf_by_region.png",
        "https://ucdp.uu.se/downloads/charts/graphs/png_20/fat_in_nsconf.png",
        "https://ucdp.uu.se/downloads/charts/graphs/png_20/fat_in_nsconf_by_region.png",
        "https://ucdp.uu.se/downloads/charts/graphs/png_20/fat_in_osv_incrw.png"]

        if query is None:
            description = ""

            for o in options:
                description += o + "\n"

            embed = Embed(
            title="Options",
            description=description,
            color=LIGHT_GREEN)

            await ctx.send(embed=embed)

        else:
            index = 0

            if query.isdigit():
                index = int(query) - 1
            else:
                for i in range(len(query)):
                    if query == options[i]:
                        index = i - 1
            
            embed = Embed(
                title=options[index],
                description="",
                color=LIGHT_GREEN)

            embed.set_image(url=URL[index])
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Statistics(bot))

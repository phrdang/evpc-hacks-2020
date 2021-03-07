from discord.ext.commands import Cog, command
from typing import Optional
from discord import Embed
from colors import DARK_GREEN, LIGHT_GREEN, RUST


class Statistics(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def deaths(self, ctx, *, name: Optional[str]):
        """
        Sends the # of total estimated deaths in the specified war
        """
        for war in self.bot.wars:
            if war.name.lower() == name.lower() or name.lower() in [
                alias.lower() for alias in war.aliases
            ]:
                if war.upper_deaths != war.lower_deaths:
                    await ctx.send(
                        f"The {war.name} had {war.lower_deaths}-{war.upper_deaths} deaths."
                    )
                else:
                    await ctx.send(
                        f"The {war.name} had {war.lower_deaths} deaths."
                    )
                return

        await ctx.send("War not found")

    @command()
    async def war(self, ctx, *, name: Optional[str]):
        """
        Sends info about the specified war
        """
        await ctx.send("hello")

    @command(aliases=["period"])
    async def era(self, ctx, *, name: Optional[str]):
        """
        Sends info about wars in the specified era
        """
        await ctx.send("hello")

    @command(aliases=["time", "date", "dates", "years"])
    async def when(self, ctx, *, name: Optional[str]):
        """
        Sends date range for the specified war
        """
        for war in self.bot.wars:
            if war.name.lower() == name.lower() or name.lower() in [
                alias.lower() for alias in war.aliases
            ]:
                embed = Embed(
                    title=f"When the {war.name} happened",
                    color=RUST,
                )

                # find start and end dates
                dates = war.date_range.split('-')
                start = dates[0]
                if len(dates) == 2:
                    end = dates[1]
                else:
                    end = dates[0]

                embed.add_field(
                    name="Start Year",
                    value=start,
                )
                embed.add_field(
                    name="End Year",
                    value=end,
                )
                embed.add_field(
                    name="Duration in Years",
                    value=war.duration(),
                )

                await ctx.send(embed=embed)
                return
        await ctx.send("War not found")

    @command(aliases=["place", "location", "area", "region"])
    async def where(self, ctx, *, name: Optional[str]):
        """
        Sends the regions for where the specified war happened
        """
        for war in self.bot.wars:
            if war.name.lower() == name.lower() or name.lower() in [
                alias.lower() for alias in war.aliases
            ]:
                embed = Embed(
                    title=f"Location of the {war.name}",
                    description=war.location,
                    color=RUST,
                )
                await ctx.send(embed=embed)
                return
        await ctx.send("War not found")

    @command(aliases=["combatants", "sides"])
    async def who(self, ctx, *, name: Optional[str]):
        """
        Sends the combatants/countries involved in the specified war
        """
        for war in self.bot.wars:
            if war.name.lower() == name.lower() or name.lower() in [
                alias.lower() for alias in war.aliases
            ]:
                embed = Embed(
                    title=f"Combatants in the {war.name}",
                    description=war.combatants,
                    color=RUST,
                )
                await ctx.send(embed=embed)
                return
        await ctx.send("War not found")

    @command(aliases=["desc", "description", "notes", "about"])
    async def what(self, ctx, *, name: Optional[str]):
        """
        Sends a description of the specified war
        """
        for war in self.bot.wars:
            if war.name.lower() == name.lower() or name.lower() in [
                alias.lower() for alias in war.aliases
            ]:
                embed = Embed(
                    title=f"About the {war.name}",
                    description=war.description,
                    color=RUST,
                )
                embed.add_field(
                    name="Notes",
                    value=war.notes if war.notes else "None",
                )
                await ctx.send(embed=embed)
                return
        await ctx.send("War not found")


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
    async def chart(self, ctx, *country: Optional[str]):
        """
        Sends a visual of a certain statistic
        """
        await ctx.send("hello")


def setup(bot):
    bot.add_cog(Statistics(bot))

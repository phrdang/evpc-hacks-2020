from discord.ext.commands import Cog, command


class Utility(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def ping(self, ctx):
        """
        Pings the bot
        """
        await ctx.send(f"Pong! {round (self.bot.latency * 1000)} ms")


def setup(bot):
    bot.add_cog(Utility(bot))

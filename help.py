from discord.ext.commands import Cog, command
from typing import Optional
from discord import Embed

import colors


class Help(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(brief="Shows a list of commands or info on a specific command")
    async def help(self, ctx, command: Optional[str]):
        """
        Shows a list of commands or info on a specific command

        **Arguments**
            `cmd`: name of command to get info on (optional)
        """
        if command is None:
            # display list of commands and briefs
            embed = Embed(
                title="Watchdog Help",
                description="List of commands and descriptions",
                color=colors.DARK_GREEN,
            )

            for cmd in self.bot.commands:
                embed.add_field(
                    name=self.bot.command_prefix + cmd.qualified_name,
                    value=cmd.brief,
                    inline=False,
                )

            await ctx.send(embed=embed)
        else:
            # display specific command info
            valid_cmd = False
            for cmd in self.bot.commands:
                if cmd.qualified_name == command.lower():
                    valid_cmd = True
                    command = cmd
                    break

            if valid_cmd:
                embed = Embed(
                    title=f"Watchdog Help - {command.qualified_name} command",
                    description=command.brief,
                    color=colors.LIGHT_GREEN,
                )

                embed.add_field(
                    name="Aliases",
                    value=", ".join(command.aliases) if command.aliases else "None",
                )
                embed.add_field(name="Cog", value=command.cog.qualified_name)
                print(command.usage)

                await ctx.send(embed=embed)
            else:
                await ctx.send("Command not found")


def setup(bot):
    bot.add_cog(Help(bot))

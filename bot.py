from discord.ext.commands import Bot as BotBase
from discord.flags import Intents
from dotenv import load_dotenv
import os


PREFIX = ">"
OWNER_IDS = [
    616465633156005919,  # Yoobin
    528349146608959489,  # Rebecca
]


class Bot(BotBase):
    def __init__(self):
        super().__init__(
            command_prefix=PREFIX,
            owner_ids=OWNER_IDS,
            intents=Intents.all(),
            help_command=None,  # disable default help cmd
        )

    def run(self):
        print("Running bot")

        # Load cogs
        COGS = [
            "fun",
            "help",
            "info",
            "statistics",
            "utility",
        ]
        for cog in COGS:
            self.load_extension(cog)

        # Get token
        load_dotenv()
        self.TOKEN = os.getenv("BOT_TOKEN")

        # run bot with token
        super().run(self.TOKEN, reconnect=True)

    async def on_ready(self):
        print("Bot ready")

    async def on_connect(self):
        print("Bot connected")

    async def on_disconnect(self):
        print("Bot disconnected")


# Creates bot instance and runs it
bot = Bot()
bot.run()

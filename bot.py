from discord.ext.commands import Bot as BotBase
from discord.flags import Intents
from dotenv import load_dotenv
import os
from war import War


PREFIX = ">"
OWNER_IDS = [
    616465633156005919,  # Yoobin
    528349146608959489,  # Rebecca
]
WAR_STATS_FILE_PATH = "./data/war_stats.tsv"


class Bot(BotBase):
    def __init__(self):
        super().__init__(
            command_prefix=PREFIX,
            owner_ids=OWNER_IDS,
            intents=Intents.all(),
            help_command=None,  # disable default help cmd
        )
        self.load_data(WAR_STATS_FILE_PATH)

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

    def load_data(self, file_path):
        """
        Loads war data from given file path

        Args:
            file_path (str): path to .tsv file with war data
        """
        # open war stats data in read mode
        self.wars = []
        file = open(file_path, "r")

        # CSV columns:
        # Era	War	Death range	Date	Combatants	Location	Notes	Aliases	Description	Source
        for line in file.readlines():
            items = line.split("\t")  # tab-separated values

            # Strip leading and trailing whitespace
            for i in range(len(items)):
                items[i] = items[i].strip()

            # skip first row (column headings)
            if items[0] == "Era":
                continue

            era = items[0]
            name = items[1]
            death_range = items[2].replace("+", "")  # remove + symbols
            date = items[3]
            combatants = items[4]
            location = items[5]
            notes = items[6]

            # turn aliases into a list
            aliases = [alias.strip() for alias in items[7].split(",")]

            description = items[8]
            source = items[9]

            # figure out upper and lower deaths
            deaths = death_range.split("-")
            lower_deaths = deaths[0]
            if len(deaths) == 2:
                upper_deaths = deaths[1]
            else:
                upper_deaths = deaths[0]

            # append War object
            self.wars.append(
                War(
                    name,
                    aliases,
                    upper_deaths,
                    lower_deaths,
                    combatants,
                    era,
                    date,
                    description,
                    location,
                    notes,
                    source,
                )
            )


# Creates bot instance and runs it
bot = Bot()
bot.run()

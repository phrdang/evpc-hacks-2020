class War:
    def __init__(
        self,
        name,
        aliases,
        upper_deaths,
        lower_deaths,
        combatants,
        era,
        date_range,
        description,
        location,
        notes,
        source,
    ):
        self.name = name
        self.aliases = aliases
        self.upper_deaths = upper_deaths
        self.lower_deaths = lower_deaths
        self.combatants = combatants
        self.era = era
        self.date_range = date_range
        self.description = description
        self.location = location
        self.notes = notes
        self.source = source

    def duration(self):
        pass
        # txt = self.bot.date_range.split("-")
        # start_year = txt[0]
        # end_year = txt[1]

        # if (start_year.contains("BC") and end_year.contains("BC")):
        #     return abs(self.end_year - self.start_year) # a and not b or b not a
        # else if (start_year.contains("BC") XOR )

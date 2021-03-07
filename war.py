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
        txt = self.date_range.split("-")
        start_year = txt[0]
        end_year = txt[1]

        if ("BC" in start_year and not ("BC" in end_year)) or (
            "BC" in end_year and not ("BC" in start_year)
        ):
            return self.start_year + self.end_year
        else:
            return abs(self.end_year - self.start_year)

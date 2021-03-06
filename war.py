class War:
    def __init__(self, name, aliases, upper_deaths, lower_deaths, combatants, era, 
    start_year, end_year, description, location, notes, source):
        self.name = name
        self.aliases = aliases
        self.upper_deaths = upper_deaths
        self.lower_deaths = lower_deaths
        self.combatants = combatants
        self.era = era
        self.start_year = start_year
        self.end_year = end_year
        self.description = description
        self.location = location
        self.notes = notes
        self.source = source

    def duration(self):
        return self.end_year - self.start_year
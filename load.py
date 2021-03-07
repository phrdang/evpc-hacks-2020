from war import War


WAR_STATS_FILE_PATH = "./data/war_stats.tsv"


def load_data(file_path):
    """
    Loads war data from given file path

    Args:
        file_path (str): path to .tsv file with war data
    """
    # open war stats data in read mode
    wars = []
    file = open(file_path, "r")

    # CSV columns:
    # Era	War	Death range	Date	Combatants	Location	Notes	Aliases	Description	Source
    for line in file.readlines():
        print("line", line)
        items = line.split("\t")  # tab-separated values
        print("items", items)  # get individual column values

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
        wars.append(
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
    print(wars[0].aliases)


load_data(WAR_STATS_FILE_PATH)

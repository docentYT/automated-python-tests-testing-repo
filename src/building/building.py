class Building():
    def __init__(self, levels: int, flats: int, entrances: int, color: str) -> None:
        self.levels = levels
        self.flats = flats
        self.entrances = entrances
        self.color = color

    def __str__(self):
        return f"This {self.color} building has {self.levels} levels, {self.flats} flats and {self.entrances} entrances."

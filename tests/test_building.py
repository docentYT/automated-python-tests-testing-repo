from building.building import Building


def test_building():
    building = Building(3, 6, 2, "yellow")
    assert str(building) == "This yellow building has 3 levels, 6 flats and 2 entrances."

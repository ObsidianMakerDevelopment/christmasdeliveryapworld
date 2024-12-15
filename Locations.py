from BaseClasses import Location
import typing


class AdvData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str


class ChristmasDeliveryAdvancement(Location):
    game: str = "ChristmasDelivery"


advancement_table = {}

for i,color in enumerate(["aqua", "beige", "brown", "blue", "chartreuse", "coral", "crimson", "darkcyan", "darkorange", "orange", "deepskyblue", "fuchsia", "green"]):
    advancement_table[color.title()+ " house"] = AdvData(1000+i, 'Board')

exclusion_table = {
}

events_table = {
}

lookup_id_to_name: typing.Dict[int, str] = {data.id: item_name for item_name, data in advancement_table.items() if data.id}
from BaseClasses import Item
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool


class ChristmasDeliveryItem(Item):
    game: str = "ChristmasDelivery"


item_table = {
}
for i,color in enumerate(["aqua", "beige", "brown", "blue", "chartreuse", "coral", "crimson", "darkcyan", "darkorange", "orange", "deepskyblue", "fuchsia", "green"]):
    item_table[color.title()+" gift"] = ItemData(1000+i, True)

required_items = {
}

item_frequencies = {

}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}
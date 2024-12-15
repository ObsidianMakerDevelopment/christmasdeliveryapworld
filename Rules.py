from worlds.generic.Rules import set_rule
from BaseClasses import MultiWorld, CollectionState

# Sets rules on entrances and advancements that are always applied
def set_rules(world: MultiWorld, player: int):
    for color in ["aqua", "beige", "brown", "blue", "chartreuse", "coral", "crimson", "darkcyan", "darkorange", "orange", "deepskyblue", "fuchsia", "green"]:
        
        set_rule(world.get_location(f"{color.title()} house",player), lambda state, gift=f"{color.title()} gift": state.has(gift, player))
                 
        # c = color.title()
        # def s(c):
        #     def r(state):
        #         return state.has(c+" gift",player,1)
        #     set_rule(world.get_location(c+" house",player), r)
        # s(c)

# Sets rules on completion condition
def set_completion_rules(world: MultiWorld, player: int):

    completion_requirements = lambda state: \
        all([state.has(x.title()+" gift",player,1) for x in ["aqua", "beige", "brown", "blue", "chartreuse", "coral", "crimson", "darkcyan", "darkorange", "orange", "deepskyblue", "fuchsia", "green"]])
    world.completion_condition[player] = lambda state: completion_requirements(state)
from typing import Iterable

class Skill:
    def __init__(self, name, range, damage_modifier, fatigue_cost,ap_cost, special_effects : Iterable):
        self.name = name
        self.range = range
        self.damage_modifier = damage_modifier
        self.fatigue_cost = fatigue_cost
        self.ap_cost = ap_cost
        self.special_effects = special_effects
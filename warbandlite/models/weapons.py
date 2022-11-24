from typing import Iterable

class Weapon:
    def __init__(self, name, raw_damage, armour_damage_percent, fatigue_malus, weapon_skills : Iterable):
        self.name = name
        self.raw_damage = raw_damage
        self.armour_damage_percent = armour_damage_percent
        self.fatigue_malus = fatigue_malus
        self.weapon_skills = weapon_skills
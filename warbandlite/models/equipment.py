from typing import Iterable

class Equipment:
    def __init__(self, name, move_modifier, ap_modifier, armour_modifier, stamina_modifier, equipment_skills : Iterable):
        self.name = name
        self.move_modifier = move_modifier
        self.ap_modifier = ap_modifier
        self.armour_modifier = armour_modifier
        self.stamina_modifier = stamina_modifier
        self.equipment_skills = equipment_skills
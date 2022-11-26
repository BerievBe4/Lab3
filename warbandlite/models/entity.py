import string
from typing import Iterable
from warbandlite.constants.weaponSkills import Skills
from warbandlite.constants.status_effects import Status_effects
from warbandlite.constants.weapon_list import Weapons
from warbandlite.models import custom_stat
from warbandlite.models import status_effect
from warbandlite.models.equipment import Equipment

class Entity:
    def __init__(self, name, base_damage : int, experience : int, move : custom_stat, action_points : custom_stat, health : custom_stat,
     armour : custom_stat, stamina : custom_stat, weapons, equipment):
        self.name = name
        self.move = move
        self.experience = experience
        self.action_points = action_points
        self.base_damage = base_damage
        self.health = health
        self.armour = armour
        self.stamina = stamina
        self.equipment = equipment
        self.weapons = weapons
        for wp in weapons:
            self.stamina.remaining_value += wp.fatigue_malus
            self.stamina.cumulative_modifier += wp.fatigue_malus
        for eq in equipment:
            self.move.cumulative_modifier += eq.move_modifier
            self.move.remaining_value += eq.move_modifier
            self.action_points.cumulative_modifier += eq.ap_modifier
            self.action_points.remaining_value += eq.ap_modifier
            self.armour.cumulative_modifier += eq.armour_modifier
            self.armour.remaining_value += eq.armour_modifier
            self.stamina.cumulative_modifier += eq.stamina_modifier
            self.stamina.remaining_value += eq.stamina_modifier
        self.status_effects = []

    def equip_item(self, equipment : Equipment):
        self.equipment.append(equipment)
        self.move.cumulative_modifier += equipment.move_modifier
        self.move.check_overflow()   
        self.action_points.cumulative_modifier += equipment.ap_modifier
        self.action_points.check_overflow()   
        self.armour.cumulative_modifier += equipment.armour_modifier
        self.armour.check_overflow()   
        self.stamina.cumulative_modifier += equipment.stamina_modifier
        self.stamina.check_overflow()

    def equip_weapon(self, weapon : Weapons):
        self.weapons.append(weapon)
        self.stamina.cumulative_modifier += weapon.fatigue_malus
        self.stamina.check_overflow()

    def drop_item(self, equipment : Equipment):
        if equipment in self.equipment:
            self.equipment.remove(equipment)
            self.move.cumulative_modifier -= equipment.move_modifier
            self.move.check_overflow()   
            self.action_points.cumulative_modifier -= equipment.ap_modifier
            self.action_points.check_overflow()
            self.armour.cumulative_modifier -= equipment.armour_modifier
            self.armour.check_overflow()   
            self.stamina.cumulative_modifier -= equipment.stamina_modifier
            self.stamina.check_overflow()   

    def drop_weapon(self, weapon : Weapons):
        if weapon in self.weapons:
            self.weapons.remove(weapon)
            self.stamina.cumulative_modifier -= weapon.fatigue_malus
            self.stamina.check_overflow()   

    def take_attack(self, damage : int, armour_damage_percent : float, status_effects : Iterable):
        health_damage = damage*(1 - armour_damage_percent)
        armour_damage = damage*armour_damage_percent;
        if self.armour.remaining_value > armour_damage:
            self.armour.remaining_value -= armour_damage
        else:
            health_damage += armour_damage - self.armour.remaining_value
            self.armour.remaining_value = 0           
        self.health.remaining_value -= health_damage
        for effect in status_effects:
            self.status_effects.append(effect)

    def make_attack(self, weapon : Weapons, skill : string):
        selectedWeapom = None
        if weapon in self.weapons:
            selectedWeapon = weapon

        selectedSkill = Skills.available_skills[skill]
        if self.stamina.remaining_value < selectedSkill.fatigue_cost or self.action_points.remaining_value < selectedSkill.ap_cost:
            return None
        else:
            self.stamina.remaining_value -= selectedSkill.fatigue_cost
            self.action_points.remaining_value -= selectedSkill.ap_cost
        inflicted_effects = []
        for effect in selectedSkill.special_effects:
            inflicted_effects.append(Status_effects.effects[effect])

        return (self.base_damage + selectedWeapon.raw_damage) * selectedSkill.damage_modifier, selectedWeapon.armour_damage_percent, inflicted_effects 

    def pass_turn(self):
        for effect in self.status_effects:
            self.health.remaining_value -= effect.direct_damage
            effect.duration -= 1
            if effect.duration == 0:
                self.status_effects.remove(effect)

        self.health.remaining_value += self.health.regen_rate
        self.health.check_overflow()   
        self.action_points.remaining_value += self.action_points.regen_rate
        self.action_points.check_overflow()   
        self.armour.remaining_value += self.armour.regen_rate
        self.armour.check_overflow()   
        self.move.remaining_value += self.move.regen_rate
        self.move.check_overflow()   
        self.stamina.remaining_value += self.stamina.regen_rate
        self.stamina.check_overflow()   



        


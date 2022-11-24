from typing import Iterable
from warbandlite.models.status_effect import *
from warbandlite.models.weapons import *

class Weapons(object):
    available_weapons = {"knife" : Weapon("Knife", 5, 0.9, -4, ["stab_knife","slash_knife", "puncture_knife"]),
            "maul" : Weapon("Maul", 30, 0.3, -10, ["batter_maul", "strike_down_maul"]),
            "sword" : Weapon("Sword", 15, 0.7, -8, ["slash_sword", "decapitate_sword"])}
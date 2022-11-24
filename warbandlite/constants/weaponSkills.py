from typing import Iterable
from warbandlite.models.skill import *

class Skills(object):
        available_skills = {"stab_knife" : Skill("Stab",1,0.8, 4, 2, ["bleed"]),
        "slash_knife" : Skill("Slash",1,0.5, 3, 3, []),
        "puncture_knife" : Skill("puncture",1, 1.2, 8, 5, []),
        "batter_maul" : Skill("Batter", 1, 1, 7, 8, []),
        "strike_down_maul" : Skill("Strike down",1, 0.5, 12, 12, ["stun"]),
        "slash_sword" : Skill("Slash",1,0.6, 4, 6, []),
        "decapitate_sword" : Skill("Decapitate",1,2, 15, 10, ["bleed", "stun"])}


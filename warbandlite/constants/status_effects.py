from typing import Iterable
from warbandlite.models.status_effect import *

class Status_effects(object):
    effects = {"bleed" : Status_Effect("Bleeding" ,2 , 10, 0, 0),
        "root" : Status_Effect("Rooted" , 1, 0, 1, 0),
        "stun" : Status_Effect("Stunned", 1, 0, 1, 1),
        "acid" : Status_Effect("Acid", 2, 20, 0, 0)}
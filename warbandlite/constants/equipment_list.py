from typing import Iterable
from warbandlite.models.status_effect import *
from warbandlite.models.equipment import Equipment

class Equipment(object):
    available_equipment = {"extra_padding" : Equipment("Extra padding", 0, 0, 10, -5, []),
        "waystalker_boots" : Equipment("Waystalker boots", 1, 2, -20, -5, []),
        "water_flask" : Equipment("Extra padding", 0, 0, 0, 15, []),
        "company_banner" : Equipment("Company banner", -2, 1, 0, 10, [])}
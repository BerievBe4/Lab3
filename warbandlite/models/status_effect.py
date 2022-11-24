from typing import Iterable

class Status_Effect:
    def __init__(self, name, duration, direct_damage, prevents_move, prevents_attacks):
        self.name = name
        self.duration = duration
        self.direct_damage = direct_damage
        self.prevents_move = prevents_move
        self.prevents_attacks = prevents_attacks
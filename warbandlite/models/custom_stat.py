class Custom_stat:
    def __init__(self, max_value, regen_rate, cumulative_modifier):
        self.max_value = max_value
        self.regen_rate = regen_rate
        self.cumulative_modifier = cumulative_modifier
        self.remaining_value = max_value + cumulative_modifier

    @property
    def possible_max(self):
        return self.max_value + self.cumulative_modifier

    def check_overflow(self):
        if self.remaining_value >= self.possible_max:
                self.remaining_value = self.possible_max
from warbandlite.models.custom_stat import Custom_stat

def test_stats_remaining_value_sets_as_intended_without_malus():
    armour = Custom_stat(100, 0, 0)
    assert armour.remaining_value == 100


def test_stats_remaining_value_sets_as_intended_with_malus():
    armour = Custom_stat(100, 0, -10)
    assert armour.remaining_value == 90

def test_stats_get_max_possible_works_correctly():
    armour = Custom_stat(100, 0, -10)
    assert armour.possible_max == 90

def test_stats_get_max_possible_works_correctly_after_decrease():
    armour = Custom_stat(100, 0, -10)
    armour.cumulative_modifier -= 20
    assert armour.possible_max == 70

def test_stats_overflow_works():
    armour = Custom_stat(100, 0, -10)
    armour.remaining_value += 8
    armour.check_overflow()
    assert armour.possible_max == 90

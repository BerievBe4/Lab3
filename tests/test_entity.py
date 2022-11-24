from warbandlite.constants.status_effects import Status_effects
from warbandlite.models.entity import Entity
from warbandlite.models.custom_stat import Custom_stat
from warbandlite.constants.weapon_list import Weapons
from warbandlite.constants.equipment_list import Equipment

def getBasicHuman():
    move = Custom_stat(5,0,0)
    action_points = Custom_stat(20,0,0)
    health = Custom_stat(100,0,0)
    armour = Custom_stat(70,0,0)
    stamina = Custom_stat(70,10,0)
    weapons = [Weapons.available_weapons["sword"], Weapons.available_weapons["maul"]]
    equipment = [Equipment.available_equipment["extra_padding"], Equipment.available_equipment["water_flask"]]
    basic_human = Entity("Basic human", 10, 0, move, action_points, health, armour, stamina, weapons, equipment)
    return basic_human

def test_entity_stamina_malus():
    human = getBasicHuman()
    assert human.stamina.remaining_value == 62

def test_entity_max_armour():
    human = getBasicHuman()
    assert human.armour.possible_max == 80

def test_entity_max_armour():
    human = getBasicHuman()
    assert human.armour.possible_max == 80

def test_entity_equip_boots_stat_changes():
    human = getBasicHuman()
    human.equip_item(Equipment.available_equipment["waystalker_boots"])
    assert human.stamina.remaining_value == 57

def test_entity_equip_second_maul_stat_changes():
    human = getBasicHuman()
    human.equip_weapon(Weapons.available_weapons["maul"])
    assert human.stamina.remaining_value == 52

def test_entity_equip_boots_equipment_changes():
    human = getBasicHuman()
    boots = Equipment.available_equipment["waystalker_boots"]
    human.equip_item(boots)
    assert boots in human.equipment

def test_entity_equip_second_maul_weapon_changes():
    human = getBasicHuman()
    maul = Weapons.available_weapons["maul"]
    human.equip_weapon(maul)
    assert maul in human.weapons

def test_entity_drop_padding_stat_changes():
    human = getBasicHuman()
    human.drop_item(Equipment.available_equipment["extra_padding"])
    assert human.armour.remaining_value == 70

def test_entity_drop_second_maul_stat_changes():
    human = getBasicHuman()
    human.drop_weapon(Weapons.available_weapons["maul"])
    assert human.stamina.remaining_value == 62

def test_entity_drop_padding_equipment_changes():
    human = getBasicHuman()
    padding = Equipment.available_equipment["extra_padding"]
    human.drop_item(padding)
    assert padding not in human.equipment

def test_entity_drop_second_maul_weapon_changes():
    human = getBasicHuman()
    maul = Weapons.available_weapons["maul"]
    human.drop_weapon(maul)
    assert maul not in human.weapons

def test_entity_attack_with_maul():
    human = getBasicHuman()
    maul = Weapons.available_weapons["maul"]
    result = human.make_attack(maul, "batter_maul")
    assert result == (40, 0.3, [])

def test_entity_attack_with_sword():
    human = getBasicHuman()
    sword = Weapons.available_weapons["sword"]
    result = human.make_attack(sword, "slash_sword")
    assert result == (15, 0.7, [])

def test_entity_attack_with_sword_no_stamina():
    human = getBasicHuman()
    human.stamina.remaining_value = 2
    sword = Weapons.available_weapons["sword"]
    result = human.make_attack(sword, "slash_sword")
    assert result == None

def test_entity_attack_with_sword_no_ap():
    human = getBasicHuman()
    human.action_points.remaining_value = 2
    sword = Weapons.available_weapons["sword"]
    result = human.make_attack(sword, "slash_sword")
    assert result == None

def test_entity_take_maul_hit_full_armour():
    human = getBasicHuman()
    maul = Weapons.available_weapons["maul"]
    result = human.make_attack(maul, "batter_maul")
    human.take_attack(result[0], result[1], result[2])
    assert human.armour.remaining_value == 68 and human.health.remaining_value == 72

def test_entity_take_maul_hit_armour_breaks():
    human = getBasicHuman()
    human.armour.remaining_value = 10
    maul = Weapons.available_weapons["maul"]
    result = human.make_attack(maul, "batter_maul")
    human.take_attack(result[0], result[1], result[2])
    assert human.health.remaining_value == 70

def test_entity_take_maul_hit_no_armour():
    human = getBasicHuman()
    human.armour.remaining_value = 0
    maul = Weapons.available_weapons["maul"]
    result = human.make_attack(maul, "batter_maul")
    human.take_attack(result[0], result[1], result[2])
    assert human.health.remaining_value == 60

def test_entity_take_sword_hit_debuffs_apply_correct():
    human = getBasicHuman()
    maul = Weapons.available_weapons["sword"]
    result = human.make_attack(maul, "decapitate_sword")
    bleed = Status_effects.effects["bleed"]
    stun = Status_effects.effects["stun"]
    human.take_attack(result[0], result[1], result[2])
    assert len(human.status_effects) == 2 and bleed in human.status_effects and stun in human.status_effects

def test_entity_restore_stats():
    human = getBasicHuman()
    human.stamina.remaining_value = 60
    human.pass_turn()
    assert human.stamina.remaining_value == 62

def test_entity_take_bleed_damage():
    human = getBasicHuman()
    bleed = Status_effects.effects["bleed"]
    stun = Status_effects.effects["stun"]
    human.status_effects.append(bleed)
    human.status_effects.append(stun)
    human.pass_turn()
    assert len(human.status_effects) == 1 and bleed in human.status_effects and stun not in human.status_effects and human.health.remaining_value == 90

        
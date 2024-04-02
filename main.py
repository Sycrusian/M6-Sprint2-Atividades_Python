from classes.film import Film
from classes.villager import Villager
from classes.mage import Mage


# S2-07 | 💪 Atividade: Métodos Especiais

# if __name__ == "__main__":
#     john_wick = Film('John Wick', 113)
#     print(john_wick)
#     print(len(john_wick))
#     print(vars(john_wick))



# S2-09 | 💪 Atividade: Lógica Herança de Classes

if __name__ == "__main__":
    villager = Villager("Villager")
    mage = Mage("Mage")

    print(
        "*"*50,
        "Esperado: {'name': 'Villager', 'health': 50, 'defense': 0, 'attack': 0, 'is_alive': True}",
        f"Resultado: {vars(villager)}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 100}",
        f"Resultado: {vars(mage)}",
        "*"*50,
        sep="\n"
    )
    
    battle_result = mage.fire_ball(villager)

    print(
        "*"*50,
        "Esperado: 20",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Villager', 'health': 20, 'defense': 0, 'attack': 0, 'is_alive': True}",
        f"Resultado: {vars(villager)}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 80}",
        f"Resultado: {vars(mage)}",
        "*"*50,
        sep="\n"
    )

    battle_result = mage.normal_attack(villager)

    print(
        "*"*50,
        "Esperado: 10",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Villager', 'health': 10, 'defense': 0, 'attack': 0, 'is_alive': True}",
        f"Resultado: {vars(villager)}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 80}",
        f"Resultado: {vars(mage)}",
        "*"*50,
        sep="\n"
    )

    battle_result = mage.fire_ball(villager)

    print(
        "*"*50,
        f"Esperado: {(False, 'Target is dead!')}",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Villager', 'health': 0, 'defense': 0, 'attack': 0, 'is_alive': False}",
        f"Resultado: {vars(villager)}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 60}",
        f"Resultado: {vars(mage)}",
        "*"*50,
        sep="\n"
    )

    battle_result = mage.fire_ball(villager)

    print(
        "*"*50,
        f"Esperado: {(False, 'Target is dead!')}",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        f"Esperado: 40",
        f"Resultado: {mage.mana}",
        "*"*50,
        sep="\n"
    )

    battle_result = mage.fire_ball(villager)
    battle_result = mage.fire_ball(villager)
    battle_result = mage.fire_ball(villager)

    print(
        "*"*50,
        f"Esperado: {(False, 'Not enough mana!')}",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )
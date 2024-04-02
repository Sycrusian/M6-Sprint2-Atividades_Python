from classes.film import Film
from classes.villager import Villager
from classes.mage import Mage
from datetime import datetime, timedelta


# S2-07 | 💪 Atividade: Métodos Especiais

# if __name__ == "__main__":
#     john_wick = Film('John Wick', 113)
#     print(john_wick)
#     print(len(john_wick))
#     print(vars(john_wick))



# S2-09 | 💪 Atividade: Lógica Herança de Classes

# if __name__ == "__main__":
#     villager = Villager("Villager")
#     mage = Mage("Mage")

#     print(
#         "*"*50,
#         "Esperado: {'name': 'Villager', 'health': 50, 'defense': 0, 'attack': 0, 'is_alive': True}",
#         f"Resultado: {vars(villager)}",
#         "*"*50,
#         sep="\n"
#     )

#     print(
#         "*"*50,
#         "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 100}",
#         f"Resultado: {vars(mage)}",
#         "*"*50,
#         sep="\n"
#     )
    
#     battle_result = mage.fire_ball(villager)

#     print(
#         "*"*50,
#         "Esperado: 20",
#         f"Resultado: {battle_result}",
#         "*"*50,
#         sep="\n"
#     )

#     print(
#         "*"*50,
#         "Esperado: {'name': 'Villager', 'health': 20, 'defense': 0, 'attack': 0, 'is_alive': True}",
#         f"Resultado: {vars(villager)}",
#         "*"*50,
#         sep="\n"
#     )

#     print(
#         "*"*50,
#         "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 80}",
#         f"Resultado: {vars(mage)}",
#         "*"*50,
#         sep="\n"
#     )

#     battle_result = mage.normal_attack(villager)

#     print(
#         "*"*50,
#         "Esperado: 10",
#         f"Resultado: {battle_result}",
#         "*"*50,
#         sep="\n"
#     )

#     print(
#         "*"*50,
#         "Esperado: {'name': 'Villager', 'health': 10, 'defense': 0, 'attack': 0, 'is_alive': True}",
#         f"Resultado: {vars(villager)}",
#         "*"*50,
#         sep="\n"
#     )

#     print(
#         "*"*50,
#         "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 80}",
#         f"Resultado: {vars(mage)}",
#         "*"*50,
#         sep="\n"
#     )

#     battle_result = mage.fire_ball(villager)

#     print(
#         "*"*50,
#         f"Esperado: {(False, 'Target is dead!')}",
#         f"Resultado: {battle_result}",
#         "*"*50,
#         sep="\n"
#     )

#     print(
#         "*"*50,
#         "Esperado: {'name': 'Villager', 'health': 0, 'defense': 0, 'attack': 0, 'is_alive': False}",
#         f"Resultado: {vars(villager)}",
#         "*"*50,
#         sep="\n"
#     )

#     print(
#         "*"*50,
#         "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 60}",
#         f"Resultado: {vars(mage)}",
#         "*"*50,
#         sep="\n"
#     )

#     battle_result = mage.fire_ball(villager)

#     print(
#         "*"*50,
#         f"Esperado: {(False, 'Target is dead!')}",
#         f"Resultado: {battle_result}",
#         "*"*50,
#         sep="\n"
#     )

#     print(
#         "*"*50,
#         f"Esperado: 40",
#         f"Resultado: {mage.mana}",
#         "*"*50,
#         sep="\n"
#     )

#     battle_result = mage.fire_ball(villager)
#     battle_result = mage.fire_ball(villager)
#     battle_result = mage.fire_ball(villager)

#     print(
#         "*"*50,
#         f"Esperado: {(False, 'Not enough mana!')}",
#         f"Resultado: {battle_result}",
#         "*"*50,
#         sep="\n"
#     )



# S2-12 | 💪 Atividade: Datetime


if __name__ == "__main__":
    STR_FORMAT = "%d/%m/%Y %H:%M:%S"
    test_performed_at = datetime.now()
    print(test_performed_at)
    date_test_str = "Data de realização do exame: " + test_performed_at.strftime(STR_FORMAT)
    TIME_TEST_RESULT = timedelta(days=2)
    print(TIME_TEST_RESULT)
    test_result_schedule = test_performed_at + TIME_TEST_RESULT
    print(test_result_schedule)
    result_schedule_str = "Previsão de entrega do resultado: " + test_result_schedule.strftime(STR_FORMAT)
    print("^_" * 26 + "^")
    print(date_test_str)
    print(result_schedule_str)
    print("^_" * 26 + "^")

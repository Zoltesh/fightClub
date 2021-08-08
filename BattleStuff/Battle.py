import random

"""
Index 0 is False while the player begins the animation and True when it is time to return to start point.
Index 1 is False while the player has not completed their turn and True when their turn has completed.

"""


def Battle(player1, player2, attacker):
    random_list = [0, 0]

    guard = False

    my_random = int(random.randint(1, 2))

    if my_random == 1:

        attacker[0] = 2

        random_list[0] += 1

        p1_guard = random.randint(1, 100)

        if p1_guard <= int(player1.playerAgility):

            guard = True

            if guard:
                p2_reduced_attack = player2.playerAttack - player2.playerAttack * (player1.playerDefense / 100)

                player1.playerHp -= p2_reduced_attack
                print(player1.playerName, "Guarded attack.", "Damage received reduced from:", player2.playerAttack,
                      "to:", p2_reduced_attack)
                print(player1.playerHp, "remaining.")

        else:

            player1.playerHp -= player2.playerAttack
            print(player1.playerName, "Took", player2.playerAttack, "damage!", player1.playerHp, "remaining.")

    elif my_random == 2:

        attacker[0] = 1

        random_list[1] += 1

        p2_guard = random.randint(1, 100)

        if p2_guard <= int(player2.playerAgility):

            guard = True

            if guard:
                p1_reduced_attack = player2.playerAttack - player2.playerAttack * (player1.playerDefense / 100)

                player2.playerHp -= p1_reduced_attack
                print(player2.playerName, "Guarded attack.", "Damage received reduced from:", player1.playerAttack,
                      "to:", p1_reduced_attack)
                print(player2.playerHp, "remaining.")

            else:

                player2.playerHp -= player1.playerAttack
                print(player2.playerName, "Took", player1.playerAttack, "damage!", player2.playerHp, "remaining.")

    else:
            print("Random number didn't work. No player starts")

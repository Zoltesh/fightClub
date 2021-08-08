

def AdjustStats(player1, player2):

    p1Adjuster = player1.playerLevel / 100
    p2Adjuster = player2.playerLevel / 100

    player1.playerHp *= p1Adjuster
    player1.playerAttack *= p1Adjuster
    player1.playerDefense *= p1Adjuster
    player1.playerAgility *= p1Adjuster
    player1.playerGuard *= p1Adjuster

    player2.playerHp *= p2Adjuster
    player2.playerAttack *= p2Adjuster
    player2.playerDefense *= p2Adjuster
    player2.playerAgility *= p2Adjuster
    player2.playerGuard *= p2Adjuster
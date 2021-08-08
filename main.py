from WindowStuff.Window import *
from CharacterStuff.UpdateCharacters import *
from BattleStuff.Battle import *
from BattleStuff.AdjustStats import *

WIDTH, HEIGHT = 1200, 675
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Fight Club")
characterList = []

DARK_BLUE = (30, 30, 50)
WHITE = (255, 255, 255)

FPS = 60

GOKU_IMAGE = pygame.image.load(os.path.join('Assets', 'Goku.png'))
VEGETA_IMAGE = pygame.image.load(os.path.join('Assets', 'Vegeta.png'))
reverse_vegeta = pygame.image.load(os.path.join('Assets', 'VegetaR.png'))
blue_vegeta = pygame.image.load(os.path.join('Assets', 'VegetaBlue.png'))


def main():
    readInCharacters(characterList)

    player1 = characterList[0]
    player2 = characterList[1]

    AdjustStats(player1, player2)

    attacker = [0]
    clock = pygame.time.Clock()

    new_window = Window()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

        if player1.playerHp > 0 and player2.playerHp > 0:
            Battle(player1, player2, attacker)

            if attacker[0] == 1:

                while not Window.reverse_player1[1]:
                    P1_Attack(Window.player1_rect, Window.player2_rect, Window.player1_rotation,
                              Window.player2_rotation,
                              Window.reverse_player1, Window.reverse_player2)

                    new_window.draw_fight(Window.player1_rect, Window.player2_rect, Window.player1_rotation[0],
                                          Window.player2_rotation[0])

                Window.reverse_player1 = [False, False]

            elif attacker[0] == 2:

                while not Window.reverse_player2[1]:
                    P2_Attack(Window.player1_rect, Window.player2_rect, Window.player1_rotation,
                              Window.player2_rotation,
                              Window.reverse_player1, Window.reverse_player2)

                    new_window.draw_fight(Window.player1_rect, Window.player2_rect, Window.player1_rotation[0],
                                          Window.player2_rotation[0])

                Window.reverse_player2 = [False, False]

            else:

                print("Not sure what happened...")

        else:

            if player1.playerHp <= 0:
                KO(player2, player1)

            elif player2.playerHp <= 0:
                KO(player1, player2)


    pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

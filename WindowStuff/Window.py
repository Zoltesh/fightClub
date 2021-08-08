from CharacterStuff.Character import *

STATIC_WIDTH, STATIC_HEIGHT = 426, 568


def P1_Attack(p1, p2, p1_rotation, p2_rotation, p1_reverse, p2_reverse):

    max_width = p2.centerx
    max_height = p2.centery - p2.centery / 8
    max_rotation = -45

    if p1.centerx >= p2.centerx and p1.centery <= p2.centery and p1_rotation[0] <= -45:
        p1_reverse[0] = True

    if not p1_reverse[0]:

        if p1.centerx <= max_width:
            p1.x += 20

        if p1.centery >= max_height and p1_rotation[0] > -45:
            p1.y -= 5

        if p1_rotation[0] > max_rotation and p1.centery <= max_height:
            p1_rotation[0] -= 15

        if p1_rotation[0] <= -45 and p1.centerx < p2.centerx and p1.centery < p2.centery:
            p1.y += 5

    if p1_reverse[0]:

        if p1.x > 313:
            p1.x -= 20

        if p1.y < 334:
            p1.y += 5

        if p1_rotation[0] < 0:
            p1_rotation[0] += 15

        if p1.x <= 313 and p1.y >= 334 and p1_rotation[0] >= 0:
            p1_reverse[1] = True


def P2_Attack(p1, p2, p1_rotation, p2_rotation, p1_reverse, p2_reverse):

    max_width = p1.centerx
    max_height = p1.centery - p1.centery / 8
    max_rotation = 45

    if p2.centerx <= p1.centerx and p2.centery <= p1.centery and p2_rotation[0] >= 45:
        p2_reverse[0] = True

    if not p2_reverse[0]:

        if p2.centerx >= max_width:
            p2.x -= 20

        if p2.centery >= max_height and p2_rotation[0] < 45:
            p2.y -= 5

        if p2_rotation[0] < max_rotation and p2.centery <= max_height:
            p2_rotation[0] += 15

        if p2_rotation[0] >= 45 and p2.centerx > p1.centerx and p2.centery < p1.centery:
            p2.y += 5

    if p2_reverse[0]:

        if p2.x < 887:
            p2.x += 20

        if p2.y < 334:
            p2.y += 5

        if p2_rotation[0] > 0:
            p2_rotation[0] -= 15

        if p2.x >= 887 and p2.y >= 334 and p2_rotation[0] <= 0:
            p2_reverse[1] = True


def KO(winner, loser):

    print(loser.playerName, "has fainted!")
    print(winner.playerName, "is the winner with,", winner.playerHp, "hp remaining!")


class Window:

    DARK_BLUE = (30, 30, 50)
    WHITE = (255, 255, 255)

    reverse_player1 = [False, False]
    reverse_player2 = [False, False]

    player1_rect = pygame.Rect(313, 334, STATIC_WIDTH, STATIC_HEIGHT)
    player2_rect = pygame.Rect(887, 334, STATIC_WIDTH, STATIC_HEIGHT)

    player1_rotation = [0]
    player2_rotation = [0]

    def __init__(self, width=1200, height=675, color=DARK_BLUE):

        self.width = width
        self.height = height
        self.color = color

        self.WIN = pygame.display.set_mode((self.width, self.height))
        self.WIN.fill(self.color)

        pygame.display.update()

    def change_color(self, color):

        self.WIN.fill(color)
        pygame.display.update()

    def draw_fight(self, player1, player2, player1_rotation, player2_rotation):

        self.WIN.fill(self.DARK_BLUE)
        goku = pygame.transform.rotate(GOKU_IMAGE, player1_rotation)
        vegeta = pygame.transform.rotate(VEGETA_IMAGE, player2_rotation)

        rect1 = goku.get_rect()
        rect1.center = player1.x, player1.y

        rect2 = vegeta.get_rect()
        rect2.center = player2.x, player2.y

        self.WIN.blit(vegeta, rect2)
        self.WIN.blit(goku, rect1)

        pygame.display.update()

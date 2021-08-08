import pygame
import os

"""
Character object and methods
"""

GOKU_IMAGE = pygame.image.load(os.path.join('Assets', 'Goku.png'))
VEGETA_IMAGE = pygame.image.load(os.path.join('Assets', 'Vegeta.png'))
reverse_vegeta = pygame.image.load(os.path.join('Assets', 'VegetaR.png'))
blue_vegeta = pygame.image.load(os.path.join('Assets', 'VegetaBlue.png'))


class Character:

    def __init__(self, playerId, playerName, playerLevel, playerHp, playerAttack, playerDefense, playerAgility,
                 playerGuard):
        """

        :param playerId: Unique player identifier
        :param playerName: Player name, not necessarily unique
        :param playerLevel: Player level increases stats. (playerLevel/100 * stat)
        :param playerHp: Player max health points
        :param playerAttack: Player base attack damage
        :param playerDefense: Player base defense
        :param playerAgility: Increases chance to guard attack
        :param playerGuard: Reduces damage received


        """
        self.playerId = playerId
        self.playerName = playerName
        self.playerLevel = playerLevel
        self.playerHp = playerHp
        self.playerAttack = playerAttack
        self.playerDefense = playerDefense
        self.playerAgility = playerAgility
        self.playerGuard = playerGuard

    def changeId(self, newId):
        self.playerId = newId

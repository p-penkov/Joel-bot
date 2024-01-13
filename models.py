from enum import Enum
import pygame
import random

class Suits(Enum):
  CLUB = 0
  SPADE = 1
  HEART = 2
  DIAMOND = 3

class Card:
  suit = None
  value = None
  image = None

  def __init__(self, suit, value):
    self.suit = suit
    self.value = value
    self.image = pygame.image.load('images/' + self.suit.name + '-' + str(self.value) + '.svg')
import pygame
class Next(pygame.sprite.Sprite):
  def __init__(self,x,y):
    '''
    initializes a sprite that brings the player to the next level
    args: x = x coordinate, y = y coordinate
    '''
    super().__init__()
    self.image = pygame.image.load("assets/beet.png")
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
  def collidecheck(self,sprite):
    '''
    checks to see if sprite collided with player
    sprite = player sprite
    '''
    return pygame.sprite.spritecollideany(self,sprite)
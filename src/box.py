import pygame

class Branch(pygame.sprite.Sprite):
  def __init__(self,x,y):
    '''
    platform for game
    args: x = x coordinate
    y = y coordinate
    '''
    super().__init__()
    self.image = pygame.image.load("assets/box.png")
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    print("box created")

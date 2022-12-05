import pygame
class Harvey(pygame.sprite.Sprite):
  def __init__(self):
    '''
    initializes harvey sprite
    args and returns: none
    '''
    super().__init__()
    self.image = pygame.image.load("assets/harvey.png")
    self.rect = self.image.get_rect()
    self.rect.x = 600
    self.rect.y = 450
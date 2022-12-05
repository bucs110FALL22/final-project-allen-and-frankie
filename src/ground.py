import pygame

class Ground(pygame.sprite.Sprite):
  def __init__(self,x,y):
    super().__init__()
    self.image = pygame.image.load("assets/ground.png")
    self.image_scale = pygame.transform.scale(self.image,(x,y))
    self.rect = self.image_scale.get_rect()
    self.rect.x = 0
    self.rect.y = 450
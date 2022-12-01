import pygame
class Menu():
  def __init__(self):
    super().__init__()
    self.button = pygame.image.load("assets/menu_img.png")
    self.rect = self.button.get_rect()
    # pygame.Surface.blit(self.button,1,1)

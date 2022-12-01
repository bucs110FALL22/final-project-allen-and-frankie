import pygame
from src.player import Player
from src.bearcat import Bearcat
from src.menu import Menu
from src.river import River
class Controller:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((1600,800))
    self.bg = pygame.image.load("assets/background.jpg")
    self.bear = Bearcat()
    self.river = River()
    self.ply = Player("cs")
    self.menu = Menu()
    
    self.sprites = pygame.sprite.Group()
    
    self.sprites.add(self.river)
    self.sprites.add(self.ply)
    self.sprites.add(self.bear)
    self.screen_x = self.screen.get_width

    # ground_height = -60
    self.STATE = "menu"
  def mainloop(self):
    while self.STATE == "menu":

      self.button = pygame.image.load("assets/menu_img.png")
      self.screen.blit(self.button,(1,1))
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            self.STATE = "game"
 
          
      pygame.display.flip()
    while self.STATE == "game":


      self.screen.blit(self.bg,(0,0))      
      for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if key[pygame.K_0]:
          self.STATE == 'end' 
          pygame.quit()
          SystemExit()
            
        
        elif key[pygame.K_d]:
          self.ply.move_right()

        elif key[pygame.K_a]:
            self.ply.move_left()
        elif key[pygame.K_f]:
          self.ply.attack()
          Bearcat.rect.collidepoint() == False
          hitb = pygame.Rect.collidepoint()
          if hitb == True:
            Bearcat.hit()
        elif key[pygame.K_w]:
            self.ply.jump()
      for sprite in self.sprites:
        if Bearcat.check == True:
          self.ply.hit()
        if River.check == True:
          self.ply.slow(True)
        else:
          self.ply.slow(False)

        self.sprites.draw(self.screen)
      self.bear.move_left()
      pygame.display.update()

      
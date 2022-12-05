import pygame
import pickle
from src.player import Player
from src.river import River
from src.ground import Ground
from src.level_builder import LevelBuilder
from src.harvey import Harvey
from src.next import Next


class Controller:
  def __init__(self):
    pygame.init()
    print(type(LevelBuilder.Level_2(self)))
    print(type(LevelBuilder.NextLevel(self)))
    
    self.res_x = 975
    self.res_y = 500
    self.screen = pygame.display.set_mode((self.res_x,self.res_y))
    self.bg = pygame.image.load("assets/background.jpg")
    self.bg2 = pygame.image.load("assets/bg1.png")
    self.bg3 = pygame.image.load("assets/bg2.png")
    self.bg4 = pygame.image.load("assets/bg3.png")
    
    self.harvey = pygame.image.load("assets/interaction.png")
    self.river = River()

    self.next_ = pygame.sprite.Group()
    self.levelbuilder = LevelBuilder()

    self.ground = pygame.sprite.Group(Ground(self.res_x,self.res_y))

    self.origin = (0,0)
    self.harv = Harvey()
    self.sprites = pygame.sprite.Group()
    self.player_group = pygame.sprite.Group()
 
    self.level2_bears = LevelBuilder.Level2Bear(self)
    self.level3_bears = LevelBuilder.Level3Bear(self)
    self.level = 1
    self.level = pickle.load(open("level.dat",'rb'))
    if self.level == 1:
      self.next_obj = Next(600,400)
      self.next_.add(self.next_obj)
    if self.level == 2:
      self.next_obj = Next(760,130) 
      self.level_ = LevelBuilder.Level_2(self)
      self.bears = self.level2_bears
      self.next_.add(self.next_obj)
    if self.level == 3:
      self.level_ = LevelBuilder.Level_3(self)
      self.next_obj = Next(760,220) 
      self.bears = self.level3_bears
      self.next_.add(self.next_obj)
    if self.level == 4:
      self.level_ = LevelBuilder.Level_4(self)
      self.next_obj = Next(460,5)
      self.next_.add(self.next_obj)
    if self.level == 5:
      self.level_ = pygame.sprite.Group()
      self.next_ = pygame.sprite.Group()
      self.bears = pygame.sprite.Group()
      
      
    self.screen_x = self.screen.get_width
    self.font = pygame.font.Font('freesansbold.ttf', 32)
    self.message = self.font.render("press space to talk",True,"blue")
    self.message_pos = 300,80
    self.saved_mes = self.font.render("saved",True,"blue")
    self.clear_mes = self.font.render("save cleared",True,"red")
    self.STATE = "start"
  def mainloop(self):

    

    while True:
      while self.STATE == "start":
        self.start = pygame.image.load("assets/Start.png")
        self.screen.blit(self.start,(1,1))
        pygame.display.update()
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
              self.STATE = "menu"
      while self.STATE == "menu":
  
        self.button = pygame.image.load("assets/new_menu.png")
        self.screen.blit(self.button,self.origin)
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
              self.ply = Player("cs")
              self.player_group.add(self.ply)
              self.STATE = "game"            
            if event.key == pygame.K_b:
              self.ply = Player("business")
               
              self.player_group.add(self.ply)
              self.STATE = "game"
            if event.key == pygame.K_LCTRL and pygame.K_c:
              self.level = 1
              pickle.dump(1,open("level.dat",'wb'))
              self.next_.remove(self.next_obj)
              self.next_obj = Next(600,400)
              self.next_.add(self.next_obj)
              self.screen.blit(self.clear_mes,self.origin)
              pygame.display.update()
              pygame.time.wait(1000)
        pygame.display.flip()
      while self.STATE == "game":
        if self.level == 1:
          self.level_ = LevelBuilder.NextLevel(self)
          self.bears = pygame.sprite.Group()
          self.screen.blit(self.bg,self.origin)
        if self.level == 2:
          self.level_ = LevelBuilder.Level_2(self)
          self.bears = self.level2_bears
          
          self.screen.blit(self.bg2,self.origin)
          
        if self.level == 3:
          self.level_ = LevelBuilder.Level_3(self)
          self.bears = self.level3_bears
          
          self.screen.blit(self.bg3,self.origin)
        if self.level == 4:
          self.level_ = LevelBuilder.Level_4(self)
          self.screen.blit(self.bg4,self.origin)
        if self.level == 5:
          self.level_ = pygame.sprite.Group()
          self.next_ = pygame.sprite.Group()
          self.bears = pygame.sprite.Group()
          self.screen.blit(self.bg4,self.origin)
          self.screen.blit(self.harv.image,(600,350)) 
          
       
 
        
        
       
        for event in pygame.event.get():
            
          key = pygame.key.get_pressed()
          if key[pygame.K_0]:
            self.STATE == 'end' 
            pygame.quit()
            SystemExit()
          if key[pygame.K_w]:
            self.ply.jump(self.ground,self.level_)

          key = pygame.key.get_pressed()
          if key[pygame.K_d]:
            self.ply.move_right()
  
          elif key[pygame.K_a]:
            self.ply.move_left()

           
          if key[pygame.K_SPACE] and self.ply.rect.colliderect(self.harv.rect):
              self.screen.blit(self.harvey,self.origin)
              pygame.display.update()
              pygame.time.wait(1000)
              self.STATE == "start"
          if key[pygame.K_LCTRL] and key[pygame.K_s]:
            pickle.dump(self.level,open('level.dat',"wb"))
            self.screen.blit(self.saved_mes,self.origin)
            pygame.display.update()
            pygame.time.wait(1000)
            
        if pygame.sprite.spritecollideany(self.ply,self.next_):
          self.level += 1
          self.next_.remove(self.next_obj)
          if self.level == 2:
            self.level_ = LevelBuilder.Level_2(self)
            self.next_obj = Next(760,130)
            self.next_.add(self.next_obj)
          if self.level == 3:
            self.next_obj = Next(760,220)
            self.level_ = LevelBuilder.Level_3(self)
            self.next_.add(self.next_obj)
          if self.level == 4:
            self.next_obj = Next(470,2)
            self.next_.add(self.next_obj)
            self.level_ = LevelBuilder.Level_4(self)
          self.ply.level_start()     

        if pygame.sprite.spritecollideany(self.ply,self.bears):
          self.ply.health -=1
          self.ply.level_start()
          if self.ply.health == 0:
            self.level = 1
            self.ply.health = 5
            self.next_.remove(self.next_obj)
            self.next_obj = Next(600,400)
            self.next_.add(self.next_obj)
        self.ply.update(self.ground,self.level_) 
        # for bear in self.level2_bears:
        #   bear.move()
        for sprite in self.sprites:
          if self.level== 5:
            if self.ply.rect.colliderect(self.harv.rect):
              self.screen.blit(self.message,self.message_pos)

          if pygame.Rect.colliderect(self.ply.rect, self.river.rect) == True:
            self.ply.slow(True)
          else:
            self.ply.slow(False)
          self.sprites.draw(self.screen)
          
        
        
        

        self.bears.draw(self.screen)
        self.player_group.draw(self.screen)
        self.next_.draw(self.screen)

        self.level_.draw(self.screen)
        self.ground.draw(self.screen)
        pygame.display.update()


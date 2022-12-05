import pygame
from src.box import Branch
from src. bearcat import Bearcat
class LevelBuilder(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()

    self.platforms = []
    self.bears = []
    print("builder init")
    
    


  def NextLevel(self):
    if True:
      self.platforms = []
      print("platform list created")
    self.level_build = pygame.sprite.Group()
    for platform in self.platforms:
      self.level_build.add(Branch(platform[0], platform[1]))

    print("level made")
    return self.level_build
  def Level2Bear(self):
    if True:
      self.bears = [(580, 250, 240)]
      print("bearcat list created")
    self.bear_place2 = pygame.sprite.Group()
    for bear in self.bears:
      self.bear_place2.add(Bearcat(bear[0],bear[1], bear[2]))

    print("bearcats made")
    return self.bear_place2
  def Level3Bear(self):
    if True:
      self.bears = [(300, 450, 240),(450, 450, 240),(600, 450, 240),(690, 450, 240)]
      print("bearcat list created")
    self.bear_place3 = pygame.sprite.Group()
    for bear in self.bears:
      self.bear_place3.add(Bearcat(bear[0],bear[1], bear[2]))
    return self.bear_place3
  def Level4Bear(self):
    if True:
      self.bears = [(350, 450, 240),(450, 450, 240)]
      print("bearcat list created")
    self.bear_place3 = pygame.sprite.Group()
    for bear in self.bears:
      self.bear_place3.add(Bearcat(bear[0],bear[1], bear[2]))    
    print("bearcats made")
    return self.bear_place4  
  def Level_2(self):
    if True:
      self.platforms = [(120,300),(200, 300),(340,250),(420,250),(500,250),(580,250),(740,200)]
      # print("platform list created")
    self.level2_build = pygame.sprite.Group()
    for platform in self.platforms:
      self.level2_build.add(Branch(platform[0], platform[1]))  
    
    
    return self.level2_build
  def Level_3(self):
    if True:
      self.platforms = [(200, 300),(470,250),(740,300)]
      # print("platform list created")
    self.level3_build = pygame.sprite.Group()
    for platform in self.platforms:
      self.level3_build.add(Branch(platform[0], platform[1]))    
    return self.level3_build
  def Level_4(self):
    if True:
      self.platforms = [(400,300),(480,300),(560,300),(640,200),(640,100),(560,50),(480,50)]
      self.level4_build = pygame.sprite.Group()
      for platform in self.platforms:
        self.level4_build.add(Branch(platform[0], platform[1])) 
      return self.level4_build
      
      

  # def update_bearcat():
     # Bearcat.move()
  
    
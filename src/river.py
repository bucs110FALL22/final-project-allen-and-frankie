import pygame

class River(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("assets/river.png")
    self.depth = 5
    self.width = 5
    self.image_scaled = pygame.transform.scale(self.image,(5,5))
    self.rect = self.image_scaled.get_rect()
    self.rect.x = 400
    self.rect.y = 200
    # self.distance_to_bridge = 10
    
  # def damage_player(self):
  #   '''
  #   damages the player when the conditions are too bad, or player is drowing
  #   arguments:none
  #   return:none
  #   '''
  #   self.rect.collidepoint
  #   self.image = pygame.image.load("assets/river_damage.png")

  # def slow_player(self):
  #   '''
  #   slows the player down when colliding with river
  #   arguments:none
  #   return:none
  #   '''
    

  def check(self):
    return self.rect.collidepoint()
  # def increase_depth(self, depth_change):
  #   '''
  #   increases the depth attribute for the river if raining/flooding
  #   arguments:depth_change --- how much the river depth should be changed
  #   return:none
  #   '''
  #   self.depth =+ depth_change

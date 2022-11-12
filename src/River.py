import pygame

class River(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__(self)
    self.image = pygame.image.load("assets/river.png")
    self.depth = 5
    self.width = 5
    self.rect = self.image.get_rect()
    self.distance_to_bridge = 10
    
  def damage_player(self):
    '''
    damages the player when the conditions are too bad, or player is drowing
    arguments:none
    return:none
    '''
    self.rect.collidepoint
    self.image = pygame.image.load("assets/river_damage.png")
    
  def increase_depth(self, depth_change):
    '''
    increases the depth attribute for the river if raining/flooding
    arguments:depth_change --- how much the river depth should be changed
    return:none
    '''
    self.depth =+ depth_change

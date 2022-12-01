import pygame

class Bearcat(pygame.sprite.Sprite):
  def __init__(self):
    '''
    initializes bearcat enemy
    self - instance of bearcat
    '''
    super().__init__()
    self.speed = 1
    self.health = 2
    self.image = pygame.image.load("assets/bearcat.png")
    self.rect = self.image.get_rect()
    self.rect.x = 700
    self.rect.y = 60
  def move_left(self):
    '''
    makes bearcat move left
    '''
    self.rect.x -= self.speed
  def move_right(self):
    '''
    makes bearcat move right
    '''
    self.rect.x += self.speed
  def jump(self):
    '''
    makes bearcat jump
    '''
    jump_time = 10
    jump_speed = 2
    self.rect.y += self.speed/jump_speed
    pygame.time.wait(jump_time)
    self.rect.y += self.speed/jump_speed
  def check(self):
    return self.rect.collidepoint()
  def attack(self):
    '''
    shows bearcat hitting player
    '''
    hitbox = self.rect.collidepoint
    if hitbox == True:
      self.image = pygame.image.load("assets/bearcat_attack.png")
  def hit(self):
    '''
    shows bearcat getting hit
    '''
    # self.rect.collidepoint
    self.image.load("assets/bearcat_hit.png")
    self.health -= 1
  # def update(self):
    
import pygame

class Bearcat(pygame.sprite.Sprite):
  def __init__(self,x,y, distance):
    '''
    initializes bearcat enemy
    self - instance of bearcat
    '''
    super().__init__()
    self.speed = 1
    self.health = 2
    self.image = pygame.image.load("assets/newbearcat.png")
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = (y-60)
    self.startingx = x
    self.distance = distance
    
    
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
    self.image.load("assets/bearcat_hit.png")
    self.health -= 1
  # def update(self):

  def move(self):
    # print("updating bear")
    '''
    makes the bearcat move on its own
    '''
    while True:
      if self.rect.x < (self.startingx - self.distance):
        direction = 0
      else:
        direction = 1
      if direction == 1:
        self.move_right()
      else:
        self.move_left()
  
    
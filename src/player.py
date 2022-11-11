import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self,major):
    '''
    initializes player object
    self - instance of player
    major - major of player (affects stats)
    '''
    super().__init__(self)
    if major == "cs":
      self.move_effect = .8
      self.health_effect = 1
    if major == "bio"
      self.move_effect = 1
      self.health_effect = 2    
    self.speed = 20*self.move_effect
    self.health = 5*self.health_effect
    self.image = pygame.image.load("assets/student.png")
    self.rect = self.image.get_rect()
  def move_left(self):
    '''
    makes player move left
    
    '''
    self.rect.x += self.speed
  def jump(self):
    '''
    makes player jump
    '''
    jump_time = 10
    jump_speed = 2
    self.rect.y += self.speed/jump_speed
    pygame.time.wait(jump_time)
    self.rect.x += self.speed/jump_speed
  def attack(self):
    '''
    makes player attack
    '''
    self.image = pygame.image.load("assets/student_attack.png")
    self.rect.collidepoint

  def hit(self):
    '''
    shows player getting hit
    '''
    # self.rect.collidepoint
    self.image.load("assets/student_hit.png")
    self.health -= 1
import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self,major):
    '''
    initializes player object
    self - instance of player
    major - major of player (affects stats)
    '''
    super().__init__()
    if major == "cs":
      self.move_effect = .8
      self.health_effect = 1
    if major == "bio":
      self.move_effect = 1
      self.health_effect = 2    
    self.speed = 12*self.move_effect
    self.health = 5*self.health_effect
    self.image = pygame.image.load("assets/player.png")
    self.image_1 = pygame.transform.scale(self.image,(100,100))
    self.rect = self.image_1.get_rect()
    self.rect.x = 10
    self.rect.y = 60
  def move_right(self):
    '''
    makes player move right
    
    '''
    
    self.image = pygame.image.load("assets/player_walk.png")  
    
    self.rect.x += self.speed

  def move_left(self):
    '''
    makes player move left
    
    '''
    
    self.image = pygame.image.load("assets/player_walk.png")  
    
    self.rect.x -= self.speed

        
  def jump(self):
    '''
    makes player jump
    '''
    jump_time = 10
    jump_speed = 2
    self.rect.y += self.speed/jump_speed
    pygame.time.wait(jump_time)
    self.rect.y += self.speed/jump_speed
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
   
    self.image.load("assets/student_hit.png")
    self.health -= 1

  def slow(self, set):
  #   '''
  #   slows the player down when colliding with river
  #   arguments:none
  #   return:none
  #   '''
    if set == True:
      self.move_effect = 0.1
    else:
      self.move_effect = 0.8
    
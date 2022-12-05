import pygame
# import numpy
# from src.bearcat import Bearcat
class Player(pygame.sprite.Sprite):
  def __init__(self,major):
    '''
    initializes player object
    self - instance of player
    major - major of player (affects stats)
    '''
    super().__init__()
    if major == "cs":
      self.move_effect = .2
      self.health_effect = .2
    if major == "business":
      self.move_effect = 1
      self.health_effect = 2    
    self.speed = 36*self.move_effect
    self.health = 5*self.health_effect
    self.image = pygame.image.load("assets/student.png")
    self.vertical_speed = 0    
    self.jump_speed = 14
    self.gravity = .5
    self.image_1 = pygame.transform.scale(self.image,(100,100))
    self.rect = self.image_1.get_rect()
    self.start_x = 10
    self.rect.x = self.start_x
    self.start_y = 360
    self.rect.y = self.start_y
    self.invincible = False
  def move_right(self):
    '''
    makes player move right
    
    '''
    
    self.image = pygame.image.load("assets/student.png")  
    
    self.rect.move_ip(self.speed,0)

  def move_left(self):
    '''
    makes player move left
    
    '''
    
    self.image = pygame.image.load("assets/student.png")  
    
    self.rect.move_ip(-self.speed,0)

        
  def jump(self,sprite1,sprite2):
    '''
    makes player jump
    arg1: sprite class intended to be the ground object
    arg2: sprite class intended to be platform object
    '''
    ground_check = self.check_collision(0,1,sprite1)
    plat_check = self.check_collision(0,1,sprite2)

    if plat_check or ground_check:
      self.vertical_speed = -self.jump_speed
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
    '''
    slows the player down when colliding with river
    arguments:none
    return:none
    '''
    if set == True:
      self.move_effect = 0.1
      
    else:
      self.move_effect = 0.8
  def update(self,sprite1,sprite2):
    
    '''
    checks player position to update y value
    args:
    sprite1 = ground sprite
    sprite2 = platform sprite
    '''
    ground_check = self.check_collision(0,1,sprite1)
    plat_check = self.check_collision(0,1,sprite2)
    
        
            

    

     
    if self.vertical_speed < 10:
      self.vertical_speed += self.gravity
    if self.vertical_speed > 0 and ground_check:
      self.vertical_speed = 0
    if self.vertical_speed > 0 and plat_check:
      self.vertical_speed = 0      

         
          
        # elif key[pygame.K_f]:
        #   self.ply.attack()
        #   # Bearcat.rect.collidepoint() == False
        #   hitb = pygame.Rect.collidepoint()
        #   if hitb == True:
        #     Bearcat.hit()
    self.move(self.vertical_speed)
  def check_collision(self, x, y, sprite):
      '''
      checks player collision in certain area
      args:
      x - x coordinate moved
      y - y coordinate moved
      sprite - sprite collision checked
      '''
      self.rect.move_ip([x, y])
      collide = pygame.sprite.spritecollideany(self, sprite)
      self.rect.move_ip([-x, -y])
      return collide
  def move(self,y):
    '''
    moves player the appropriate y value
    arg: y = intended y value moved
    '''
    
    dy = y
    



    self.rect.move_ip([0, dy])
      
  def level_start(self):
    '''
    brings player to start of level
    '''
    self.rect.x = self.start_x
    self.rect.y = self.start_y
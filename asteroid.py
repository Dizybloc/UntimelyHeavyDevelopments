import pygame, random


class asteroid(pygame.sprite.Sprite):
  def __init__(self, pos):
    super().__init__()
    self.image = pygame.image.load('asteroid (1).png')
    self.image = pygame.transform.smoothscale(self.image, (random.randint(20, 100), random.randint(20, 100)))
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.speed = pygame.math.Vector2(0,3)
    rotation = random.randint(0, 360)
    self.speed.rotate_ip(rotation)
  
  def update(self):
    screen_info = pygame.display.Info()
    self.rect.move_ip(self.speed)
    if self.rect.left < 0 or self.rect.right > screen_info.current_w:
      self.speed[0] += -1
    if self.rect.left < 0 or self.rect.right > screen_info.current_w:
      self.speed[0] += -1  
    if self.rect.left < 0 or self.rect.right > screen_info.current_w:
      self.speed[0] += -1
    if self.rect.left < 0 or self.rect.right > screen_info.current_w:
      self.speed[0] += -1
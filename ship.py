import pygame


class Ship(pygame.sprite.Sprite):
  def __init__(self, pos):
    super().__init__()
    self.image = pygame.image.load('ship.png')
    self.image = pygame.transform.smoothscale(self.image,(40, 40))
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.image = pygame.transform.rotate(self.image, -90)
    self.speed = pygame.math.Vector2(10,0)

  def update(self):
    self.rect.move_ip(self.speed)

  def reset(self, pos):
    self.rect.center = pos

  def checkReset(self, endPos):
    if self.rect.center[0] >= endPos:
      return True
    else:
      return False
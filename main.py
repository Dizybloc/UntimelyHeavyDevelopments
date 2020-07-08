import pygame
from pygame.locals import *
from ship import *

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (30, 0, 30)
screen.fill(color)

NumLevels = 4
level = 1
AsteroidCount = 3
Player = Ship((20, 300))




def main():
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          Player.speed[0] = 10
        if event.key == pygame.K_LEFT:
          Player.speed[0] = -10
        if event.key == pygame.K_UP:
          Player.speed[1] = -10
        if event.key == pygame.K_DOWN:
          Player.speed[1] = 10
      else:
        Player.speed[0] = 0
        Player.speed[1] = 0
            
    screen.fill(color)
    screen.blit(Player.image, Player.rect)
    Player.update()
    pygame.display.flip()
    


if __name__ == "__main__":
  main()
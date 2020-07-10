import pygame, pandas as pd
from pygame.locals import *
from ship import *
from asteroid import *

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (30, 0, 30)
screen.fill(color)

df = pd.read_csv('game_info.csv')
NumLevels = df['levelNum'].max()
level = df['levelNum'].min()


AsteroidCount = levelData['AsteroidCount'].min()
Player = Ship(({'PlayerX'}, levalData, {'PlayerY'}))
Asteroids = pygame.sprite.Group()



def init():
  global AsteroidCount, level, levalData
  levelData = df.iloc[level]
  Player.reset((["PlayerX"], ["PlayerY"]))
  level = df ['levelNum'].min()
  level += 1
  AsteroidCount += 3
  for i in range(AsteroidCount):
    Asteroids.add(asteroid((random.randint(0, 800), random.randint(0, 600))))

def win():
  font = pygame.font.SysFont(None, 70)
  text = font.render("WINNER WINNER SPACE CHINKEN DINNER", True, (255, 0, 0))
  text_rect = text.get_rect()
  text_center = (screen_info.current_w //2, screen_info.current_h)
  while True:
    screen.fill(color)
    screen.blit(text, text_rect)
    pygame.display.flip()



def main():
  global level
  init()
  size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
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
    Asteroids.draw(screen)
    Asteroids.update()
    gets_hit = pygame.sprite.spritecollide(Player, Asteroids, False)     
    screen.fill(color)
    screen.blit(Player.image, Player.rect)
    Player.update()
    pygame.display.flip()
    
    if Player.checkReset(screen.info.current_w()):
      if level == NumLevels:
        break()
    
      else:
      
    elif gets_hit:
      player.reset((20, 300))

win()

if __name__ == "__main__":
  main()
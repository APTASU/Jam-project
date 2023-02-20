import pygame, math, random
from enemies import Enemies
from levels import Levels
scoreFile = open('score.txt', 'r')

# Initialize game engine

image_dict = {'main character':pygame.image.load('jam man.png'),
              'still':pygame.image.load('still enemy.png'),
              'walk':pygame.image.load('walk enemy.png'),
              'run':pygame.image.load('run enemy.png'),
              'jump':pygame.image.load('jump enemy.png'),
              'fly':pygame.image.load('slow fly enemy.png'),
              'fast fly':pygame.image.load('fast fly enemy.png'),
              'speratic':pygame.image.load('speratic enemy.png'),
              'jump boss':pygame.image.load('jump boss.png'),
              'fly boss':pygame.image.load('fly boss.png'),
              'big boss':pygame.image.load('final boss.png'),
              'plat left':pygame.image.load('left end platform.png'),
              'plat right':pygame.image.load('right end platform.png'),
              'plat alone':pygame.image.load('alone platform.png'),
              'plat central':pygame.image.load('central platform.png'),
              'wall alone':pygame.image.load('lone wall.png'),
              'wall central':pygame.image.load('center wall.png'),
              'wall horrizontal':pygame.image.load('horizontal wall.png'),
              'wall vertical':pygame.image.load('vertical wall.png'),
              'wall left':pygame.image.load('left pair wall.png'),
              'wall right':pygame.image.load('right pair wall.png'),
              'wall top':pygame.image.load('top pair wall.png'),
              'wall bottom':pygame.image.load('bottom pair wall.png'),
              'wall left T':pygame.image.load('left T wall.png'),
              'wall right T':pygame.image.load('right T wall.png'),
              'wall up T':pygame.image.load('top T wall.png'),
              'wall bottom T':pygame.image.load('bottom T wall.png'),
              'wall UR':pygame.image.load('right up corner.png'),
              'wall DR':pygame.image.load('right down corner.png'),
              'wall UL':pygame.image.load('left up corner.png'),
              'wall DL':pygame.image.load('left down corner.png'),
              'bullet':pygame.image.load('han (1).png'),
              'gun':pygame.image.load('jam gun.png'),}
run = True

while run:
  score =Levels.levels(image_dict)
  wait = True
  pygame.init()
  width, height = 640, 480
  screen = pygame.display.set_mode((width, height))
  font = pygame.font.Font('freesansbold.ttf',50)
  font2 = pygame.font.Font('freesansbold.ttf',30)
  text = font.render('YOU DIED',True,(255,255,255),(0,0,0))
  textRect = text.get_rect()
  textRect.center = (width//2,height//2-60)
  text2 = font.render('try again',True,(255,255,255))
  textRect2 = text2.get_rect()
  textRect2.center = (width//2-140,height//2+75)
  text3 = font.render('give up',True,(255,255,255))
  textRect3 = text3.get_rect()
  textRect3.center = (width//2+130,height//2+75)
  
  for line in scoreFile:
      text4 = font2.render('High Score:'+line,True,(255,255,255))
  textRect4 = text4.get_rect()
  textRect4.left = 20
  textRect4.top = 20
  text5 = font2.render('Current Score:' + str(score),True,(255,255,255))
  textRect5 = text5.get_rect()
  textRect5.left = 20
  textRect5.top = 60
  while wait:
      screen.fill((128,128,128))
      screen.blit(text,textRect)
      screen.blit(text2,textRect2)
      screen.blit(text3,textRect3)
      screen.blit(text4,textRect4)
      screen.blit(text5,textRect5)
      mouse_x, mouse_y = pygame.mouse.get_pos()
      for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if textRect2.right > mouse_x > textRect2.left:
                if textRect2.top < mouse_y < textRect2.bottom:
                    wait = False
            if textRect3.right > mouse_x > textRect3.left:
                if textRect3.top < mouse_y < textRect3.bottom:
                    wait = False
                    run = False
      
      pygame.display.update()
      
    
# Clean up
pygame.quit()
import pygame, math, random
from enemies import Enemies

              
class Levels:
  
              
              
  def levels(image_dict):
    pygame.init()
    score = 0
    levelFile = open('levels.txt', 'r')
    scoreFile = open('score.txt', 'r')
    
  
    # Set up window
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    
    # Set up game objects
    clock = pygame.time.Clock()
    clockCount = 0
    fps = 165
    
    
    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render('Score:0:',True,(255,255,255))
    textRect = text.get_rect()
    textRect.center = (width//2-260,height//2-215)
    
    square = pygame.Rect(0, 100, 32, 32)
    main_character = pygame.transform.scale(image_dict['main character'],(34,34))
    falling = True
    platforms = []
    platform_color = (128, 128, 128)
    platformXpos = 0
    platformYpos = 0
    found_platform = False
    
    enemies = []
    spawners = []
    
    for line in levelFile:
        for character in line:
            if character == '$':
                img = pygame.transform.scale(image_dict['wall central'],(32,32))
                platform = pygame.Rect(platformXpos, platformYpos, 32, 32)
                platforms.append([platform,'w',img])
                platformXpos = platformXpos + 32
            if character == '-':
                img = pygame.transform.scale(image_dict['plat central'],(32,16))
                platform = pygame.Rect(platformXpos, platformYpos, 32, 16)
                platforms.append([platform,'p',img])
                platformXpos = platformXpos + 32
            if character == ' ':
                platformXpos = platformXpos + 32
            if character == '@':
                platformXpos = platformXpos + 32
                square = pygame.Rect(platformXpos, platformYpos, 30, 30)
            if character == '0':
                still = pygame.transform.scale(image_dict['still'],(32,32))
                enemy = pygame.Rect(platformXpos,platformYpos, 32,32,)
                enemies.append([enemy,0,0,False,still,1])
                platformXpos = platformXpos + 32
            if character == '1':
                walk = pygame.transform.scale(image_dict['walk'],(32,32))
                enemy = pygame.Rect(platformXpos,platformYpos, 32,32)
                enemies.append([enemy,1,0,False,walk,2])
                platformXpos = platformXpos + 32
            if character == '2':
                run = pygame.transform.scale(image_dict['run'],(60,20))
                enemy = pygame.Rect(platformXpos,platformYpos, 60,20)
                enemies.append([enemy,2,0,False,run,1])
                platformXpos = platformXpos + 32
            if character == '3':
                jump = pygame.transform.scale(image_dict['jump'],(32,32))
                enemy = pygame.Rect(platformXpos,platformYpos, 32,32)
                enemies.append([enemy,3,0,False,jump])
                platformXpos = platformXpos + 32
            if character == '4':
                fly = pygame.transform.scale(image_dict['fly'],(32,32))
                enemy = pygame.Rect(platformXpos,platformYpos, 32,32)
                enemies.append([enemy,4,0,False,fly])
                platformXpos = platformXpos + 32
            if character == '5':
                ffly = pygame.transform.scale(image_dict['fast fly'],(32,32))
                enemy = pygame.Rect(platformXpos,platformYpos, 32,32)
                enemies.append([enemy,5,0,False,ffly])
                platformXpos = platformXpos + 32
            if character == '6':
                speratic = pygame.transform.scale(image_dict['speratic'],(32,32))
                enemy = pygame.Rect(platformXpos,platformYpos, 32,32)
                enemies.append([enemy,6,0,False,speratic])
                platformXpos = platformXpos + 32
            if character == '7':
                jumpb = pygame.transform.scale(image_dict['jump boss'],(64,64))
                enemy = pygame.Rect(platformXpos,platformYpos, 64,64,20)
                enemies.append([enemy,7,0,False,jumpb])
                platformXpos = platformXpos + 32
            if character == '8':
                flyb = pygame.transform.scale(image_dict['fly boss'],(64,64))
                enemy = pygame.Rect(platformXpos,platformYpos, 64,64,20)
                enemies.append([enemy,8,0,False,flyb])
                platformXpos = platformXpos + 32
            if character == '9':
                final = pygame.transform.scale(image_dict['big boss'],(128,128))
                enemy = pygame.Rect(platformXpos,platformYpos, 128,128,100)
                enemies.append([enemy,0,0,False,final])
                platformXpos = platformXpos + 32
            if character == 'p':
                still = pygame.transform.scale(image_dict['still'],(32,32))
                wait = fps * 5
                spawner = [platformXpos,platformYpos,32,32,wait,0,1,still,1]
                spawners.append(spawner)
                platformXpos = platformXpos + 32
            if character == 'l':
                walk = pygame.transform.scale(image_dict['walk'],(32,32))
                wait = fps * 5
                spawner = [platformXpos,platformYpos,32,32,wait,1,1,walk,2]
                spawners.append(spawner)
                platformXpos = platformXpos + 32
            if character == 'm':
                run = pygame.transform.scale(image_dict['run'],(60,20))
                wait = fps * 5
                spawner = [platformXpos,platformYpos,60,20,wait,2,1,run,1]
                spawners.append(spawner)
                platformXpos = platformXpos + 32
            if character == '!':
                jump = pygame.transform.scale(image_dict['jump'],(32,32))
                wait = fps * 10
                spawner = [platformXpos,platformYpos,32,32,wait,3,1,jump,1]
                spawners.append(spawner)
                platformXpos = platformXpos + 32
            if character == 'g':
                fly = pygame.transform.scale(image_dict['fly'],(32,32))
                wait = fps * 5
                spawner = [platformXpos,platformYpos,32,32,wait,4,1,fly,3]
                spawners.append(spawner)
                platformXpos = platformXpos + 32
            if character == '?':
                ffly = pygame.transform.scale(image_dict['fast fly'],(32,32))
                wait = fps * 10
                spawner = [platformXpos,platformYpos,32,32,wait,5,1,ffly,2]
                spawners.append(spawner)
                platformXpos = platformXpos + 32
                platformXpos = platformXpos + 32
            if character == '.':
                speratic = pygame.transform.scale(image_dict['speratic'],(32,32))
                wait = fps * 20
                spawner = [platformXpos,platformYpos,32,32,wait,6,1,speratic,1]
                spawners.append(spawner)
                platformXpos = platformXpos + 32
            if character == '[':
                jumpb= pygame.transform.scale(image_dict['jump boss'],(64,64))
                wait = fps * 40
                spawner = [platformXpos,platformYpos,64,64,wait,7,1,jumpb,20]
                spawners.append(spawner)
                platformXpos = platformXpos + 32
            if character == ']':
                flyb= pygame.transform.scale(image_dict['fly boss'],(64,64))
                wait = fps * 40
                spawner = [platformXpos,platformYpos,64,64,wait,8,1,flyb,20]
                spawners.append(spawner)
                platformXpos = platformXpos + 32
            if character == 't':
                jump = pygame.transform.scale(image_dict['jump'],(32,32))
                wait = fps * 5
                spawner = [platformXpos,platformYpos,32,32,wait,9,1,jump,100]
                spawners.append(spawner)
                platformXpos = platformXpos + 32
        platformYpos = platformYpos + 32
        platformXpos = 0
    
    
    enemy_color = (255, 0, 0)
    
    
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    angle = math.atan2(mouse_y - square.centery, mouse_x - square.centerx)
    gun_color = (255, 0, 0)
    gun_width = 3
    
    #add enemy ai
    
    
    bullets = []
    bullet_speed = 8
    bullets_allowed = 3
    
    #test vars
    okCount = 0
    z=0
    
    #player info
    player_speed = 4
    gravity = 0.1
    falling_speed = 0
     
    jump_height = 5
    jump_state = False
    
    running = True
    while running:
        for line in scoreFile:
          
          if int(line) < score:
            scoreFile = open('score.txt', 'w')
            scoreFile.write(str(score))
        scoreFile = open('score.txt','r')
       
        text = font.render('Score:'+str(score),True,(255,255,255))
        v = square.y
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                angle = math.atan2(mouse_y - square.centery, mouse_x - square.centerx)
                bullet = {'start': square.center, 'angle': angle, 'color': (255, 255, 0)}
                bullets.append(bullet)
        
        # Update game state
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            square.x -= player_speed
        if keys[pygame.K_RIGHT]or keys[pygame.K_d]:
            square.x += player_speed
        if (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE])and not jump_state:
          for platform in platforms:
                if square.bottom >= platform[0].top and not falling:
                    jump_state = True
                    break
    
        
        for spawner in spawners:
            if square.x + 700 > spawner[0] > square.x - 700 and square.y + 700 > spawner[1] > square.y - 700:
                if spawner[4] < spawner[6]:
                    enemy = pygame.Rect(spawner[0],spawner[1],spawner[2],spawner[3])
                    enemies.append([enemy,spawner[5],0,False,spawner[7]])
                    spawner[6] = 1
            
                else:
                    spawner[6] += 1
        
        if jump_state:
            square.y -= jump_height
                    
        #Handle enemy movement
        for enemy in enemies:
            if square.x + 500 > enemy[0].x > square.x - 500 and square.y + 500 > enemy[0].y > square.y - 500:
                enemy[3] = False
                for platform in platforms:
                    enemy_ground = Enemies(enemy[0],None,None,None,enemy[2],platform[0],None,platform[1])
                    y = enemy_ground.groundedEnemy()
                    enemy[2] = y[0]
                    enemy[0] = y[2]
                    if y[1]:
                      enemy[3] = y[1]
                        
                enemy_move = Enemies(enemy[0], square,enemy[1], gravity, enemy[2],None,enemy[3],None)
                x = enemy_move.enemyType()
                enemy[0].x = x[0]
                enemy[0].y = x[1]
                enemy[2] = x[2]  
    
        #if enemy is hit by bullet
        for enemy in enemies:
            for bullet in bullets:
                if enemy[0].left <= bullet['start'][0] <= enemy[0].right:
                    if enemy[0].top <= bullet['start'][1] <= enemy[0].bottom:
                        enemies.remove(enemy)
                        bullets.remove(bullet)
                        score += 100
        
        for enemy in enemies:
            if enemy[0].left <= square.right and square.left <= enemy[0].right:
                if enemy[0].top <= square.bottom and square.top <= enemy[0].bottom:   
                    running = False
                    return score
          
        
        
          
    
        if falling:
            falling_speed += gravity
        square.y += falling_speed
    
        
        falling = True
        v -= square.y
        for platform in platforms:
            if platform[0].left <= square.right and square.left <= platform[0].right:
                if platform[0].top <= square.bottom and square.top <= platform[0].bottom:
                    if platform[1] == 'p':
                        if square.bottom >= platform[0].top and square.centery <= platform[0].top:
                            if v <= 0:
                                falling_speed = 0
                                jump_state = False
                                falling = False
                                square.bottom = platform[0].top
                                break
                    if platform[1] == 'w':
                        if square.bottom <= platform[0].centery and square.centery <= platform[0].top:
                          if square.left <= platform[0].right -5 and square.right >= platform[0].left+5:
                            falling_speed = 0
                            jump_state = False
                            falling = False
                            square.bottom = platform[0].top
                            
                        elif square.top > platform[0].centery and square.centery >= platform[0].bottom:
                          if square.left <= platform[0].right -5 and square.right >= platform[0].left+5:
                            falling_speed = 0.1
                            jump_state = False
                            square.top = platform[0].bottom +1
                        elif square.left <= platform[0].x:
                            square.right = platform[0].left -2
                            
                        elif square.right >= platform[0].x:
                            square.left = platform[0].right + 2
                           
    
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - square.centery, mouse_x - square.centerx)
    
        # Set gun position
        gun_end = (square.centerx + 20 * math.cos(angle), square.centery + 20 * math.sin(angle))
    
        # Draw game objects
        screen.fill((135, 206, 235))
    
        for platform in platforms:
            if square.x + 500 > platform[0].x > square.x - 500 and square.y + 500 > platform[0].y > square.y - 500:
                screen.blit(platform[2],platform[0].topleft)
    
        for enemy in enemies:
            if square.x + 500 > enemy[0].x > square.x - 500 and square.y + 500 > enemy[0].y > square.y - 500:
                screen.blit(enemy[4],enemy[0].topleft)
                
        
        screen.blit(text,textRect)
        screen.blit(main_character,square.topleft)
        
        pygame.draw.line(screen, (255, 0, 0), (square.centerx, square.centery), (gun_end), gun_width)
    
        screen_offset_x = width/2 - square.centerx
        screen_offset_y = height/2 - square.centery
    
        # update the platform and rectangle position
        for platform in platforms:
            platform[0].x += screen_offset_x
            platform[0].y += screen_offset_y
        square.x += screen_offset_x
        square.y += screen_offset_y
        for enemy in enemies:
          enemy[0].x += screen_offset_x
          enemy[0].y += screen_offset_y
        for spawner in spawners:
            spawner[0] += screen_offset_x
            spawner[1] += screen_offset_y
    
        if len(bullets) > bullets_allowed:
            del bullets[0]
        for bullet in bullets:
            if not square.x-500 <= bullet['start'][0] <= square.x +500 or not square.y - 500 <= bullet['start'][1] <= square.y +500:
                del bullets[0]
    
        for bullet in bullets:
            bullet_x = bullet['start'][0] + bullet_speed * math.cos(bullet['angle']) + screen_offset_x
            bullet_y = bullet['start'][1] + bullet_speed * math.sin(bullet['angle']) + screen_offset_y
            bullet_end = (bullet_x, bullet_y)
            pygame.draw.circle(screen, bullet['color'], (int(bullet_x), int(bullet_y)), 2, 3)
            bullet['start'] = bullet_end
    
        pygame.display.update()
        
        # Control frame rate
        clock.tick(fps)
    pygame.quit()
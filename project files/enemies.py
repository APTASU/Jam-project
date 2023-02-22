import pygame, math, random
class Enemies:
    def __init__(self,enemy, player, enemy_type, gravity, enemy_v,platform,grounded,platform_type):
        self.enemy = enemy
        self.player = player
        self.enemy_type = enemy_type
        self.gravity = gravity
        self.enemy_v = enemy_v
        self.platform = platform
        self.grounded = grounded
        self.plat_type =platform_type
    
    #call each movement type
    
    def enemyType(self):
        if self.enemy_type == 0:
            return self.stillEnemy()
        elif self.enemy_type == 1:
            return self.walkEnemy()
        elif self.enemy_type == 2:
            return self.runEnemy()
        elif self.enemy_type == 3:
            return self.jumpingEnemy()
        elif self.enemy_type == 4:
            return self.slowFlyEnemy()
        elif self.enemy_type == 5:
            return self.fastFlyEnemy()
        elif self.enemy_type == 6:
            return self.speraticEnemy()
        elif self.enemy_type == 7:
            return self.bossEnemy()
        elif self.enemy_type == 8:
            return self.boss2Enemy()
        elif self.enemy_type == 9:
            return self.boss3Enemy()
        
    
    #find if the enemy is touching a platform
    
    def groundedEnemy(self):
        if self.plat_type == 'p':
            if self.enemy.bottom >= self.platform.top and self.platform.topleft <= self.enemy.bottomright and self.enemy.bottomleft <= self.platform.topright and self.enemy.centery<=self.platform.top:
                self.grounded = True
                self.enemy_v = 0
                self.enemy.bottom = self.platform.top
                return [self.enemy_v, self.grounded,self.enemy]
            else:
                self.grounded = False
                return [self.enemy_v, self.grounded,self.enemy]
        if self.plat_type == 'w':
          if self.platform.left <= self.enemy.right and self.enemy.left <= self.platform.right:
                if self.platform.top <= self.enemy.bottom and self.enemy.top <= self.platform.bottom:
                    if self.enemy.bottom >= self.platform.top  and self.enemy.centery<=self.platform.top:
                      if self.enemy.left <= self.platform.right-3  and self.enemy.right >= self.platform.left+3:
                        self.enemy_v = 0
                        self.grounded = True
                        self.enemy.bottom = self.platform.top
                    elif self.enemy.top < self.platform.bottom and self.platform.centery <=self.enemy.top: 
                      if self.enemy.left <= self.platform.right-3  and self.enemy.right >= self.platform.left+3:
                        self.enemy.top = self.platform.bottom +1
                        self.enemy_v = 0
                    elif self.enemy.left < self.platform.right and self.enemy.centerx >= self.platform.left:
                      if self.enemy.top <= self.platform.bottom-3  and self.enemy.bottom >= self.platform.top+3:
                        self.enemy.left = self.platform.right+2
                    elif self.enemy.right > self.platform.left and self.enemy.centerx <= self.platform.right:
                      if self.enemy.top <= self.platform.bottom-3  and self.enemy.bottom >= self.platform.top+3:
                        self.enemy.right = self.platform.left-2
                    
                
        return[self.enemy_v, self.grounded,self.enemy]
        
    
    
    
    
    #move the enemy to a position
            
    def stillEnemy(self):
        self.enemy_v += self.gravity
        self.enemy.y += self.enemy_v
        return [self.enemy.x,self.enemy.y,self.enemy_v]
    
    def walkEnemy(self):
        random_modifier = random.randint(0,1)
        if self.player.x > self.enemy.x:
            self.enemy.x += random_modifier + 1
        elif self.player.x < self.enemy.x:
            self.enemy.x -= random_modifier + 1
        self.enemy_v += self.gravity
        self.enemy.y += self.enemy_v
        return [self.enemy.x ,self.enemy.y, self.enemy_v]
        
    def runEnemy(self):
        random_modifier = random.randint(0,1)
        if self.player.x > self.enemy.x:
            self.enemy.x += 3
        elif self.player.x < self.enemy.x:
            self.enemy.x -= 3
        self.enemy_v += self.gravity
        self.enemy.y += self.enemy_v
        return [self.enemy.x ,self.enemy.y,self.enemy_v]
    
    def jumpingEnemy(self):
        random_modifier = random.randint(0,1)
        jump_power = 5
        if self.player.x > self.enemy.x:
            self.enemy.x += random_modifier + 2
        elif self.player.x < self.enemy.x:
            self.enemy.x -= random_modifier + 2
        if self.grounded == True:
            self.enemy_v -= jump_power
        self.enemy_v += self.gravity
        self.enemy.y += self.enemy_v
        return [self.enemy.x ,self.enemy.y,self.enemy_v]
        
    def slowFlyEnemy(self):
        angle = math.atan2(self.player.centery - self.enemy.centery  , self.player.centerx - self.enemy.centerx )
        random_modifier = random.randint(0,1)
        if self.player.x > self.enemy.x:
            self.enemy.x += random_modifier + 1.5 * math.cos(angle)
        if self.player.x < self.enemy.x:
            self.enemy.x += random_modifier + 1.5 * math.cos(angle) 
        if self.player.y > self.enemy.y:
            self.enemy.y += random_modifier + 1.5 * math.sin(angle)
        if self.player.y < self.enemy.y:
            self.enemy.y += random_modifier + 1.5 * math.sin(angle)
        return [self.enemy.x ,self.enemy.y,self.enemy_v]
        
    def fastFlyEnemy(self):
        angle = math.atan2(self.player.centery - self.enemy.centery  , self.player.centerx - self.enemy.centerx )
        random_modifier = random.randint(0,1)
        if self.player.x > self.enemy.x:
            self.enemy.x += random_modifier + 3 * math.cos(angle)
        if self.player.x < self.enemy.x:
            self.enemy.x += random_modifier + 3 * math.cos(angle) 
        if self.player.y > self.enemy.y:
            self.enemy.y += random_modifier + 3 * math.sin(angle)
        if self.player.y < self.enemy.y:
            self.enemy.y += random_modifier + 3 * math.sin(angle)
        return [self.enemy.x ,self.enemy.y,self.enemy_v]
        
    def speraticEnemy(self):
        jump_power = random.randint(0,6)
        if self.player.x > self.enemy.x:
            self.enemy.x += random.randint(-2,6)
        elif self.player.x < self.enemy.x:
            self.enemy.x -= random.randint(-2,6)
        if self.grounded == True:
            self.enemy_v -= jump_power
        self.enemy_v += self.gravity
        self.enemy.y += self.enemy_v
        return [self.enemy.x ,self.enemy.y,self.enemy_v]
        
    def bossEnemy(self):
        random_modifier = random.randint(0,1)
        jump_power = 7
        if self.player.x > self.enemy.x:
            self.enemy.x += random_modifier + 2
        elif self.player.x < self.enemy.x:
            self.enemy.x -= random_modifier + 2
        if self.grounded == True:
            self.enemy_v -= jump_power
        self.enemy_v += self.gravity
        self.enemy.y += self.enemy_v
        return [self.enemy.x ,self.enemy.y,self.enemy_v,]
        
    def boss2Enemy(self):
        random_modifier = random.randint(0,1)
        angle = math.atan2(self.player.centery - self.enemy.centery  , self.player.centerx - self.enemy.centerx )
        if self.player.x > self.enemy.x:
            self.enemy.x += random_modifier + 1.5 * math.cos(angle)
        if self.player.x < self.enemy.x:
            self.enemy.x += random_modifier + 1.5 * math.cos(angle) 
        if self.player.y > self.enemy.y:
            self.enemy.y += random_modifier + 1.5 * math.sin(angle)
        if self.player.y < self.enemy.y:
            self.enemy.y += random_modifier + 1.5 * math.sin(angle)
        return [self.enemy.x ,self.enemy.y,self.enemy_v]
        
    def boss3Enemy(self):
        if self.player.x > self.enemy.x:
            self.enemy.x += 1
        elif self.player.x < self.enemy.x:
            self.enemy.x -= 1
        self.enemy_v += self.gravity
        self.enemy.y += self.enemy_v
        return [self.enemy.x,self.enemy.y,self.enemy_v]
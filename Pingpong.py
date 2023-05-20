import pygame
from random import randint
pygame.mixer.init()
pygame.font.init()
score = 0
score1 = 0
speed = 5
lose = 0
font1 = pygame.font.Font(None, 60)
font2 = pygame.font.Font(None,600)
score_text = font1.render(str(score), True,(250,250,250))
score_text1 = font1.render(str(score1), True,(250,250,250))
win = font1.render("YOU WIN!", True, (250,250,250))
lose = font1.render("YOU LOSE!", True, (250,250,250))
Record = font1.render("Your record is ", True, (250,250,250))
pygame.mixer.music.load('02. DJVI - Back On Track.mp3')
pygame.mixer.music.play()
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
w = 700
h = 500
window = pygame.display.set_mode((w,h))
pygame.display.set_caption('Pingpong')
background  = pygame.transform.scale(pygame.image.load('Brilliant Black_SLAB_web.jpg'),(w,h))
class Player(pygame.sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image),(70,70))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Enemy(Player):
    direction = 'right'
    def update(self):
          if self.rect.x <= 300:
            self.direction = 'right'
          if self.rect.x >= 10000000000000:
            self.direction = 'left'
          if self.direction == 'left':
            self.rect.x -= self.speed
          if self.direction == 'right':
            self.rect.x += self.speed

            
class Hero(Player):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y <= 500: 
            self.rect.y += self.speed

class Wall(pygame.sprite.Sprite):
    def __init__ (self,width,height,color,wall_x,wall_y):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill((color))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
        
    def update(self,walls):
        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self,walls,False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self,walls,False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom



                wall_list = pygame.sprite.Group()

                wall = Wall()
                wall_list.add(wall)
                all_sprite_list.add(wall)

                clock = pygame.time.Clock()








hero = Hero('ddssudhdusudu.png',270,400,10) 
enemy = Enemy('Soccer_ball.svg.png',30,300,5) 
wall = Wall(20,550,(130,183,254),10,100)
wall1 = Wall(20,550,(130,183,254),700,100)
game = True
finish = False
clock = pygame.time.Clock()
FPS = 60
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    if finish != True:
         score_text = font1.render("score:"+str(score), True,(250,250,250))
         score_text1 = font1.render("your max score:"+str(score1), True,(250,250,250))
         window.blit(background, (0,0))
         window.blit(score_text, (230,0))
         hero.update()
         hero.reset()
         enemy.update()
         enemy.reset()
         wall.draw_wall()
         wall1.draw_wall()

    if pygame.sprite.collide_rect(hero,enemy):
        enemy.speed *=-1
        score = score +1
        enemy.rect.y = randint(100,300)
    if pygame.sprite.collide_rect(wall,enemy):
        enemy.speed *=-1
        enemy.rect.y = randint(100,300)
    if score >=100:
            finish = True
            window.blit(win, (200,200))
    if score + 1:
        score1 = score
    if pygame.sprite.collide_rect(wall1,enemy):
        window.blit(score_text1,(200,200))
        finish = True
        




             
        
             
             
             
        
        

    pygame.display.update()
    clock.tick(FPS)

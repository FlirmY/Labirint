#создай игру "Лабиринт"!
from pygame import *
font.init()
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play(-1)
font1=font.Font(None, 70)



Window = display.set_mode((700,500))
background = transform.scale(image.load('bad.jpg'),(700,500))


win = font1.render('YOU WIN' , True,(0,255,0))
lose = font1.render('YOU LOSE', True,(255,0,0))
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self,filename,w,h,speed,x,y):
        super().__init__()
        self.image = transform.scale(image.load(filename),(w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        Window.blit(self.image,(self.rect.x,self.rect.y))



class Player(GameSprite):
    def update (self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 10
        if keys_pressed[K_a]and self.rect.x > 0:
            self.rect.x -= 10
        if keys_pressed[K_s]and self.rect.y < 400:
            self.rect.y += 10
        if keys_pressed[K_d]and self.rect.x < 600:
            self.rect.x += 10

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 300:
            self.direction = "right"
        if self.rect.x >= 500:
            self.direction = "left"

        if self.direction == "left": 
            self.rect.x -= 10
        else:
            self.rect.x += 10

    
class Wall (sprite.Sprite): 
    def __init__ (self,width,height,x,y):
        super().__init__()
        self.image = Surface((width,height))
        self.image.fill((133,24,234))
        self.rect =self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        Window.blit(self.image,(self.rect.x,self.rect.y))



wall1 = Wall(200,20,1,100)
wall2 = Wall(20,200,310,0)
wall3 = Wall(200,20,130,200)
wall4 = Wall(20,160,130,200)
wall5 = Wall(270,20,130,350)
wall6 = Wall(20,400,0,100)
wall7 = Wall(400,20,0,480)
wall8 = Wall(20,200,300,100)
walls = sprite.Group()
walls.add(wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8)






player = Player('man3.png',65,65,10,20,20)
enemy = Enemy('enemy.png',65,65,10,450,300)
victory = GameSprite('treasure.png',65,65,10,450,200)



finish = False



game = True
clock = time.Clock()    
while game:
    if finish != True:
        
        

        Window.blit(background,(0,0))
        player.update()
        player.reset()
        enemy.update()
        enemy.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()        
        wall3.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        victory.reset()
        if sprite.collide_rect(player,victory):
            finish = True
            money.play()
            Window.blit(win,(200,200))
        if sprite.collide_rect(player,enemy):
            finish = True
            kick.play()
            Window.blit(lose,(200,200))
        if len(sprite.spritecollide(player,walls,False)) > 0:
            player.rect.x = 20
            player.rect.y = 20

    clock.tick(60)
    for e in event.get():
        if e.type == QUIT:
             game = False        
    display.update()
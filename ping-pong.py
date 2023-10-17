from pygame import *

win_height = 500
win_width = 700
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load("galaxy.jpg"), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed

pl1 = Player('raketka.png', 595, 330, 10, 65, 85)
pl2 = Player('raketka.png', 40, 330, 10, 65, 85)
font.init()
font1 = font.Font(None, 36)
run = True 
finish = False
FPS = 40
clock = time.Clock()
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish == False:         
        window.blit(background, (0, 0))
        pl1.reset()
        pl1.update()
        pl2.reset()
        pl2.update()
    #for c in collides:
    #    score += 1
    #    monster = Enemy('ufo.png', randint(50, 650), 0, 2, 65, 65)
    #    monsters.add(monster)
        
    #if sprite.spritecollide(ship, monsters, True) or lost == 1:
        
  
    display.update()
    clock.tick(FPS) 
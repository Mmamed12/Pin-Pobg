from pygame import *
back = (200, 120, 10)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

clock = time.Clock()
FPS = 120
game =  True

class GameSprite(sprite.Sprite):
    
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
 
        
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


ball = GameSprite("imgpreview-removebg-preview.png", 200, 200, 50, 50, 4)


while game:
    for e in event.get():
        if  e.type == QUIT:
            game = False

    ball.reset()
    

    display.update()
    clock.tick(FPS)
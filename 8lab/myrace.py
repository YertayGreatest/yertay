import pygame, sys
import random, time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((400, 600))
fps = 60
framepersec = pygame.time.Clock()

speed = 5
score = 0

pygame.mixer.init()
pygame.mixer.music.load("8lab/raceObjects/background.wav")
pygame.mixer.music.play(-1)


object1 = pygame.Rect((20, 50), (50, 100))

object2 = pygame.Rect((10, 10), (100, 100))
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
screen.fill(white)
pygame.display.set_caption("myrace")

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

background = pygame.image.load("8lab/raceObjects/AnimatedStreet.png")
collected_gems = 0
class GreenGem(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("8lab/raceObjects/purplegem.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(40, 400 - 40), random.randint(40, 400-40))
        

    def draw(self, surface):
        
        screen.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("8lab/raceObjects/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -6)
        if self.rect.bottom < 600:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 6)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-6, 0)
        if self.rect.right < 600:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(6, 0)
    
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("8lab/raceObjects/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 400-40),0)
    def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.top > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, 400-40),0)
    
gem = GreenGem()
p1 = Player()
e1 = Enemy()
gems = pygame.sprite.Group()
gems.add(gem)
if len(gems) == 0:
    
    if random.randint(0,100) < 1:
        gem = GreenGem()
        gems.add(gem)
enemies = pygame.sprite.Group()
enemies.add(e1)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)
gem_lasttime = None
        
while True:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == inc_speed:
            speed += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    
    screen.blit(background, (0,0))
    scores = font_small.render("Cars: "+str(score), True, black)
    screen.blit(scores, (10, 10))
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    
    for gem in gems:
        gem.draw(screen)
        
        if pygame.sprite.spritecollideany(p1, gems):
            
            speed -= 0.4
            gems.remove(gem)
            collected_gems += 1
            gem_lasttime = current_time 
            if current_time - gem_lasttime >= 1500:
                new_gem = GreenGem()
                gems.add(new_gem)
    gem_text = font_small.render("Gems: "+str(collected_gems), True, black)
    screen.blit(gem_text, (10, 30))
    
    
    if gem_lasttime is not None and current_time - gem_lasttime >= 1500:
        gems.empty()
        gem = GreenGem()
        gems.add(gem)
        gem_lasttime = None
    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.mixer.Sound('8lab/raceObjects/crash.wav').play()
        time.sleep(0.5)
        
        screen.fill(red)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
         

        time.sleep(1.5) 
        pygame.quit()
        sys.exit()
    
   
    
    
    pygame.display.update()
    framepersec.tick(fps)
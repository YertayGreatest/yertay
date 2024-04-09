import pygame, sys
from random import randrange
pygame.font.init()
window_width = 850
window_height = 800
tile = 50
range = (tile // 2, window_width - tile // 2, tile)


snake = pygame.Rect([0, 0, tile-2, tile-2])

length = 1
segments = [snake.copy()]
snake_dir = [0, 0]
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
time, time_step = 0, 110
score_bar_height = 50
game_board_height = window_height - score_bar_height
#allowed directions
#dirs = {pygame.K_UP: 1, pygame.K_DOWN: 1, pygame.K_LEFT: 1, pygame.K_RIGHT: 1}
dirs = {pygame.K_UP: (0, -tile), pygame.K_DOWN: (0, tile), pygame.K_LEFT: (-tile, 0), pygame.K_RIGHT: (tile, 0)}
#irslet = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
dirslet = {pygame.K_w: pygame.K_UP, pygame.K_s: pygame.K_DOWN, pygame.K_a: pygame.K_LEFT, pygame.K_d: pygame.K_RIGHT}
#food and positioning
fruit = snake.copy()
def randompos():
    x = randrange(tile//2, game_board_height-tile // 2, tile)
    y = randrange(tile//2, game_board_height-tile // 2, tile)
    return [x, y]
fruit.center = randompos()
#time right now
curren_time = pygame.time.get_ticks()
last_time = None #pause between levels
#score counter
score = 0
snake.center = randompos()
seclvl = False

needed = 12


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w and dirslet[pygame.K_w]:
                
                    
                    
                snake_dir = [0, -tile]
                dirslet = {pygame.K_w: 0, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
            if event.key == pygame.K_s and dirslet[pygame.K_s]:
            
                    
                    
                snake_dir = [0, tile]
                dirslet = {pygame.K_w: 1, pygame.K_s: 0, pygame.K_a: 1, pygame.K_d: 1}
            if event.key == pygame.K_a and dirslet[pygame.K_a]:
                snake_dir = [-tile, 0]
                dirslet = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 0, pygame.K_d: 1}
            if event.key == pygame.K_d and dirslet[pygame.K_d]:
                snake_dir = [tile, 0] 
                dirslet = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 0}
            if event.key == pygame.K_UP and dirs[pygame.K_UP]:
                snake_dir = [0, -tile]
                dirs = {pygame.K_UP: 0, pygame.K_DOWN: 1, pygame.K_LEFT: 1, pygame.K_RIGHT: 1}
            if event.key == pygame.K_DOWN and dirs[pygame.K_DOWN]:
                snake_dir = [0, tile]
                dirs = {pygame.K_UP: 1, pygame.K_DOWN: 0, pygame.K_LEFT: 1, pygame.K_RIGHT: 1}
            if event.key == pygame.K_LEFT and dirs[pygame.K_LEFT]:
                snake_dir = [-tile, 0]
                dirs = {pygame.K_UP: 1, pygame.K_DOWN: 1, pygame.K_LEFT: 0, pygame.K_RIGHT: 1}
            if event.key == pygame.K_RIGHT and dirs[pygame.K_RIGHT]:
                snake_dir = [tile, 0]
                dirs = {pygame.K_UP: 1, pygame.K_DOWN: 1, pygame.K_LEFT: 1, pygame.K_RIGHT: 0}
    screen.fill('black')
    pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(0, game_board_height, window_width, score_bar_height))
    #handling food under tail
    food_in_tail = pygame.Rect.collidelist(fruit, segments[:-1])!=-1
    if food_in_tail:
        fruit.center = randompos()
        score += 1
        while fruit.collidelist(segments) != -1:
            fruit.center = randompos()
    
    #collision with itself
    self_coll = pygame.Rect.collidelist(snake, segments[:-1]) != -1
    if self_coll:
        score+=1
    #borders
    if snake.left < 0 or snake.right > window_width or snake.top < 0 or snake.bottom > game_board_height or self_coll:
        snake.center, fruit.center = randompos(), randompos()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]
        score = 0
        needed = 12
    #food eating
    pygame.draw.rect(screen, 'red', fruit)
    if snake.center == fruit.center:
        fruit = snake.copy()
        fruit.center = randompos()
        length += 1
        score += 1
    #movement
    time_now = pygame.time.get_ticks()
    if time_now - time > (80 if seclvl else time_step):
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
    #SECOND LEVEL
    if score >= 12:
        seclvl = True
        time_step = 80
        score = 0
        needed = 14
        snake.center = randompos()  
    #texts
    font = pygame.font.SysFont("Verdana", 36)
    score_text = font.render(f'score: {score}/{needed}', True, (255,255,255))
    screen.blit(score_text, (10, game_board_height + 10))
    
    #last part
    [pygame.draw.rect(screen, 'green', segment) for segment in segments]
    pygame.display.update()
    clock.tick(60)
    
      
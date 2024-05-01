import pygame, sys, random, pygame_gui
pygame.init()
s_w, s_h = 800, 800
block_size = 50
font = pygame.font.SysFont("Arial", block_size * 2)
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("new snake")
clock = pygame.time.Clock()
fps = 7

menu_flag = True



class Snake:
    def __init__(self):
        self.x, self.y = block_size, 150
        self.xdir = 1
        self.ydir = 0 
        self.head = pygame.Rect(self.x, self.y,block_size, block_size)
        self.body = [pygame.Rect(self.x-block_size, self.y,block_size, block_size)]
        self.dead = False
    
    def update(self):
        global apple
        
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, s_w) or self.head.y not in range(100, s_h):
                self.dead = True
        
        if self.dead:
            self.x, self.y = block_size, 150
            self.xdir = 1
            self.ydir = 0
            self.head = pygame.Rect(self.x, self.y,block_size, block_size)
            self.body = [pygame.Rect(self.x-block_size, self.y,block_size, block_size)] 
            self.dead = False
            apple = Apple() 
        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * block_size
        self.head.y += self.ydir * block_size
        self.body.remove(self.head)


class Apple:
    def __init__(self):
        
        self.x = int(random.randint(0, s_w)/block_size) * block_size
        self.y = int(random.randint(100, s_h)/block_size) * block_size
        self.rect = pygame.Rect(self.x, self.y, block_size, block_size)
    def update(self):
        pygame.draw.rect(screen, "red", self.rect)

def drawGrid():
    for x in range(0, s_w, block_size):
        for y in range(0, s_h, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, (48, 48, 48), rect, 1)



def start_game():
    global apple
    snake.update()
    
    screen.fill('black')
    drawGrid()
    bar_for_texts = pygame.draw.rect(screen, "gray", pygame.Rect(0, 0, s_w, 100))
    apple.update()
    #score
    score = font.render(f'{len(snake.body) + 1}', True, 'black')
    #level show
    level = font.render(f'level: {which_lvl}', True, 'black')
    #snake
    pygame.draw.rect(screen, (176, 255, 174), snake.head) 
    
    for square in snake.body:
        pygame.draw.rect(screen, "green", square)
       
    screen.blit(score, score_rect)
    screen.blit(level, level_rect)
           
    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x, square.y, block_size, block_size))
        apple = Apple()  

def menu():
    global menu_flag
    
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    input_rect = pygame.Rect(335, 310, 140, 32)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1] 
                if event.key == pygame.K_RETURN:
                    menu_flag = False
                    return
                    #start_game()
                else:
                    user_text += event.unicode
        screen.fill('black')
        pygame.draw.rect(screen, 'cyan', input_rect, 2)
        enter_text = base_font.render("Enter name:", True, 'white')
        screen.blit(enter_text, (335, 240))
        text_surface = base_font.render(user_text, True, 'white')  
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5) )
        input_rect.w = max(100, text_surface.get_width() + 10)
        pygame.display.update()
        clock.tick(60)



score = font.render('1', True, 'black')
score_rect = score.get_rect(center=(s_w-100, s_h-750))

level = font.render('1', True, 'black')
level_rect = level.get_rect(center=(s_w/20, s_h/20))
which_lvl = 1


#drawGrid()


snake = Snake()

apple = Apple()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            
            
            
            if event.key == pygame.K_DOWN:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_UP:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_RIGHT:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pygame.K_LEFT:
                snake.ydir = 0
                snake.xdir = -1
    
    if menu_flag:
        menu()
    else:
        start_game()     
    pygame.display.update()
    clock.tick(fps)
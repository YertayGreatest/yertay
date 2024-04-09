import pygame, sys
pygame.init()
scr_width = 800
scr_height = 600
fps = 1000
timer = pygame.time.Clock()
screen = pygame.display.set_mode([scr_width, scr_height])
pygame.display.set_caption('paint')
size_rn = 0
color_rn = 'white'
painting = []


#menu
def menu(size, color):
    pygame.draw.rect(screen, 'gray', [0, 0, scr_width, 70])
    pygame.draw.line(screen, 'black', (0, 70), (scr_width, 70), 3)
    bigger = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (35,35), 20)
    big = pygame.draw.rect(screen, 'black', [70, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (95, 35), 15)
    meduim = pygame.draw.rect(screen, 'black', [130, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (155, 35), 10)
    small = pygame.draw.rect(screen, 'black', [190, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (215, 35), 5)
    #picked color
    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 5)
    
    
    
    #colors:
    blue = pygame.draw.rect(screen, (0, 0, 255), [scr_width - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [scr_width - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [scr_width - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [scr_width - 60 , 35, 25, 25])
    white = pygame.draw.rect(screen, (255, 255, 255), [scr_width - 85, 10, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [scr_width - 85, 35, 25, 25])
    brushes = [bigger, big, meduim, small]
    colors = [blue, red, green, yellow, white, black]
    rgb = [(0, 0, 255),(255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 255, 255),(0, 0, 0) ]
    if size == 20:
        pygame.draw.rect(screen, 'green', [10, 10, 50, 50], 3)
    elif size == 15:
        pygame.draw.rect(screen, 'green', [70, 10, 50, 50], 3)
    elif size == 10:
        pygame.draw.rect(screen, 'green', [130, 10, 50, 50], 3)
    elif size == 5:
        pygame.draw.rect(screen, 'green', [190, 10, 50, 50], 3)  
    
    return brushes, colors, rgb
#paint
def paint(paints):
    for i in range(len(paints)):
        pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])

while True:
    timer.tick(fps)
    screen.fill('white')
    
    mousepos = pygame.mouse.get_pos()
    leftmouse = pygame.mouse.get_pressed()[0]
    
    if mousepos[1] > 70 and leftmouse:
        painting.append((color_rn, mousepos, size_rn))
    
    paint(painting)
    if mousepos[1] > 70:
        pygame.draw.circle(screen, color_rn, mousepos, size_rn)
    brushes, colors, rgb = menu(size_rn, color_rn)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(len(brushes)):
                    if brushes[i].collidepoint(event.pos):
                        size_rn = 20 - (i*5)
                for i in range(len(colors)):
                    if colors[i].collidepoint(event.pos):
                        color_rn = rgb[i]
     
    
    pygame.display.update()
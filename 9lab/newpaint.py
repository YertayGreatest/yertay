import pygame, sys
pygame.init()
s_width = 1200
s_height = 800
screen = pygame.display.set_mode([s_width, s_height])

pygame.display.set_caption('paint v1')
clock = pygame.time.Clock()
#pencil
pencil = pygame.image.load('9lab/pencil.jpg')
pencil = pygame.transform.scale(pencil, [75, 75])
pencil_rect = pygame.Rect(10, 10, 75, 75)
def draw_pencil():
    screen.blit(pencil, pencil_rect.topleft)
    
pencil_pressed = False
#pencil options
def pencil_options():
    s1 = pygame.draw.rect(screen, 'black', [10, 110, 75, 75])
    sc1 = pygame.draw.circle(screen, 'white', [47.5, 147.5], 30)
    s2 = pygame.draw.rect(screen, 'black', [10, 195, 75, 75])
    sc2 = pygame.draw.circle(screen, 'white', [47.5, 232.5], 22.5)
    s3 = pygame.draw.rect(screen, 'black', [10, 280, 75, 75])
    sc3 = pygame.draw.circle(screen, 'white', [47.5, 317.5], 15)
    return s1, s2, s3, sc1, sc2, sc3
s1rect = pygame.Rect(10, 110, 75, 75)
s2rect = pygame.Rect(10, 195, 75, 75)
s3rect = pygame.Rect(10, 280, 75, 75)
#SHAPES
#rectangle
def menurec():
    return pygame.draw.rect(screen, 'black', [95, 10, 75, 75])
menurect = pygame.Rect(95, 10, 75, 75)
rectangle_pressed = False
#circle
def menucircle():
    return pygame.draw.circle(screen, 'black', [220, 50], 37.5)
menucirc = pygame.Rect(185, 35, 75, 75)
circles = []
circle_drawing = False
#colors
def color_pallete():
    red_square = pygame.draw.rect(screen,'red', [s_width - 40, 10, 30, 30])
    blue_square = pygame.draw.rect(screen,'blue', [s_width - 40, 40, 30, 30])
    yellow_square = pygame.draw.rect(screen, 'yellow', [s_width - 70, 10, 30, 30])
    green_square = pygame.draw.rect(screen, 'green', [s_width - 70, 40, 30, 30])
    white_square = pygame.draw.rect(screen, 'white', [s_width - 100, 10, 30, 30])
    black_square = pygame.draw.rect(screen, 'black', [s_width - 100, 40, 30, 30])
    return red_square, blue_square, yellow_square, green_square, white_square, black_square
red_rect = pygame.Rect(s_width - 40, 10, 30, 30)
blue_rect = pygame.Rect(s_width - 40, 40, 30, 30)
yellow_rect = pygame.Rect(s_width - 70, 10, 30, 30)
green_rect = pygame.Rect(s_width - 70, 40, 30, 30)
white_rect = pygame.Rect(s_width - 100, 10, 30, 30)
black_rect = pygame.Rect(s_width - 100, 40, 30, 30)
rgbs = [(255, 0, 0), (0, 0, 255), (255,211,67), (0, 255, 0), (255, 255, 255), (0, 0, 0)]
colors = [red_rect, blue_rect, yellow_rect, green_rect, white_rect, black_rect]
#picked options
color_rn = 'black'
brush_rn = None
drawing = False
drawings = []
rectangle_drawing = False
rectangle_drawings = []
#pos
startx = 10
starty = 10
endx = 10
endy = 10
#flag
rectangle_drawn = False
circle_drawn = False

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        px, py = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button == 1:
                if pencil_rect.collidepoint(event.pos):
                    if pencil_pressed:
                        pencil_pressed = False  
                        rectangle_drawing = False
                        rectangle_drawn = False
                        print("pencil closed")
                    else:
                        pencil_pressed = True
                        
                        rectangle_pressed = False
                        rectangle_drawing = False
                        rectangle_drawn = False 
                        
                        print("pencil opened")
                if pencil_pressed and s1rect.collidepoint(event.pos):
                    brush_rn = 30   
                                   
                    print("big brush picked")
                if pencil_pressed and s2rect.collidepoint(event.pos):
                    brush_rn = 22.5
                if pencil_pressed and s3rect.collidepoint(event.pos):
                    brush_rn = 15
                   
                for i in range(len(colors)):
                    if colors[i].collidepoint(event.pos):
                        color_rn = rgbs[i]
                        print("color picked")
                        rectangle_drawn = False
                
                
                if menurect.collidepoint(event.pos):
                    rectangle_pressed = True
                    pencil_pressed = False
                    drawing = False
                    rectangle_drawing = True
                    brush_rn = None
                    
                    print("rec")
                if menucirc.collidepoint(event.pos):
                    rectangle_pressed = False
                    rectangle_drawing = False
                    rectangle_drawn = False
                    pencil_pressed = False
                    drawing = False
                    circle_drawing = True
                    print("circle")
                    startx, starty = event.pos
                    
                
            if color_rn is not None and brush_rn is not None and not pencil_pressed:
                drawing = True 
                
            if rectangle_pressed and color_rn is not None:
                rectangle_drawing = True
                startx = event.pos[0]
                starty = event.pos[1]
            if circle_drawing and color_rn is not None:
                startx = event.pos[0]
                starty = event.pos[1]
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                drawings.append((color_rn, [px, py], brush_rn))
                rectangle_drawing = False
            if rectangle_drawing:
                endx = event.pos[0]
                
                    
                endy = event.pos[1]
                pygame.draw.rect(screen, color_rn, [(min(startx, endx)), (min(starty, endy)), (abs(startx-endx)), (abs(starty - endy))] )
                
            if circle_drawing:
                endx, endy = event.pos  
                radius = int(((endx - startx) ** 2 + (endy - starty) ** 2) ** 0.5) // 2
                pygame.draw.ellipse(screen, color_rn, [min(startx, endx - radius), min(starty, endy - radius), 2 * radius, 2 * radius])
                        
                
            
            
            

                
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if rectangle_drawing:
                final_rectangle = (color_rn, min(startx, endx), min(starty, endy), abs(startx-endx), abs(starty - endy))
                if pencil_pressed == False:
                    
                    rectangle_drawings.append(final_rectangle)
            rectangle_drawing = False
            rectangle_drawn = True
            if circle_drawing:
                radius = int(((endx - startx) ** 2 + (endy - starty) ** 2) ** 0.5) // 2
                final_circle = (color_rn, startx - radius, starty - radius, 2 * radius, 2 * radius)
                circles.append(final_circle)
                circle_drawing = False
                        
    
               
    for circle in circles:
        pygame.draw.ellipse(screen, circle[0], [circle[1], circle[2], circle[3], circle[4]] )
        
    
    for rect in rectangle_drawings:
        pygame.draw.rect(screen, rect[0], [rect[1], rect[2], rect[3], rect[4]] )
    
    
    for i in range(len(drawings)):
        pygame.draw.circle(screen, drawings[i][0], drawings[i][1], drawings[i][2])
    if circle_drawn:
        pygame.draw.ellipse(screen, color_rn, [(min(startx, endx)), (min(starty, endy)), abs(startx-endx), abs(starty - endy)] )
        circle_drawn = False
    if rectangle_drawn:

            pygame.draw.rect(screen, color_rn, [(min(startx, endx)), (min(starty, endy)), (abs(startx-endx)), (abs(starty - endy))] )    
    pygame.draw.rect(screen, 'gray', [0, 0, s_width, 100 ]) #menu
    
    draw_pencil()
    if pencil_pressed:
        pencil_options()
    menurec()
    color_pallete()
    menucircle()
    
    
        
    pygame.display.update()
    clock.tick(1000)
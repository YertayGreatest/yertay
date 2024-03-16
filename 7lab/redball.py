import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('red ball')

radius = 50


posx = 400
posy = 300




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                posx = posx - 20
            elif event.key == pygame.K_RIGHT:
                posx = posx + 20
            elif event.key == pygame.K_UP:
                posy = posy - 20
            elif event.key == pygame.K_DOWN:
                posy = posy + 20
                
        if posx - radius < 0:  
            posx = radius
        elif posx + radius > 800:  
            posx = 800 - radius
        if posy - radius < 0:  
            posy = radius
        elif posy + radius > 600:  
            posy = 600 - radius
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (posx, posy), radius)
        
    
    
    
    pygame.display.update()

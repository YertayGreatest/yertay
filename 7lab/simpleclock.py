import pygame
import sys
import datetime

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('mickey clock')
run = True

current_time = datetime.datetime.now().time()
minute = current_time.minute
second = current_time.second

bg_mickey = pygame.image.load('mainclock.png').convert()

bg_mickey = pygame.transform.scale(bg_mickey, (width, height))
#RIGHT ARM
right_arm = pygame.image.load('rightarm.png')
right_arm = pygame.transform.scale(right_arm, (700, 600))


right_arm_rect = right_arm.get_rect()
right_arm_rect.bottom = 610
right_arm_rect.centerx = 400
right_rotation_speed = -0.1
angle_right = -(minute * 6) - 36



#LEFT ARM
left_arm = pygame.image.load('leftarm.png')
left_arm = pygame.transform.scale(left_arm, (50,600))
                                  
left_arm_rect = left_arm.get_rect()
left_arm_rect.bottom = 610
left_arm_rect.centerx = 400
clock = pygame.time.Clock()
left_rotation_speed = -6
angle_left = -(second * 6) 






pygame.display.update()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(bg_mickey,(0, 0))
    
    
    
    #LEFT ARM
    rotated_left = pygame.transform.rotate(left_arm, angle_left)
    rotated_rect_left = rotated_left.get_rect(center=left_arm_rect.center)
    screen.blit(rotated_left, rotated_rect_left)
    angle_left += left_rotation_speed * clock.get_time() / 1000.0
    angle_left %= 360
    #RIGHT ARM
    rotated_right = pygame.transform.rotate(right_arm, angle_right)
    rotated_rect_right = rotated_right.get_rect(center=right_arm_rect.center)
    screen.blit(rotated_right, rotated_rect_right)
    angle_right += right_rotation_speed * clock.get_time() / 1000.0
    angle_right %= 360
    pygame.display.update()
    clock.tick(60)
   
    
    
    
pygame.quit()
sys.exit()
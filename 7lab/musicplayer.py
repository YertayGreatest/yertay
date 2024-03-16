import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('music player')
pygame.mixer.init()
playlist = ['sound.mp3', 'song2.mp3', 'song3.mp3']
current_track_index = 0
pygame.mixer.music.load(playlist[current_track_index])
music = pygame.mixer.music.load('sound.mp3')
playing = False
paused = False
pos = 0  # to start from stopped moment

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not playing:
                    pygame.mixer.music.play(start=pos)  
                    playing = True
                    paused = False
                elif not paused:
                    pygame.mixer.music.pause()
                    pos = pygame.mixer.music.get_pos() / 1000  
                    paused = True
                else:
                    pygame.mixer.music.unpause()
                    playing = True
                    paused = False
            elif event.key == pygame.K_RIGHT:
                current_track_index = (current_track_index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_track_index = (current_track_index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track_index])
                pygame.mixer.music.play()
        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        text = font.render('Playing:'+ playlist[current_track_index], True, (0, 0, 0))
        screen.blit(text, (50, 50))
        
        playlist_font = pygame.font.Font(None, 30)
        for i, song in enumerate(playlist):
            color = (255, 0, 0) if i == current_track_index else (0, 0, 0)
            playlist_text = playlist_font.render(str(i + 1) + '.'+ song, True, color)
            screen.blit(playlist_text, (70, 170 + i * 30))
            
                        

        
                
        
        
        pygame.display.update()
    pygame.time.wait(10)

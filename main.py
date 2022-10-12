import sys
import pygame
import player


pygame.init()

d = (500,500)

screen = pygame.display.set_mode(d) # my screen
player = player.Player()
player.draw(screen) #recording

screen.fill("lightblue")

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: #Closing the window of the game when exit botton being pressed
            pygame.quit()
            sys.exit() # closing system's window

    player.point_at(*pygame.mouse.get_pos())
    keys = pygame.key.get_pressed()
    player.move(keys[pygame.K_d] - keys[pygame.K_a], keys[pygame.K_s] - keys[pygame.K_w])
    screen.fill("lightgrey")
    player.draw(screen)

    pygame.display.update() #rendring for pygame
    pygame.time.delay(16) #60 FPS

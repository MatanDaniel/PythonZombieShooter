import sys
import pygame
import player
import zombie
import bullet


pygame.init()

d = (500,500)

#Program's objects:
screen = pygame.display.set_mode(d) # my screen
player = player.Player()
player.draw(screen) #recording
zombie1 = zombie.Zombie()
zombie1.draw(screen)
bullet = bullet.Bullet()
bullet.draw(screen)


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
    zombie1.draw(screen)
    zombie1.point_at(*player.rect.center) #looking at player
    zombie1.move(player)



    pygame.display.update() #rendring for pygame
    pygame.time.delay(16) #60 FPS

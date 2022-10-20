import sys
import pygame
import player
import zombie
import bullet

pygame.init()
d = (1000  , 1000)

# Program's objects:
screen = pygame.display.set_mode(d)  # my screen
player = player.Player()
zombies = pygame.sprite.Group()
zombies.add(zombie.Zombie())
zombies.add(zombie.Zombie())
zombies.add(zombie.Zombie())
screen.fill("lightblue")

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 20)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:  # Closing the window of the game when exit botton being pressed
            pygame.quit()
            sys.exit()  # closing system's window
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.attack()

    player.point_at(*pygame.mouse.get_pos())
    keys = pygame.key.get_pressed()
    player.move(keys[pygame.K_d] - keys[pygame.K_a], keys[pygame.K_s] - keys[pygame.K_w])
    screen.fill("lightgrey")
    player.draw(screen, zombies)
    zombies.update(screen,player)

    ### Debug
    text_surface = my_font.render(f'Mouse pos:{pygame.mouse.get_pos()}', False, 'red')
    player_debug = my_font.render(f'Player pos:{player.rect.center}', False, 'blue')
    screen.blit(text_surface, (0, 0))
    screen.blit(player_debug, (0, text_surface.get_height()))


    pygame.display.update()  # rendring for pygame
    pygame.time.delay(16)  # 60 FPS

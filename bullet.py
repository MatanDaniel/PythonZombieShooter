import pygame

import Assets
from pygame.sprite import AbstractGroup
class Bullet(pygame.sprite.Sprite):
    def __init__(self,*groups: AbstractGroup):
        super().__init__(*groups)
        self.original_image = pygame.image.load("Assets\\bullet.png")
        self.time_to_live = 500 #bullet time of actually existing on the screen
        self.speed = 5
        self.rect = self.original_image.get_rect()
        self.image = pygame.image.load("Assets\\bullet.png")
        self.image = pygame.transform.scale(self.image,(20,10))

    def hit(self):
        pass

    def draw(self,screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, "green", self.rect,width = 1)


    def move(self, player):
        print("bullet is on the move")
        direction = pygame.Vector2(*pygame.mouse.get_pos()) #gets position of mouse as vector
        player_vector = pygame.Vector2(player.rect.center)
        towards = (player_vector - direction)
        self.rect.move_ip(towards)

    def update(self):
        pass









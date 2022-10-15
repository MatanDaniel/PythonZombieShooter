import pygame
import Assets
from pygame.sprite import AbstractGroup
class Bullet(pygame.sprite.Sprite):
    def __init__(self,*groups: AbstractGroup):
        super().__init__(*groups)
        self.image = pygame.image.load("Assets\\bullet.png")
        self.time_to_live = 500 #bullet time of actually existing on the screen
        self.speed = 5
        self.rect = self.image.get_rect()

    def hit(self):
        pass

    def draw(self,screen):
        screen.blit(self.image, self.rect.center)

    def move(self,zombie):
        direction = pygame.Vector2(*pygame.mouse.get_pos()) #gets position of mouse as vector
        # while True:




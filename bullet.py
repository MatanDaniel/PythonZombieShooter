import pygame

import Assets
from pygame.sprite import AbstractGroup


class Bullet(pygame.sprite.Sprite):
    def __init__(self, player, *groups: AbstractGroup):
        super().__init__(*groups)
        self.time_to_live = 100  # bullet time of actually existing on the screen
        self.speed = 15
        self.image = pygame.image.load("Assets\\bullet.png")
        self.image = pygame.transform.scale(self.image, (20, 10))
        self.location = player.rect.center
        self.rect = self.image.get_rect(center=self.location)
        self.direction = pygame.Vector2(*pygame.mouse.get_pos())
        self.player_vector = pygame.Vector2(self.location)

        m = pygame.math.Vector2(0,0)
        angle = m.angle_to((self.direction - self.player_vector).normalize())
        self.image = pygame.transform.rotate(self.image, -angle)


    def hit(self, zombies):
        zombie = pygame.sprite.spritecollideany(self,zombies)
        if zombie is not None:
            zombie.take_damage()
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, "green", self.rect, width=1)

        if self.time_to_live <= 0:
            self.kill()

    def move(self):
        towards = (self.direction - self.player_vector).normalize() #Vector towards mouse positioning
        self.rect.move_ip(towards * self.speed)
        self.time_to_live -= 1


    def update(self, *args):
        self.draw(args[0])
        self.move()
        self.hit(args[1])  # collision check

import pygame
from pygame.sprite import AbstractGroup

import bullet


class Player(pygame.sprite.Sprite):  # base for sprite objects
    def __init__(self, *groups: AbstractGroup):
        super().__init__(*groups)
        self.ammo = 100  # player's ammo
        self.is_alive = True
        self.moving = False
        self.acquire_ammo = False
        self.level = 0
        self.health = 100  # player's health
        self.position = (100, 100)
        self.original_image = pygame.image.load("Assets\\up.png")  # load image from assets
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.position)  # boundary box of the player
        self.velocity = 5  # player's speed
        self.bullets = pygame.sprite.Group()

    def draw(self, screen: pygame.Surface, zombies):
        screen.blit(self.image, self.rect)  # blit function to draw the player in coordinate (0,0)
        pygame.draw.rect(screen, "red", self.rect, width=1)  # enabling player's rectangle
        self.bullets.update(screen, zombies)

    def attack(self):
        if self.ammo > 0:
            self.bullets.add(bullet.Bullet(self))

    def pick_ammo(self):
        pass

    def point_at(self, x, y):  # mouse rotation ability
        direction = pygame.math.Vector2(x, y) - self.rect.center
        angle = direction.angle_to(pygame.math.Vector2(0, -1))
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)  # player's actual boundary box

    def move(self, x, y):
        self.rect.move_ip(x * self.velocity, y * self.velocity)

    def level(self):
        pass

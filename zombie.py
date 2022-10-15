import pygame
from pygame.sprite import AbstractGroup
class Zombie(pygame.sprite.Sprite):
    def __init__(self,*groups: AbstractGroup):
        super().__init__(*groups)
        self.is_alive = True
        self.moving = False
        self.health = 100 #zombie's health
        self.position = (20,20)
        self.original_image = pygame.image.load("Assets\\zup.png") #zombie's image from Assets folder
        self.image = self.original_image
        self.rect= self.image.get_rect(center = self.position) #boundary box for zombie
        self.velocity = 4 #zombie's speed

    def draw(self, screen:pygame.Surface):
        screen.blit(self.image,self.rect)
        pygame.draw.rect(screen, "blue",self.rect, width = 1) #enabling zombie's rectangle

    def point_at(self, x, y): #mouse rotation ability
        direction = pygame.math.Vector2(x, y) - self.rect.center
        angle = direction.angle_to(pygame.math.Vector2(0,-1))
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)# player's actual boundary box

    def move(self, player):
        try:
            zombie_vector = pygame.Vector2(self.rect.center) # converting tuple of
            player_vector = pygame.Vector2(player.rect.center)
            towards = (player_vector - zombie_vector).normalize() * self.velocity
            self.rect.move_ip(towards)
        except:
            pass


    def attack(self):
        pass
        #Rect.Contains
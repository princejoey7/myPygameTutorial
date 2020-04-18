import pygame


class Ship():

    def __init__(self, screen):
        """initiliaze the ship and set it position"""
        self.screen = screen

        # Load the ship image and set it rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False

    def update(self):
        # Update the ship position based on movement flag.
        if self.moving_right:
            self.rect.centerx +=1

    def blitme(self):
        #draw the ship at this location
        self.screen.blit(self.image, self.rect)

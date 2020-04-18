import sys

import pygame

def check_events(ship):
    """ Respond to key presses and mouse event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #move the ship to the RIGHT
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False        



def update_screen(ai_settings, screen, ship):
    # update images on the screen and flip to new screen
    #Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # make the most recent draw visible
    pygame.display.flip()

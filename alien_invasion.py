
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # initialise a game and create a screen object
    pygame.init()
    # initialize pygame settings, and screen settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Make a Ship
    ship = Ship(ai_settings, screen)
    # make a group to store a bullet
    bullets = Group()

    # start the main loop of the run_game
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # get rid of the bullet that disappear
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
            print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)

        # Redraw the screen during each pass through loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()


          # make the most recently draw screen visible
        pygame.display.flip()
run_game()

import pygame

from src.player import PlayerModel, GROUND_Y
from levels.level1 import PLATFORMS
from utils.utils import *

pygame.init()

WINDOW_SIZE = (800, 600)

screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 22)

#icon
pygame.display.set_caption("Ananas in RTF")
icon = pygame.image.load("assets/images/icon.svg")
pygame.display.set_icon(icon)

#Background img
background_image = pygame.image.load("assets/images/background.png").convert()
background_image = pygame.transform.scale(background_image, WINDOW_SIZE)
pygame.display.flip()
screen.blit(background_image, (0, 0))

WORLD_WALLS = [
    pygame.Rect(0, 0, 20, 600),    # Левая стена
    pygame.Rect(780, 0, 20, 600),  # Правая стена
]

player = PlayerModel(100, 400, 40, 40, (0, 200, 120))

lvl = ''

run = True

while run:
    pygame.display.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE or e.key == pygame.K_UP or e.key == pygame.K_w:
                player.jump()

            if e.key == pygame.K_1:
                lvl = 'level1'

            if e.key == pygame.K_ESCAPE:
                lvl = ''
                screen.blit(background_image, (0, 0))

    if not lvl:
        menu = pygame.Rect(50, 50, 700, 500)
        pygame.draw.rect(screen, (171, 171, 255), menu)

        draw_centered_text_in_rect(
            screen,
            "Нажмите цифру на клавиатуре для выбора уровня",
            font,
            (255, 255, 0),
            menu
        )

        pygame.display.flip()

    if lvl:
        keys = pygame.key.get_pressed()
        move_right = keys[pygame.K_RIGHT] or keys[pygame.K_d]
        move_left = keys[pygame.K_LEFT] or keys[pygame.K_a]
        dx = move_right - move_left

        screen.blit(background_image, (0, 0))
        pygame.draw.line(screen, (0, 0, 110), (0, GROUND_Y), (800, GROUND_Y), 20)

        if lvl == 'level1':
            player.update(dx, WORLD_WALLS, PLATFORMS)
            for platform in PLATFORMS:
                pygame.draw.rect(screen, (171, 171, 255), platform)

            player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
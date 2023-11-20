import math

import pygame

from PacmanBoard import boards

pygame.init()

WIDTH = 600
HEIGHT = 700

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Pacman")
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font("freesansbold.ttf", 20)
level = boards
color = 'blue'

player_images = []
for i in range(1, 5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'Pacman{i}.png'), (30, 30)))

player_x = 300
player_y = 475
direction = 0
counter = 0


def draw_board(level):
    number1 = ((HEIGHT - 50) // 32)
    number2 = ((WIDTH // 30))

    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * number2 + (.5 * number2), i * number1 + (.5 * number1)), 4)

            if level[i][j] == 2:
                pygame.draw.circle(screen, 'white', (j * number2 + (.5 * number2), i * number1 + (.5 * number1)), 10)

            if level[i][j] == 3:
                pygame.draw.line(screen, color, (j * number2 + (.5 * number2), i * number1),
                                 (j * number2 + (.5 * number2), i * number1 + number1), 3)
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j * number2, i * number1 + (.5 * number1)),
                                 (j * number2 + number2, i * number1 + (.5 * number1)), 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, color,
                                [(j * number2 - (number2 * .4)), (i * number1 + (.5 * number1)), number2, number1],
                                0,
                                math.pi / 2, 3)

            if level[i][j] == 6:
                pygame.draw.arc(screen, color,
                                [(j * number2 + (number2 * .4)), (i * number1 + (.5 * number1)), number2, number1],
                                math.pi / 2, math.pi, 3)

            if level[i][j] == 7:
                pygame.draw.arc(screen, color,
                                [(j * number2 + (number2 * .5)), (i * number1 - (.4 * number1)), number2, number1],
                                math.pi, 3 * math.pi / 2, 3)

            if level[i][j] == 8:
                pygame.draw.arc(screen, color,
                                [(j * number2 - (number2 * .4)) - 2, (i * number1 - (.4 * number1)), number2, number1],
                                3 * math.pi / 2, 2 * math.pi, 3)
            if level[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * number2, i * number1 + (.5 * number1)),
                                 (j * number2 + number2, i * number1 + (.5 * number1)), 3)


def draw_player():
    if direction == 0:
        screen.blit(player_images[counter // 5], (player_x, player_y))
    elif direction == 1:
        screen.blit(pygame.transform.flip(player_images[counter // 5], True, False), (player_x, player_y))
    elif direction == 2:
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 90), (player_x, player_y))
    elif direction == 3:
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 270), (player_x, player_y))


def game_loop():
    running = True

    while running:
        timer.tick(fps)
        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_board(level)
        draw_player()
        pygame.display.flip()


game_loop()

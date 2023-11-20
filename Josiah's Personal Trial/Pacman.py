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
flicker = False
direction_command = 0
valid_turns = [False, False, False, False]
player_speed = 2


def draw_board(level):
    number1 = ((HEIGHT - 50) // 32)
    number2 = ((WIDTH // 30))

    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * number2 + (.5 * number2), i * number1 + (.5 * number1)), 4)

            if level[i][j] == 2 and not flicker:
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


def check_player_position(center_x, center_y):
    valid_turns = [False, False, False, False]
    number1 = (HEIGHT - 50) // 32
    number2 = (WIDTH // 30)
    number3 = 15

    if center_x // 30 < 29:
        # Change these lines in check_player_position function
        if direction == 0:
            if level[center_y // number1][(center_x - number3) // number2] < 3:
                valid_turns[1] = True
        if direction == 1:
            if level[center_y // number1][(center_x + number3) // number2] < 3:
                valid_turns[0] = True
        if direction == 2:
            if level[(center_y + number3) // number1][center_x // number2] < 3:
                valid_turns[3] = True
        if direction == 3:
            if level[(center_y - number3) // number1][center_x // number2] < 3:
                valid_turns[2] = True

        if direction == 2 or direction == 3:
            if 12 <= center_x % number2 <= 18:
                if level[(center_y + number3) // number1][center_x // number2] < 3:
                    valid_turns[3] = True
                if level[(center_y - number3) // number1][center_x // number2] < 3:
                    valid_turns[2] = True

            if 12 <= center_y % number1 <= 18:
                if level[center_y // number1][center_x - number2 // number2] < 3:
                    valid_turns[1] = True
                if level[center_y // number1][center_x + number2 // number2] < 3:
                    valid_turns[0] = True

        if direction == 0 or direction == 1:
            if 12 <= center_x % number2 <= 18:
                if level[(center_y + number1) // number1][center_x // number2] < 3:
                    valid_turns[3] = True
                if level[(center_y - number1) // number1][center_x // number2] < 3:
                    valid_turns[2] = True

            if 12 <= center_y % number1 <= 18:
                if level[center_y // number1][center_x - number3 // number2] < 3:
                    valid_turns[1] = True
                if level[center_y // number1][center_x + number3 // number2] < 3:
                    valid_turns[0] = True

    else:
        valid_turns[0] = True
        valid_turns[1] = True

    return valid_turns


def move_player(player_x, player_y):
    if direction == 0 and valid_turns[0]:
        player_x += player_speed
    elif direction == 1 and valid_turns[1]:
        player_x -= player_speed
    elif direction == 2 and valid_turns[2]:
        player_y -= player_speed
    elif direction == 3 and valid_turns[3]:
        player_y += player_speed

    return player_x, player_y


def game_loop():
    global counter, direction, flicker, direction_command, valid_turns, player_x, player_y
    running = True

    while running:
        timer.tick(fps)

        if counter < 19:
            counter += 1
            if counter > 3:
                flicker = False
        else:
            counter = 0
            flicker = True

        screen.fill('black')
        center_x = player_x + 23
        center_y = player_y + 24
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction_command = 0
                if event.key == pygame.K_LEFT:
                    direction_command = 1
                if event.key == pygame.K_UP:
                    direction_command = 2
                if event.key == pygame.K_DOWN:
                    direction_command = 3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT and direction_command == 0:
                    direction_command = direction
                if event.key == pygame.K_LEFT and direction_command == 1:
                    direction_command = direction
                if event.key == pygame.K_UP and direction_command == 2:
                    direction_command = direction
                if event.key == pygame.K_DOWN and direction_command == 3:
                    direction_command = direction

        for i in range(4):
            if direction_command == i and valid_turns[i]:
                direction = i

        player_x, player_y = move_player(player_x, player_y)
        if player_x > WIDTH:
            player_x = -47
        elif player_x < -50:
            player_x = WIDTH - 3

        draw_board(level)
        draw_player()

        valid_turns = check_player_position(center_x, center_y)
        pygame.display.flip()


game_loop()

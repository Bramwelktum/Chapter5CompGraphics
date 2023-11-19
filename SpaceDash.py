import math
import random

import pygame
from pygame import mixer

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
background_img = pygame.image.load('space.jpg')
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))
mixer.music.load('Soundridemusic.wav')
mixer.music.play(-1)

pygame.display.set_caption("Space Invaders")

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 30)
textX = 20
textY = 20

game_over_font = pygame.font.Font('freesansbold.ttf', 50)

# MY PLAYER
playerImg = pygame.image.load('monster.png')
playerImgW = 50
playerImgH = 50
playerImg = pygame.transform.scale(playerImg, (playerImgW, playerImgH))
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# ENEMY
enemyImg = pygame.image.load('cthulhu.png')
enemyImgW = 50
enemyImgH = 50
enemyImg = pygame.transform.scale(enemyImg, (enemyImgW, enemyImgH))
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5

for i in range(num_of_enemies):
    enemyX.append(random.randint(0, 750))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# BALL
ballImg = pygame.image.load('fitness-ball.png')
ballImgW = 20
ballImgH = 20
ballImg = pygame.transform.scale(ballImg, (ballImgW, ballImgH))
ballX = 0
ballY = 480
ballX_change = 0
ballY_change = 1
ball_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg, (x, y))


def fire_ball(x, y):
    global ball_state
    ball_state = "fire"
    screen.blit(ballImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, ballX, ballY):
    distance = math.sqrt((math.pow(enemyX - ballX, 2)) + (math.pow(enemyY - ballY, 2)))
    if distance < 27:
        return True
    else:
        return False


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over():
    over_text = game_over_font.render("GAME OVER!!", True, (255, 0, 0))
    screen.blit(over_text, (200, 250))


running = True
while running:
    screen.fill((2, 0, 128))
    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # ACTIONS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -.4
            elif event.key == pygame.K_RIGHT:
                playerX_change = .4
            elif event.key == pygame.K_UP:
                playerY_change = -.4
            elif event.key == pygame.K_DOWN:
                playerY_change = .4
            if event.key == pygame.K_SPACE:
                if ball_state == "ready":
                    ball_sound = mixer.Sound('Pop Bubble Sound Effect 2022.wav')
                    ball_sound.play()
                    ballX = playerX
                    fire_ball(ballX, ballY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    if playerX < 0:
        playerX = 0
    elif playerX > (screen_width - playerImgW):
        playerX = (screen_width - playerImgW)

    if playerY < 0:
        playerY = 0
    elif playerY > (screen_height - playerImgH):
        playerY = (screen_height - playerImgH)

    for i in range(num_of_enemies):
        if enemyY[i] > playerY:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] < 0:
            enemyX_change[i] = .3
            enemyY[i] += enemyY_change[i]

        elif enemyX[i] >= 750:
            enemyX_change[i] = -.3
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], ballX, ballY)
        if collision:
            explode_sound = mixer.Sound('Explosion Sound Effect.wav')
            explode_sound.play()
            ballY = 480
            ball_state = "ready"
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0, 750)
            enemyY[i] = random.randint(0, 50)

        enemy(enemyX[i], enemyY[i], i)

    if ballY <= 0:
        ballY = 480
        ball_state = "ready"

    if ball_state == "fire":
        fire_ball(ballX, ballY)
        ballY -= ballY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

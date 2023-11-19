import random

import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
background_img = pygame.image.load('space.jpg')
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

pygame.display.set_caption("Space Invaders")

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
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40

# BALL
ballImg = pygame.image.load('fitness-ball.png')
ballImgW = 20
ballImgH = 20
ballImg = pygame.transform.scale(ballImg, (ballImgW, ballImgH))
ballX = 0
ballY = 480
ballX_change = 0
ballY_change = .4
ball_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_ball(x, y):
    global ball_state
    ball_state = "fire"
    screen.blit(ballImg, (x + 16, y + 10))


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
                playerX_change = -.1
            elif event.key == pygame.K_RIGHT:
                playerX_change = .1
            elif event.key == pygame.K_UP:
                playerY_change = -.1
            elif event.key == pygame.K_DOWN:
                playerY_change = .1
            if event.key == pygame.K_SPACE:
                if ball_state == "ready":
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

    enemyX += enemyX_change

    if enemyX < 0:
        enemyX_change = .3
        enemyY += enemyY_change

    elif enemyX > (screen_width - enemyImgW):
        enemyX_change = -.3
        enemyY += enemyY_change

    if ballY <= 0:
        ballY = 480
        ball_state = "ready"

    if ball_state == "fire":
        fire_ball(ballX, ballY)
        ballY -= ballY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()

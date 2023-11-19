import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")

playerImg = pygame.image.load('monster.png')
playerImgW = 50
playerImgH = 50
playerImg = pygame.transform.scale(playerImg, (playerImgW, playerImgH))
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


running = True
while running:
    screen.fill((2, 0, 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -.1
            elif event.key == pygame.K_RIGHT:
                playerX_change = .1
            elif event.key == pygame.K_UP:
                playerY_change = -.1
            elif event.key == pygame.K_DOWN:
                playerY_change = .1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change=0

    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()

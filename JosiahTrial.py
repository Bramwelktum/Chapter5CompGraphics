import pygame
from pygame import mixer

pygame.init()

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
mixer.music.load('Soundridemusic.wav')
mixer.music.play(-1)

pygame.display.set_caption("Snake Dash")

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 30)
textX = 20
textY = 20

game_over_font = pygame.font.Font('freesansbold.ttf', 50)

# MY PLAYER
playerImg = pygame.image.load('monster.png')
playerImgW = 30
playerImgH = 30
playerImg = pygame.transform.scale(playerImg, (playerImgW, playerImgH))
playerX = 10
playerY = 10
playerX_change = 0
playerY_change = 0

# BRICKS
brick_color = (255, 0, 0)
brick_width = 50
brick_height = 20
rows = 1
cols = 1
padding = 5
offset_x = 50
offset_y = 50


def player(x, y):
    screen.blit(playerImg, (x, y))


# def draw_bricks():
#

def game_over():
    over_text = game_over_font.render("GAME OVER!!", True, (255, 0, 0))
    screen.blit(over_text, (200, 250))


def start_menu():
    font = pygame.font.Font(None, 36)
    text = font.render("Press SPACE to start", True, pygame.Color('white'))
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False


def game_loop():
    global playerX_change, playerY_change, playerY, playerX
    running = True
    while running:
        screen.fill((2, 0, 128))

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

        player(playerX, playerY)

        pygame.display.update()


start_menu()
game_loop()
pygame.quit()

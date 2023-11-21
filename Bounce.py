import math
import random
import pygame
# import pygame_gui
from pygame.locals import K_F1, K_F2, K_F3
import ObstacleClass
from BounceBall import Ball
from CoinClass import Coin
from ObstacleClass import Obstacle

pygame.init()
pygame.mixer.init()

# Load and play the music
pygame.mixer.music.load(
    'BounceGameMusic/trapbeat.mp3')  # Replace 'path_to_your_music_file.mp3' with the actual file path
pygame.mixer.music.set_volume(0.2)  # Adjust the volume as needed
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

# GAME WINDOW
WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce Maze Game")

ground_img = pygame.image.load('BounceGamePhotos/ground.png')
ground_img = pygame.transform.scale(ground_img, (WIDTH, HEIGHT // 4))
ground_width = ground_img.get_width()
ground_height = ground_img.get_height()

# game variable
tiles = math.ceil((WIDTH / ground_width)) + 1
print(tiles)
scroll = 0



# Set up fonts
control_font = pygame.font.Font(None, 24)
start_font = pygame.font.Font(None, 36)
close_font = pygame.font.Font(None, 26)
pause_font = pygame.font.Font(None, 36)

# coins
coin_img = pygame.image.load("BounceGamePhotos/dollar.png")
# Set initial volume and volume step
volume = 0.5
volume_step = 0.1

# obstacles
obstacles = [300, 450, 600]
obstacles_speed = 2
active = True


def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def start_menu():
    draw_text("Press SPACE to start", start_font, pygame.Color('white'), WIDTH // 2, HEIGHT // 2)
    draw_text("Press q to close", close_font, pygame.Color('green'), WIDTH // 2, 550)
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
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()


def isCollision(object1X, object2X):
    distance = math.sqrt(math.pow((object1X - object2X), 2) + 0)
    if distance < 27:
        return True
    else:
        return False


def controls_menu():
    screen.fill((2, 125, 125))
    draw_text("Controls:", start_font, pygame.Color('white'), WIDTH // 2, HEIGHT // 6)
    # draw_text("LEFT ARROW: Move Left", control_font, pygame.Color('white'), WIDTH // 2, HEIGHT // 3)
    # draw_text("RIGHT ARROW: Move Right", control_font, pygame.Color('white'), WIDTH // 2, HEIGHT // 3 + 30)
    draw_text("UP ARROW: Jump", control_font, pygame.Color('white'), WIDTH // 2, HEIGHT // 3 + 60)
    draw_text("P: Pause/Unpause", control_font, pygame.Color('white'), WIDTH // 2, HEIGHT // 3 + 90)
    draw_text("Press SPACE to start the game", start_font, pygame.Color('white'), WIDTH // 2, HEIGHT - 100)
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


def onPause():
    controls_menu_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    controls_menu_surface.fill((0, 0, 0, 150))  # Set alpha value (transparency) to 150
    draw_text("Game Paused...", pause_font, pygame.Color('white'), WIDTH // 2, HEIGHT // 2)


def increase_volume():
    global volume
    volume = min(1.0, volume + volume_step)
    pygame.mixer.music.set_volume(volume)


def decrease_volume():
    global volume
    volume = max(0.0, volume - volume_step)
    pygame.mixer.music.set_volume(volume)


def mute_volume():
    pygame.mixer.music.set_volume(0.0)


def unmute_volume():
    pygame.mixer.music.set_volume(volume)


def check_volume_control():
    keys = pygame.key.get_pressed()
    if keys[K_F3]:
        increase_volume()
    elif keys[K_F2]:
        decrease_volume()
    elif keys[K_F1]:
        mute_volume()


def game_loop(scroll):
    global active
    running = True
    clock = pygame.time.Clock()

    ball = Ball()
    coin1 = Coin(coin_img)
    coin2 = Coin(coin_img)
    coin3 = Coin(coin_img)
    coin4 = Coin(coin_img)
    coin5 = Coin(coin_img)
    coinsList = [coin1, coin2, coin3, coin4, coin5]

    obstacle1 = Obstacle(300, 450, 100, 50)
    obstacle2 = Obstacle(350, 400, 50, 50)
    obstacle3 = Obstacle(400, 400, 100, 100)


    obstacleGroup1 = [obstacle1, obstacle2, obstacle3]
    obstacleGroup2 = [
        Obstacle(random.randint(600, 1200), 450, 100, 50),
        Obstacle(random.randint(600, 1200), 400, 50, 50),
        Obstacle(random.randint(600, 1200), 400, 100, 100)
    ]

    obstacleList = [obstacleGroup1, obstacleGroup2]

    jumping = False
    jump_count = 8
    scroll_change = 0
    coin_imgX_change = 0
    obstacleX_change = 0
    score_value = 0
    paused = False

    while running:
        screen.fill((2, 125, 125))
        screen.blit(ground_img, (0, 480))
        scroll += scroll_change


        score = control_font.render("Score :" + score_value.__str__(), True, (255, 0, 0))
        screen.blit(score, (10, 10))

        for coin in coinsList:
            coin.x += coin_imgX_change
            # check if ball and coin collide i.e coin is collected
            coinCollection = isCollision(coin.x, ball.x)
            if coinCollection:
                coin.x = random.randint(800, 1800)
                score_value += 1

        # for obstacleGroup in obstacleList:
        #     for obstacle in obstacleGroup:
        #         obstacle.x += obstacleX_change
        #         hitWallCollision = isCollision(obstacle.x, ball.x)
        #         if hitWallCollision:
        #             ball.x = obstacle.x

            for obstacle in obstacleGroup1:
                obstacle.x += obstacleX_change
                if obstacle.x < 1:
                    obstacle.x = random.randint(1000, 1200)
                hitWallCollision = isCollision(obstacle.x, ball.x)
                if hitWallCollision:
                    ball.x = obstacle.x


        for i in range(0, tiles):
            screen.blit(ground_img, (i * ground_width + scroll, 480))

        if abs(scroll) > ground_width:
            scroll = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ball.velocity[0] = -1
                elif event.key == pygame.K_RIGHT:
                    ball.velocity[0] = .5
                    if not paused:
                        scroll_change -= 10
                        coin_imgX_change -= 10
                        obstacleX_change -= 2
                elif event.key == pygame.K_UP and not jumping:
                    jumping = True
                elif event.key == pygame.K_p:
                    paused = not paused
                elif event.key == pygame.K_F3:
                    increase_volume()
                elif event.key == pygame.K_F2:
                    decrease_volume()
                elif event.key == pygame.K_F1:
                    mute_volume()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    ball.velocity[0] = 0
                    scroll_change = 0
                    coin_imgX_change = 0
                    obstacleX_change = 0
        check_volume_control()

        if not paused:
            if jumping:
                if jump_count >= -7:
                    neg = 1 if jump_count >= 0 else -1
                    ball.y -= (jump_count ** 2) * 0.5 * neg
                    jump_count -= 1
                else:
                    jumping = False
                    jump_count = 7

            ball.x += ball.velocity[0]
            ball.y += ball.velocity[1]
            ball.draw(screen)
            ball.ball_limits(WIDTH)

            coin1.draw(screen)
            coin2.draw(screen)
            coin3.draw(screen)
            coin4.draw(screen)
            coin5.draw(screen)

            # for obstacleGroup in obstacleList:
            #     for obstacle in obstacleGroup:
            #         obstacle.draw_obstacle(screen)
            obstacle1.draw_obstacle(screen)
            obstacle2.draw_obstacle(screen)
            obstacle3.draw_obstacle(screen)

        if paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F3:
                        increase_volume()
                    if event.key == pygame.K_F2:
                        decrease_volume()
                    if event.key == pygame.K_F1:
                        mute_volume()
                    if event.key == pygame.K_LEFT:
                        ball.velocity[0] = 0
                    elif event.key == pygame.K_RIGHT:
                        ball.velocity[0] = 0
                        scroll_change = 0
                    elif event.key == pygame.K_UP and not jumping:
                        jumping = False
            onPause()

        pygame.display.flip()
        clock.tick(60)


# Call start_menu, controls_menu, and game_loop
# start_menu()
# controls_menu()
game_loop(scroll)

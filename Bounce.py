import pygame

from BounceBall import Ball

pygame.init()

# GAME WINDOW
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce Maze Game")
ground_img = pygame.image.load('BounceGamePhotos/ground.png')
ground_img = pygame.transform.scale(ground_img, (WIDTH, HEIGHT // 4))

# Set up fonts
start_font = pygame.font.Font(None, 36)
close_font = pygame.font.Font(None, 26)
pause_font = pygame.font.Font(None, 36)


def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def start_menu():
    draw_text("Press SPACE to start", start_font, pygame.Color('white'), WIDTH // 2, HEIGHT // 2)
    draw_text("Press ESCAPE to close", close_font, pygame.Color('green'), 400, 550)
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
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()


def game_loop():
    running = True
    clock = pygame.time.Clock()

    ball = Ball()
    jumping = False
    jump_count = 7
    paused = False

    while running:
        screen.fill((2, 125, 125))
        screen.blit(ground_img, (0, 480))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ball.velocity[0] = -2
                elif event.key == pygame.K_RIGHT:
                    ball.velocity[0] = 2
                elif event.key == pygame.K_UP and not jumping:
                    jumping = True
                elif event.key == pygame.K_p:
                    paused = not paused
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    ball.velocity[0] = 0

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

        if paused:
            draw_text("Game Paused...", pause_font, pygame.Color('white'), WIDTH // 2, HEIGHT // 2)

        pygame.display.flip()
        clock.tick(60)


start_menu()
game_loop()
pygame.quit()

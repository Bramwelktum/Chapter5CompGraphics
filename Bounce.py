import pygame
import math

pygame.init()

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



# bg_images = []
# for i in range(1, 6):
#   bg_image = pygame.image.load(f"BounceGamePhotos/plx-{i}.png").convert_alpha()
#   bg_images.append(bg_image)
# bg_width = bg_images[0].get_width()
# def draw_bg():
#   for x in range(5):
#     speed = 1
#     for i in bg_images:
#       screen.blit(i, ((x * WIDTH) - scroll * speed, 0))
#       speed += 0.2

class Ball:
    def __init__(self):
        self.x = 40
        self.y = 480
        self.radius = 10
        self.color = pygame.Color('black')
        self.velocity = [0, 1]  # Adjust as needed

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def ball_limits(self):
        if self.y >= 480:
            self.y = 480
        if self.y <= 8:
            self.y = 8
        if self.x <= 8:
            self.x = 8
        if self.x > WIDTH - 8:
            self.x = WIDTH - 8


def start_menu():
    start_font = pygame.font.Font(None, 36)
    close_font = pygame.font.Font(None, 26)
    text_start = start_font.render("Press SPACE to start", True, pygame.Color('white'))
    text_close = close_font.render("Press ESCAPE to close", True, pygame.Color('red'))
    text_start_rect = text_start.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    text_close_rect = text_close.get_rect(center=(400, 550))
    screen.blit(text_start, text_start_rect)
    screen.blit(text_close, text_close_rect)
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



def game_loop(scroll):
    running = True
    clock = pygame.time.Clock()

    ball = Ball()
    # enemy = Enemy()
    jumping = False
    jump_count = 7
    scroll_change = 0

    while running:
        screen.fill((2, 125, 125))

        scroll += scroll_change
        for i in range(0, tiles):
            screen.blit(ground_img, (i * ground_width + scroll, 480))

        if abs(scroll) > ground_width:
            scroll = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle user input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ball.velocity[0] = -2
                elif event.key == pygame.K_RIGHT:
                    ball.velocity[0] = 2
                    scroll_change -= 10
                elif event.key == pygame.K_UP and not jumping:
                    jumping = True
                # elif event.key == pygame.K_DOWN:
                #     ball.velocity[1] = 2


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    ball.velocity[0] = 0
                    scroll_change = 0
                # elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                #     ball.velocity[1] = 0

        if jumping:
            if jump_count >= -7:
                neg = 1
                if jump_count < 0:
                    neg = -1
                ball.y -= (jump_count ** 2) * .5 * neg
                jump_count -= 1
            else:
                jumping = False
                jump_count = 7
        # Update ball position based on velocity
        ball.x += ball.velocity[0]
        ball.y += ball.velocity[1]

        # Draw everything

        ball.draw()
        # enemy.draw()
        # enemy.move()
        ball.ball_limits()
        pygame.display.flip()

        clock.tick(120)  # Adjust the frame rate as needed


start_menu()
game_loop(scroll)
pygame.quit()

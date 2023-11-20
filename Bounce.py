import pygame

pygame.init()

# GAME WINDOW
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce Maze Game")
ground_img = pygame.image.load('BounceGamePhotos/ground.png')
ground_img = pygame.transform.scale(ground_img, (WIDTH, HEIGHT // 4))


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


# Add this import at the beginning of your code
# enemy_img = pygame.image.load('BounceGamePhotos/enemy.jpg')
# enemy_img = pygame.transform.scale(enemy_img, (100, 100))
#
#
# class Enemy:
#     def __init__(self):
#         self.x = WIDTH - 60
#         self.y = 480
#         self.width = 50
#         self.height = 50
#         self.velocity = -2  # Adjust as needed
#
#     def draw(self):
#         screen.blit(enemy_img, (self.x, self.y))
#
#     def move(self):
#         self.x += self.velocity
#         if self.x <= 0 or self.x >= WIDTH - self.width:
#             self.velocity *= -1  # Reverse direction when hitting the window edges


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


def game_loop():
    running = True
    clock = pygame.time.Clock()

    ball = Ball()
    # enemy = Enemy()
    jumping = False
    jump_count = 7

    while running:
        screen.fill((2, 125, 125))
        screen.blit(ground_img, (0, 480))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # Handle user input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ball.velocity[0] = -2
                elif event.key == pygame.K_RIGHT:
                    ball.velocity[0] = 2
                elif event.key == pygame.K_UP and not jumping:
                    jumping = True
                # elif event.key == pygame.K_DOWN:
                #     ball.velocity[1] = 2


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    ball.velocity[0] = 0
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

        clock.tick(60)  # Adjust the frame rate as needed


start_menu()
game_loop()
pygame.quit()

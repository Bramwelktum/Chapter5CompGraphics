import pygame

pygame.init()

# GAME WINDOW
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce Maze Game")


class Ball:
    def __init__(self):
        self.x = 40
        self.y = 40
        self.radius = 8
        self.color = pygame.Color('blue')
        self.velocity = [0, 0]  # Adjust as needed

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Maze:
    def __init__(self):
        self.walls = []

    def draw(self):
        for wall in self.walls:
            pygame.draw.rect(win, pygame.Color('brown'), wall)


def start_menu():
    start_font = pygame.font.Font(None, 36)
    close_font = pygame.font.Font(None, 26)
    text_start = start_font.render("Press SPACE to start", True, pygame.Color('white'))
    text_close = close_font.render("Press ESCAPE to close", True, pygame.Color('red'))
    text_start_rect = text_start.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    text_close_rect = text_close.get_rect(center=(400, 550))
    win.blit(text_start, text_start_rect)
    win.blit(text_close, text_close_rect)
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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle user input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ball.velocity[0] = -2
                elif event.key == pygame.K_RIGHT:
                    ball.velocity[0] = 2
                elif event.key == pygame.K_UP:
                    ball.velocity[1] = -2
                elif event.key == pygame.K_DOWN:
                    ball.velocity[1] = 2


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    ball.velocity[0] = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    ball.velocity[1] = 0

        # Update ball position based on velocity
        ball.x += ball.velocity[0]
        ball.y += ball.velocity[1]

        # Draw everything
        win.fill(pygame.Color('white'))
        ball.draw()

        pygame.display.flip()

        clock.tick(60)  # Adjust the frame rate as needed


start_menu()
game_loop()
pygame.quit()

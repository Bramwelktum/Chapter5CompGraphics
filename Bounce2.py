import random

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
        self.color = pygame.Color('black')
        self.velocity = [0, 0]  # Adjust as needed

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Maze:
    def __init__(self):
        self.walls = []
        self.generate_maze()

    def draw(self):
        for wall in self.walls:
            pygame.draw.rect(win, pygame.Color('brown'), wall)

    def generate_maze(self):
        for x in range(0, WIDTH, 50):
            for y in range(0, HEIGHT, 50):
                # if y < HEIGHT - 40 or (x // 50) % 2 == (y // 50 + random.randint(0, 1)) % 2:
                #     # Add thick bricks for walls
                #     self.walls.append(pygame.Rect(x, y, 5, 10))
                # else:
                    # Add obstacles along the paths
                    obstacle_width = 10
                    obstacle_height = random.randint(10, 30)
                    obstacle_x = x + (50 - obstacle_width) // 2
                    obstacle_y = y + (50 - obstacle_height) // 2
                    self.walls.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))


def check_collision(ball, maze):
    for wall in maze.walls:
        if pygame.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2).colliderect(wall):
            ball.velocity[0] *= -1
            ball.velocity[1] *= -1


def start_menu():
    font = pygame.font.Font(None, 36)
    text = font.render("Press SPACE to start", True, pygame.Color('white'))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    win.blit(text, text_rect)
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
    running = True
    clock = pygame.time.Clock()

    ball = Ball()
    maze = Maze()

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

        check_collision(ball, maze)
        # Draw everything
        win.fill(pygame.Color('white'))
        maze.draw()
        ball.draw()

        pygame.display.flip()

        clock.tick(60)  # Adjust the frame rate as needed


start_menu()
game_loop()
pygame.quit()


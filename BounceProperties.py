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
        self.walls = [
            pygame.Rect(0, 0, 20, HEIGHT),  # Left border
            pygame.Rect(0, 0, WIDTH, 20),  # Top border
            pygame.Rect(WIDTH - 20, 0, 20, HEIGHT),  # Right border
            pygame.Rect(0, HEIGHT - 20, WIDTH, 20),  # Bottom border
            pygame.Rect(50, 50, 50, 10),
            pygame.Rect(50, 50, 10, 100),
            pygame.Rect(100, 300, 200, 20),
            pygame.Rect(400, 100, 20, 200),
            pygame.Rect(200, 400, 200, 20),
            pygame.Rect(500, 300, 20, 200),
            pygame.Rect(400, 400, 200, 20),
            pygame.Rect(100, 500, 20, 100),
            pygame.Rect(300, 500, 400, 20),
            pygame.Rect(500, 100, 20, 200)
        ]

    def draw(self):
        for wall in self.walls:
            pygame.draw.rect(win, pygame.Color('blue'), wall)


def check_collision(ball, maze):
    for wall in maze.walls:
        if pygame.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2).colliderect(wall):
            ball.velocity[0] *= -1
            ball.velocity[1] *= -1


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

pygame.quit()

import pygame


class Ball:
    def __init__(self):
        self.x = 100
        self.y = 480
        self.radius = 20
        self.color = pygame.Color('black')
        self.velocity = [0, 1]  # Adjust as needed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def ball_limits(self, WIDTH):
        if self.y >= 480:
            self.y = 480
        if self.y <= 8:
            self.y = 8
        if self.x <= 8:
            self.x = 8
        if self.x > WIDTH - WIDTH // 4:
            self.x = WIDTH - WIDTH // 4

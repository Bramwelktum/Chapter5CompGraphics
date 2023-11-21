import random


class Coin:
    def __init__(self, coinimg):
        self.x = random.randint(800, 1800)
        self.y = 470
        self.coin_img = coinimg

    def draw(self, screen):
        screen.blit(self.coin_img,(self.x, self.y))

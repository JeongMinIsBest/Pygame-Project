import pygame
import sys
import random

class Bird:
    def __init__(self, screen, bird_image, initial_x, initial_y, speed, jump_height, gravity):
        self.screen = screen
        self.image = bird_image
        self.width = 50
        self.height = 35
        self.x = initial_x
        self.y = initial_y
        self.speed = speed
        self.jump_height = jump_height
        self.gravity = gravity

    def update(self):
        self.speed += self.gravity
        self.y += self.speed
        self.screen.blit(self.image, (self.x, self.y))

class Obstacle:
    def __init__(self, screen, width, speed, gap):
        self.screen = screen
        self.width = width
        self.speed = speed
        self.gap = gap
        self.height = random.randint(150, 400)
        self.x = screen.get_width()
        self.y = screen.get_height() - self.height

    def update(self):
        self.x -= self.speed
        pygame.draw.rect(self.screen, (0, 255, 0), [self.x, 0, self.width, self.y])
        pygame.draw.rect(self.screen, (0, 255, 0), [self.x, self.y + self.gap, self.width, self.screen.get_height() - self.y - self.gap])

class FlappyBirdGame:
    def __init__(self):
        pygame.init()

        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Flappy Bird")

        self.bird_image = pygame.image.load("C:\\Users\\ljm16\\Desktop\\Python\\Pygame\\Flappy Bird\\parrot.png")
        self.bird = Bird(self.screen, self.bird_image, self.width // 3, self.height // 2, 5, 10, 1)

        self.obstacle_width = 70
        self.obstacle_speed = 5
        self.obstacle_gap = 150
        self.obstacle = Obstacle(self.screen, self.obstacle_width, self.obstacle_speed, self.obstacle_gap)

        self.font = pygame.font.SysFont(None, 55)
        self.clock = pygame.time.Clock()
        self.score = 0

    def display_score(self):
        score_text = self.font.render(" Score : " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score_text, [10, 10])

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.speed = -self.bird.jump_height

            self.bird.update()
            self.obstacle.update()

            if (
                self.bird.y < 0
                or self.bird.y + self.bird.height > self.height
                or (self.obstacle.x < self.bird.x + self.bird.width and
                    self.obstacle.x + self.obstacle.width > self.bird.x and
                    (self.bird.y < self.obstacle.y or
                     self.bird.y + self.bird.height > self.obstacle.y + self.obstacle.gap))
            ):
                pygame.quit()
                sys.exit()

            if self.obstacle.x + self.obstacle.width < self.bird.x:
                self.score += 1
                self.obstacle.x = self.width
                self.obstacle.height = random.randint(150, 400)
                self.obstacle.y = self.height - self.obstacle.height

            self.screen.fill((0, 0, 0))
            self.bird.update() # 추가해주기
            self.obstacle.update() # 추가해주기
            self.display_score()

            pygame.display.flip()
            self.clock.tick(30)

flappy_bird_game = FlappyBirdGame()
flappy_bird_game.game_loop()

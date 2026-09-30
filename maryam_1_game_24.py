import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 750))
pygame.display.set_caption("project 1 m")

running = True
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

speed  = 8

class MaryamShapes:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

class Apple(MaryamShapes):
    def __init__(self, x, y, color, radius, speed):
        super().__init__(x, y, color)
        self.radius = radius
        self.speed = speed

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        pygame.draw.ellipse(surface, (0, 200, 0),
                            (self.x - 5, self.y - self.radius - 8, 10, 6))
        pygame.draw.line(surface, (139, 69, 19),
                         (self.x, self.y - self.radius),
                         (self.x, self.y - self.radius - 8), 2)

    def move(self):
        self.y += self.speed

    def reset(self):
        self.y = 50
        self.x = random.randint(20, 480)

class Basket(MaryamShapes):
    def __init__(self, x, y, color, width, height, speed):
        super().__init__(x, y, color)
        self.width = width
        self.height = height
        self.speed = speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        step = 15
        for i in range(0, self.width, step):
            pygame.draw.line(surface, (139, 69, 19),
                             (self.x + i, self.y + self.height),
                             (self.x + i + step, self.y), 2)
            pygame.draw.line(surface, (139, 69, 19),
                             (self.x + i, self.y),
                             (self.x + i + step, self.y + self.height), 2)

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed

    def move_right(self):
        if self.x < 500 - self.width:
            self.x += self.speed

while True:
    screen.fill((255,255,255))
    text = font.render("which level ? 1 or 2 or 3?" , True , (0,0,0))
    screen.blit(text , (98,340))
    pygame . display . flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                speed = 5
            elif event.key == pygame.K_2:
                speed = 8
            elif event.key == pygame.K_3:
                speed = 10
            break
    else:
        continue
    break

apple = Apple(random.randint(10, 490), 50, (220, 20, 60), 15, speed)
basket = Basket(150, 700, (245, 222, 179), 150, 25, 5)

score = 0
missed = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket.move_left()
    if keys[pygame.K_RIGHT]:
        basket.move_right()

    screen.fill((135,206,235))

    apple.move()

    if (basket.x < apple.x < basket.x + basket.width and
        basket.y < apple.y < basket.y + basket.height):
        score += 1
        apple.reset()

    elif apple.y + apple.radius > 750:
        missed += 1
        apple.reset()

    apple.draw(screen)
    basket.draw(screen)

    text = font.render("your score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    text_2 = font.render("missed balls: " + str(missed), True, (255, 255, 255))
    screen.blit(text_2, (10, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
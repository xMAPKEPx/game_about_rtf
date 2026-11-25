import pygame

GROUND_Y = 500

class PlayerModel:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = 5

        # Параметры для прыжка и гравитации
        self.vel_y = 0
        self.gravity = 0.8
        self.jump_power = -15
        self.on_ground = False

    def jump(self):
        if self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

    def update(self, dx, walls, platforms):
        # 1. Горизонтальное движение
        self.rect.x += dx * self.speed

        for wall in walls:
            if self.rect.colliderect(wall):
                if dx > 0:
                    self.rect.right = wall.left
                elif dx < 0:
                    self.rect.left = wall.right

        # 2. Вертикальное движение (гравитация)
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # 3. Проверка столкновения с полом
        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.vel_y = 0
            self.on_ground = True

        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.vel_y > 0:
                    self.rect.bottom = platform.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = platform.bottom
                    self.vel_y = 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

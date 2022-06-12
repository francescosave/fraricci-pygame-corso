from .component import Component
import pygame

class StaticSpriteComponent(Component):
    def __init__(self, item, boundingRect):
        self.assetFileName = item.get("name") + ".png"
        self.image = None
        self.x = item.get("x")
        self.y = item.get("y")
        self.vx = item.get("vx")
        self.vy = item.get("vy")
        self.boundingRect = boundingRect

    def load(self):
        self.image = pygame.image.load(self.assetFileName)

    def render(self, surface):
        rect = self.image.get_rect()
        rect.centerx = self.x
        rect.centery = self.y
        surface.blit(self.image, rect)

    def update(self):
        self.x += self.vx
        self.y += self.vy

        # bounce on the x axis
        if self.x < 0 or self.x > self.boundingRect.width:
            self.vx = -self.vx
        
        # bounce on the y axis
        if self.y < 0 or self.y > self.boundingRect.height:
            self.vy = -self.vy

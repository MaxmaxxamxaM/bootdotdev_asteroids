from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH
import pygame  # type: ignore

class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = 0

    def draw(self, screen: pygame.Surface) -> None:
        center = self.position
        radius = self.radius
        pygame.draw.circle(screen, "white", center, radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity


class EnemyShot(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

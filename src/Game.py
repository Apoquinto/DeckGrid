import sys, pygame

from Config import Config

class Game():
    """Main controller of the game.
    Initialize everything necessary for the proper functioning of the game.

    ...

    Attributes
    ----------
    config : Config
        essential configurations for the start of the game.
    """
    def __init__(self, config: Config) -> None:
        screenSize: tuple[int] = config.screenSize
        self.screen = pygame.display.set_mode(screenSize)
        self.clock = pygame.time.Clock()

    def _render(self):
        self.screen.fill('black')

    def init(self) -> None:
        pygame.init()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self._render()

            self.clock.tick(60)
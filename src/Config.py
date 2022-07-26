class Config:
    """Class that includes the essential configurations for the start of the game.

    ...

    Attributes
    ----------
    screenSize : tuple[int]
        size of the screen in pixeles
    """
    def __init__(self, screenSize: tuple[int]) -> None:
        self._screenSize = screenSize

    @property
    def screenSize(self):
        return self._screenSize

    @screenSize.setter
    def screenSize(self, screenSize):
        self._screenSize = screenSize
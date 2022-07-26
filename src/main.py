from Config import Config
from Game import Game


def main():
    configuration: Config = Config([400, 400])
    game: Game = Game(configuration)
    game.init()

if __name__ == '__main__':
    main()
from models.game import Game
from models.playground import Playground
from datetime import date


class GamesDataAccessor:

    def store_game(self, game: Game):
        pass

    def get_games(self, play_date: date, time_range: (str, str), playground: Playground = None):
        pass

    def update_game(self, game: Game):
        pass

    def delete_game(self, game: Game):
        pass

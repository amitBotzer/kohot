from models.playground import Playground
from models.player import Player


class InvalidPlaytimeException(Exception):
    """Raised when the playground is closed at the specified time"""
    pass


class PlayerIsAlreadyInException(Exception):
    """Raised when the player added is already in the game"""
    pass


class PlayerNotFoundException(Exception):
    """Raised when the player removed isn't in the game"""
    pass


class Game:

    def __init__(self, playground: Playground, playtime: (str, str), players: list = []):
        if not playground.is_open_at_range(playtime):
            raise InvalidPlaytimeException()
        self._playground = playground
        self._playtime = playtime
        self._players = players

    def change_playground(self, new_playground: Playground):
        if not new_playground.is_open_at_range(self._playtime):
            raise InvalidPlaytimeException()
        self._playground = new_playground

    def change_playtime(self, new_playtime: (str, str)):
        if not self._playground.is_open_at_range(new_playtime):
            raise InvalidPlaytimeException()
        self._playtime = new_playtime

    def add_new_player(self, new_player: Player):
        if new_player in self._players:
            raise PlayerIsAlreadyInException()
        self._players.append(new_player)

    def remove_player(self, player: Player):
        if player not in self._players:
            raise PlayerNotFoundException()
        self._players.remove(player)

    def get_playground(self):
        return self._playground

    def get_playtime(self):
        return self._playtime

    def get_players(self):
        return self._players

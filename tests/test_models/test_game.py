import unittest
import datetime

from models.game import Game
from models.playground import Playground
from models.player import Player
from models.game import InvalidPlaytimeException


class TestGame(unittest.TestCase):

    def setUp(self) -> None:
        self.playground_a = Playground(name='Ramot Sapir', address='Gotel Levin 1, Haifa, Israel',
                                       location=(32.783800, 35.004821),
                                       opening_hours=[('0800', '1400'), ('1600', '2200')])
        self.playground_b = Playground(name='Gan Daniel', address='HaShikma 3, Haifa, Israel',
                                       location=(32.786935, 34.994653),
                                       opening_hours=[('0800', '2359')])
        self.players = [Player('botzer', 'Amit Botzer', datetime.datetime(1992, 12, 13), 'Haifa'),
                        Player('botzer92', 'Michael Botzer', datetime.datetime(1992, 12, 13), 'Haifa')]

    def test_change_playground_doesnt_accept_invalid_time(self):
        """
        playtime ('2200', '2359') is valid in the original playground but isn't valid in the new one.
        """
        game = Game(playground=self.playground_b, playtime=('2200', '2359'), players=self.players)
        self.assertRaises(InvalidPlaytimeException, lambda: game.change_playground(self.playground_a))

    def test_change_playground_accepts_valid_time(self):
        """
        playtime ('2000', '2200') is valid in both playgrounds
        """
        game = Game(playground=self.playground_a, playtime=('2000', '2200'), players=self.players)
        game.change_playground(self.playground_b)
        self.assertEqual(game.get_playground(), self.playground_b)

    def test_change_playime_rejects_too_late_time(self):
        """
        playtime ('2200', '2359') isn't valid in the playground of this game
        """
        game = Game(playground=self.playground_a, playtime=('2000', '2200'), players=self.players)
        self.assertRaises(InvalidPlaytimeException, lambda: game.change_playtime(new_playtime=('2200', '2359')))

    def test_change_playime_rejects_too_early_time(self):
        """
        playtime ('0600', '0800') isn't valid in the playground of this game
        """
        game = Game(playground=self.playground_a, playtime=('2000', '2200'), players=self.players)
        self.assertRaises(InvalidPlaytimeException, lambda: game.change_playtime(new_playtime=('0600', '0800')))

    def test_change_playime_accepts_valid_time(self):
        """
        playtime ('1600', '1800') is fine
        """
        game = Game(playground=self.playground_a, playtime=('2000', '2200'), players=self.players)
        game.change_playtime(new_playtime=('1600', '1800'))
        self.assertEqual(game.get_playtime(), ('1600', '1800'))

"""
    def add_new_player(self, new_player: Player):
        if new_player in self._players:
            raise PlayerIsAlreadyInException()
        self._players.append(new_player)

    def remove_player(self, player: Player):
        if player not in self._players:
            raise PlayerNotFoundException()
        self._players.remove(player)
"""
import unittest
import datetime

from models.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        date_of_birth = datetime.datetime(1992, 12, 13)
        self.player = Player('abotzer', 'Amit Botzer', date_of_birth, 'Haifa, Israel')

    def test_get_age(self):
        players_age = self.player.get_age()
        self.assertEqual(players_age, 27)

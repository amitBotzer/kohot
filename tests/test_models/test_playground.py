import unittest

from models.playground import Playground


class TestPlayground(unittest.TestCase):

    def setUp(self) -> None:
        self.pg = Playground(name='Ramot Sapir', address='Gotel Levin 1, Haifa, Israel',
                             location=(32.783800, 35.004821), opening_hours=[('0800', '1400'), ('1600', '2200')])

    def test_is_open_at_closing_time(self):
        self.assertEqual(False, self.pg.is_open_at('2300'))

    def test_is_open_at_opening_time(self):
        self.assertEqual(True, self.pg.is_open_at('1800'))
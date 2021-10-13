import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):

        self.card_game = CardGame()
        card_1 = Card("clubs", 2)
        card_2 = Card("diamonds", 1)
        card_3 = Card("spades", 5)
        card_4 = Card("hearts", 8)

        self.card_set = [card_1, card_2, card_3, card_4]

    def test_check_for_ace_true(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card_set[1]))

    def test_check_for_ace_false(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card_set[2]))
    
    def test_highest_card(self):
        first_card = self.card_set[0]
        second_card = self.card_set[1]
        self.assertEqual(second_card, self.card_game.highest_card(first_card, second_card))

    def test_cards_total(self):
        self.assertEqual('You have a total of 16', self.card_game.cards_total(self.card_set))

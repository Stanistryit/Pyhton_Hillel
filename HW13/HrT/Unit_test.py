import unittest
from unittest.mock import patch
from heads_or_tails import Person, InputData, InputBotData, Game, Logging

class TestPersonClass(unittest.TestCase):
    def test_deposit_property(self):
        person = Person("John", 1000)
        self.assertEqual(person.deposit, 1000)

class TestInputDataClass(unittest.TestCase):
    @patch('builtins.input', side_effect=['O', '20'])
    def test_get_player_input(self, mock_input):
        input_data = InputData("John", 100)
        choice, bet = input_data.get_player_input()
        self.assertEqual(choice, 'O')
        self.assertEqual(bet, 20)

class TestInputBotDataClass(unittest.TestCase):
    def test_generate_bot_input(self):
        input_bot_data = InputBotData("John", "Bot1")
        input_bot_data.deposit = 50
        bot_choice, bot_bet = input_bot_data.generate_bot_input(20)
        self.assertIn(bot_choice, ['O', 'R'])
        self.assertEqual(bot_bet, 20)


class TestGameClass(unittest.TestCase):
    def test_flip_coin(self):
        game = Game(None, None)
        game.flip_coin()
        self.assertIn(game.coin_side, ['O', 'R'])


class TestLoggingClass(unittest.TestCase):
    def test_add_game_info(self):
        logging = Logging()
        logging.add_game_info({'round': 1, 'real_player': {}, 'bot_players': [], 'coin_side': 'O', 'winners': []})
        self.assertEqual(len(logging.data), 1)

if __name__ == '__main__':
    unittest.main()

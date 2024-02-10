import json
import random
import logging
from abc import ABC, abstractmethod

# Налаштування логування для запису у файл
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='game_log.txt',
                    filemode='w')

random.seed(19)

class Observer(ABC):
    @abstractmethod
    def update(self, subject) -> None:
        pass

class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

class Person(Observer):
    def __init__(self, name, deposit, is_bot=False):
        self.name = name
        self.deposit = deposit
        self.is_bot = is_bot
        self.choice = None
        self.won_last_round = False
        self.bet = 0

    def update(self, subject) -> None:
        if subject.coin_side and self.choice == subject.coin_side:
            self.deposit += (subject.shared_pool / len(subject.winners)) - self.bet
            self.won_last_round = self.is_bot
        else:
            self.deposit -= self.bet
            self.won_last_round = False

    def get_input(self):
        if not self.is_bot:
            return self.get_player_input()
        return self.get_bot_input()

    def get_player_input(self):
        choice = input(f"Choose Heads (H) or Tails (T), {self.name}: ").upper()
        while choice not in ["H", "T"]:
            print("Invalid choice. Please choose Heads (H) or Tails (T).")
            choice = input(f"Choose Heads (H) or Tails (T), {self.name}: ").upper()

        bet = float(input(f"Enter your bet, {self.name} (Available: {round(self.deposit, 2)}): "))
        while bet <= 0 or bet > self.deposit:
            print("Invalid bet. Try again.")
            bet = float(input(f"Enter your bet, {self.name} (Available: {round(self.deposit, 2)}): "))

        return choice, bet

    def get_bot_input(self):
        if self.choice is None or self.won_last_round:
            self.choice = random.choice(["H", "T"]) if self.choice is None else ("H" if self.choice == "T" else "T")
        self.bet = min(10, self.deposit)
        return self.choice, self.bet

    @staticmethod
    def load_players(filename="players.json"):
        with open(filename, "r") as file:
            data = json.load(file)
            real_player_data = data["real_player"]
            real_player = Person(real_player_data["name"], real_player_data["deposit"])

            bot_players_data = data["bots"]
            bot_players = [Person(bot["name"], bot["deposit"], is_bot=True) for bot in bot_players_data]

            return real_player, bot_players

class Game(Subject):
    def __init__(self, real_player, bot_players):
        super().__init__()
        self.real_player = real_player
        self.bot_players = bot_players
        self.attach(real_player)
        for bot in bot_players:
            self.attach(bot)
        self.coin_side = None
        self.shared_pool = 0.0
        self.winners = []

    def flip_coin(self):
        self.coin_side = random.choice(["H", "T"])
        print(f"Coin flipped: {'Heads' if self.coin_side == 'H' else 'Tails'}")
        logging.info(f"Coin flipped: {'Heads' if self.coin_side == 'H' else 'Tails'}")

    def play_round(self):
        total_bets = 0

        player_choice, player_bet = self.real_player.get_input()
        print(f"Player {self.real_player.name} bets {player_bet} on {'Heads' if player_choice == 'H' else 'Tails'}")
        logging.info(f"Player {self.real_player.name} bets {player_bet} on {'Heads' if player_choice == 'H' else 'Tails'}")
        self.real_player.choice = player_choice
        self.real_player.bet = player_bet
        total_bets += player_bet

        for bot in self.bot_players:
            bot_choice, bot_bet = bot.get_input()
            print(f"Bot {bot.name} bets {bot_bet} on {'Heads' if bot_choice == 'H' else 'Tails'}")
            logging.info(f"Bot {bot.name} bets {bot_bet} on {'Heads' if bot_choice == 'H' else 'Tails'}")
            bot.choice = bot_choice
            bot.bet = bot_bet
            total_bets += bot_bet

        self.shared_pool = total_bets
        self.flip_coin()

        self.winners = [player for player in [self.real_player] + self.bot_players if player.choice == self.coin_side]
        winner_names = ', '.join([winner.name for winner in self.winners])
        print(f"Round winners: {winner_names}")
        logging.info(f"Round winners: {winner_names}")

        self.notify()

def main():
    real_player, bot_players = Person.load_players()
    game = Game(real_player, bot_players)

    num_rounds = 1
    for _ in range(num_rounds):
        game.play_round()
        print(f"Outcome: {game.coin_side}")
        for player in [real_player] + bot_players:
            print(f"{player.name}: Deposit - {player.deposit}")

if __name__ == "__main__":
    main()

import random
import logging
from abc import ABC, abstractmethod

# Налаштування логування
logging.basicConfig(level=logging.INFO, filename='game.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

STANDARD_BET = 10

class AbstractMediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str) -> None:
        pass

class Mediator(AbstractMediator):
    def __init__(self, game, accounter):
        self.game = game
        self.accounter = accounter
        self.players = {}

    def attach(self, player):
        self.players[player.name] = player

    def detach(self, name):
        del self.players[name]

    def notify(self, sender: object, event: str):
        if event == "round_finished":
            self.accounter.calc_balances(self.players.values(), self.game.result)

class AbstractAccounter(ABC):
    @abstractmethod
    def calc_balances(self, players, result):
        pass

class Accounter(AbstractAccounter):
    def calc_balances(self, players, result):
        for player in players:
            player.calculate_balance(result)

class Game:
    def __init__(self, mediator: Mediator):
        self.mediator = mediator
        self.result = None

    def request_bets(self):
        for player in self.mediator.players.values():
            player.make_bet()

    def play_round(self):
        self.request_bets()
        self.result = random.choice([1, 0])
        self.mediator.notify(self, "round_finished")

class AbstractPlayer(ABC):
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    @abstractmethod
    def calculate_balance(self, result):
        pass

    @abstractmethod
    def make_bet(self):
        pass

    @property
    def balance(self):
        return self._balance

class RealPlayer(AbstractPlayer):
    def calculate_balance(self, result):
        if (result == 1 and self.bet_choice == 'H') or (result == 0 and self.bet_choice == 'T'):
            self._balance += self.bet_amount
        else:
            self._balance -= self.bet_amount
        logging.info(f"{self.name} now has balance: {self._balance}")

    def make_bet(self):
        try:
            self.bet_amount = float(input(f"{self.name}, enter your bet amount: "))
            if self.bet_amount <= 0 or self.bet_amount > self._balance:
                raise ValueError("Invalid bet amount.")
        except ValueError as e:
            print(e)
            return self.make_bet()

        self.bet_choice = input(f"{self.name}, choose Heads (H) or Tails (T): ").upper()
        if self.bet_choice not in ["H", "T"]:
            print("Invalid choice. Please choose Heads (H) or Tails (T).")
            return self.make_bet()

class DummyBot(AbstractPlayer):
    def calculate_balance(self, result):
        if (result == 1 and self.bet_choice == 'H') or (result == 0 and self.bet_choice == 'T'):
            self._balance += self.bet_amount
        else:
            self._balance -= self.bet_amount
        logging.info(f"{self.name} now has balance: {self._balance}")

    def make_bet(self):
        self.bet_amount = random.randint(1, STANDARD_BET)
        self.bet_choice = random.choice(['H', 'T'])

if __name__ == "__main__":
    game = Game(None)
    accounter = Accounter()
    mediator = Mediator(game, accounter)
    game.mediator = mediator

    real_player = RealPlayer("Player", 100)
    bots = [DummyBot(f"Bot{i}", 100) for i in range(1, 4)]

    mediator.attach(real_player)
    for bot in bots:
        mediator.attach(bot)

    for i in range(5):  # Play 5 rounds
        print(f"\nStarting round {i + 1}")
        game.play_round()
        print(f"Coin result: {'Heads' if game.result == 1 else 'Tails'}")
        print(f"{real_player.name}'s new balance: {real_player.balance}")
        for bot in bots:
            print(f"{bot.name}'s new balance: {bot.balance}")

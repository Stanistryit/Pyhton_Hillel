import random

# SubjectState
class CoinTossResult:
    def __init__(self, side):
        self.side = side

# Базовий клас гравця
class Player:
    def __init__(self, name, deposit):
        self.name = name
        self.deposit = deposit
        self.game = None
        self.choice = None
        self.bet = 0

    def make_choice(self):
        pass

    def make_bet(self):
        pass

    def update(self, result):
        pass

    def receive_prize(self, prize):
        self.deposit += prize
        logger.info(f"{self.name}, you won {prize}! Your new deposit is {self.deposit}.")

# Перероблений клас BotPlayer
class BotPlayer(Player):
    def __init__(self, name, deposit, tactic):
        super().__init__(name, deposit)
        self.tactic = tactic  # Залежність на тактику

    def make_choice(self):
        self.choice = self.tactic.choose_side()

    def make_bet(self):
        self.bet = self.tactic.choose_bet()

# Клас для представлення тактики бота
class BotTactic:
    def choose_side(self):
        pass

    def choose_bet(self):
        pass

# Реалізація стратегії для RealPlayer
class RealPlayerStrategy:
    def apply_strategy(self, player, result):
        # Реалізація стратегії для реального гравця
        pass

# Subject
class CoinTossGame:
    def __init__(self):
        self.players = []
        self.prize_pool = 0

    def add_player(self, player):
        self.players.append(player)
        player.game = self

    def remove_player(self, player):
        self.players.remove(player)
        player.game = None

    def notify_observers(self, result):
        for player in self.players:
            player.update(result)

    def distribute_prizes(self, winners):
        total_prize = self.prize_pool
        prize_per_winner = total_prize / len(winners)

        for winner in winners:
            winner.receive_prize(prize_per_winner)

    def choose_winners(self, side):
        return [player for player in self.players if player.choice == side]

    def reset_choices_and_bets(self):
        for player in self.players:
            player.choice = None
            player.bet = 0

    def clear_players(self):
        self.players.clear()

    def play_game(self):
        side = random.choice(['Heads', 'Tails'])
        result = CoinTossResult(side)
        self.notify_observers(result)

        winners = self.choose_winners(side)

        if winners:
            self.distribute_prizes(winners)

        self.reset_choices_and_bets()
        self.clear_players()


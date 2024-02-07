import json
import random
import logging

from abc import ABC, abstractmethod

class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, event):
        for observer in self._observers:
            observer.update(event)

class Observer(ABC):
    @abstractmethod
    def update(self, event):
        pass

class GameObserver(Observer):
    def update(self, event):
        logging.info(f"Спостерігач: Отримав подію - {event}")

class Player:
    def __init__(self, name, deposit):
        self.name = name
        self.deposit = deposit

    @staticmethod
    def load_players(filename="players.json"):
        with open(filename, "r") as file:
            data = json.load(file)
            real_player_data = data["real_player"]
            real_player = Player(real_player_data["name"], real_player_data["deposit"])

            bot_players_data = data["bots"]
            bot_players = [Player(bot["name"], bot["deposit"]) for bot in bot_players_data]

            return real_player, bot_players

class InputData:
    def __init__(self, player_name, deposit=None):
        self.player_name = player_name
        self.deposit = deposit

    def get_player_input(self):
        choice = input(f"Оберіть орла (O) чи решку (R), {self.player_name}: ").upper()
        while choice not in ["O", "R"]:
            logging.error("Невірний вибір. Будь ласка, оберіть орла (O) чи решку (R).")
            choice = input(f"Оберіть орла (O) чи решку (R), {self.player_name}: ").upper()

        bet = float(input(
            f"Введіть свою ставку, {self.player_name} (Доступно вам: {round(self.deposit, 0)}): "))
        while bet <= 0 or bet > self.deposit:
            logging.error("Невірна ставка. Спробуйте знову.")
            bet = float(input(
                f"Введіть свою ставку, {self.player_name} (Доступно вам: {round(self.deposit, 0)}): "))

        return choice, bet

class InputBotData:
    def __init__(self, player_name, bot_name):
        self.player_name = player_name
        self.bot_name = bot_name

    def generate_bot_input(self, player_bet):
        choices = ["O", "R"]
        bot_choice = random.choice(choices)

        bot_bet = min(player_bet, self.deposit)
        return bot_choice, bot_bet

class Game(Subject):
    def __init__(self, real_player, bot_players):
        super().__init__()
        self.real_player = real_player
        self.bot_players = bot_players
        self.coin_side = None
        self.shared_pool = 0.0
        self.logging = logging.getLogger("game_logger")
        self.logging.setLevel(logging.INFO)
        file_handler = logging.FileHandler("game_history.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        self.logging.addHandler(file_handler)

    def attach_observer(self, observer):
        self.attach(observer)

    def detach_observer(self, observer):
        self.detach(observer)

    def notify_observers(self, event):
        self.notify(event)

    def flip_coin(self):
        sides = ["O", "R"]
        self.coin_side = random.choice(sides)

    def play_round(self):
        real_input = InputData(self.real_player.name, self.real_player.deposit)
        real_player_choice, real_player_bet = real_input.get_player_input()

        bot_bets = {}
        total_bets = real_player_bet

        bot_bets[self.real_player.name] = {"choice": real_player_choice, "bet": real_player_bet}

        for bot in self.bot_players:
            bot_input = InputBotData(bot.name, bot.name)
            bot_input.deposit = bot.deposit
            bot_choice, bot_bet = bot_input.generate_bot_input(real_player_bet)
            bot_bets[bot.name] = {"choice": bot_choice, "bet": bot_bet}
            total_bets += bot_bet

        self.flip_coin()

        print(f"\nМонетка підкинута, вона випала на {self.coin_side} сторону!")

        winners = []
        for player in [self.real_player] + self.bot_players:
            if player.name == self.real_player.name:
                choice = real_player_choice
            else:
                choice = bot_bets[player.name]["choice"]

            if choice == self.coin_side:
                winners.append(player)

        if winners:
            print("\nПереможці:")
            prize = total_bets / len(winners)
            for winner in winners:
                print(f"{winner.name} з вибором {self.coin_side} та виграє {round(prize, 0)}")
                winner.deposit += prize

        for player in [self.real_player] + self.bot_players:
            player.deposit -= bot_bets[player.name]["bet"]

        self.shared_pool = 0.0

        self.log_round_info(winners, real_player_choice, real_player_bet, bot_bets)

    def log_round_info(self, winners, real_player_choice, real_player_bet, bot_bets):
        round_info = {
            "round": len(self.logging.handlers[0].baseFilename) + 1,
            "real_player": {
                "name": self.real_player.name,
                "choice": real_player_choice,
                "bet": real_player_bet,
                "deposit": self.real_player.deposit,
            },
            "bot_players": [],
        }

        for bot in self.bot_players:
            bot_choice = bot_bets[bot.name]["choice"]
            bot_bet = bot_bets[bot.name]["bet"]
            round_info["bot_players"].append({
                "name": bot.name,
                "choice": bot_choice,
                "bet": bot_bet,
                "deposit": bot.deposit,
            })

        round_info["coin_side"] = self.coin_side
        round_info["winners"] = [winner.name for winner in winners]

        self.logging.info(json.dumps(round_info))

    def start_game(self, num_rounds=1):
        for round_num in range(1, num_rounds + 1):
            print(f"\nРаунд {round_num} з {num_rounds}")
            self.play_round()
            print("\nДепозити гравців:")
            print(f"{self.real_player.name}: {round(self.real_player.deposit, 0)}")
            for bot in self.bot_players:
                print(f"{bot.name}: {round(bot.deposit, 0)}")

# Почнемо гру
real_player, bot_players = Player.load_players()

print(f"Реальний ігрок: {real_player.name}, Депозит: {real_player.deposit}")
print("Гравці-Боти:")
for bot in bot_players:
    print(f"{bot.name}, Депозит: {bot.deposit}")

game_instance = Game(real_player, bot_players)
game_observer = GameObserver()
game_instance.attach_observer(game_observer)

rounds = 1  # Кількість раундів
game_instance.start_game(rounds)

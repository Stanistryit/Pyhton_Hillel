import random
import json
import logging

random.seed(1)


class Players:
    def __init__(self, json_file):
        self.json_file = json_file
        self.players_data = self.load_players(json_file)

    def load_players(self, json_file):
        with open(json_file, 'r') as file:
            return json.load(file)


class RealPlayer(Players):
    def __init__(self, json_file):
        super().__init__(json_file)
        player_data = self.players_data['real_player']
        self.name = player_data['name']
        self.deposit = player_data['deposit']

    def make_bet(self):
        while True:
            try:
                bet = float(input(f"{self.name}, введіть вашу ставку: "))
                if bet > self.deposit:
                    raise ValueError("Ставка перевищує депозит гравця")
                self.deposit -= bet
                return bet
            except ValueError:
                print("Неправильні дані. Будь ласка, введіть число.")

    def make_choice(self):
        choice = ''
        while choice not in ['Орел', 'Решка']:
            choice = input(f"{self.name}, оберіть Орел чи Решка(Орел\Решка): ")
        return choice


class Bot(Players):
    def __init__(self, json_file):
        super().__init__(json_file)
        bot_data = self.players_data['bots']
        self.name = bot_data['name']
        self.deposit = bot_data['deposit']
    def make_bet(self):
        if self.deposit >= 1000.0:
            bet = self.deposit * 0.1
        elif self.deposit >= 500.0:
            bet = self.deposit * 0.05
        else:
            bet = self.deposit * 0.03
        self.deposit -= bet
        return bet

    def make_choice(self):
        return 'Орел' if random.choice([True, False]) else 'Решка'


class GameData(RealPlayer, Bot):
    def __init__(self, json_file):
        super().__init__(json_file)
        self.real_player = RealPlayer(json_file)
        self.bot = Bot(json_file)
        self.real_player_bet = 0
        self.bot_bet = 0
        self.real_player_choice = ''
        self.bot_choice = ''
        self.total_bet = 0
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def update_player(self, player, bet, choice):
        if player == self.real_player:
            self.real_player_bet = bet
            self.real_player_choice = choice
        elif player == self.bot:
            self.bot_bet = bet
            self.bot_choice = choice
        self.total_bet += bet
        self.notify_observers()

    def win_pool(self):
        return self.total_bet


class Game(GameData):
    def __init__(self, json_file):
        super().__init__(json_file)
        self.logger = logging.getLogger('game_logger')
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler('game.log')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def update(self):
        if self.real_player_bet and self.bot_bet and self.real_player_choice and self.bot_choice:
            self.determine_winner()  # Починаємо гру, якщо всі гравці зробили ставку та вибрали сторону монетки

    def flip_coin(self):
        return 'Орел' if random.choice([True, False]) else 'Решка'

    def determine_winner(self):
        result = self.flip_coin()
        winners = []

        if self.real_player_choice == result:
            winners.append(self.real_player.name)

        if self.bot_choice == result:
            winners.append(self.bot.name)

        if winners:
            win_amount = self.win_pool()  # Весь призовий фонд
            prize_per_winner = win_amount / len(winners)  # Розподіл призу між переможцями

            for winner in winners:
                if winner == self.real_player.name:
                    self.real_player.deposit += prize_per_winner
                elif winner == self.bot.name:
                    self.bot.deposit += prize_per_winner

            self.save_players()
            winner_names = ", ".join(winners)
            self.logger.info(f"Переможцем(ами) стає {winner_names} та кожен з них виграє {prize_per_winner}.")
        else:
            win_amount = 0
            self.logger.info("Ніхто не переміг.")
            # Повернення ставок гравцям у разі нічиєї
            self.real_player.deposit += self.real_player_bet
            self.bot.deposit += self.bot_bet
            self.save_players()

        self.total_bet = 0  # Обнулення величини поточної ставки

        self.logger.info(f"Випала сторона {result}.")
        self.logger.info(f"Ставка гравця {self.real_player.name}: {self.real_player_bet}")
        self.logger.info(f"Ставка гравця {self.bot.name}: {self.bot_bet}")
        self.logger.info(f"Депозит гравця {self.real_player.name} після гри: {self.real_player.deposit}")
        self.logger.info(f"Депозит гравця {self.bot.name} після гри: {self.bot.deposit}")

        print(f"Випала сторона {result}.")
        print(f"Ставка гравця {self.real_player.name}: {self.real_player_bet}")
        print(f"Ставка гравця {self.bot.name}: {self.bot_bet}")
        if winners:
            print(f"Переможцем(ами) стає {', '.join(winners)} та кожен з них виграє {prize_per_winner}.")
        else:
            print("Ніхто не переміг.")
        print(f"Депозит гравця {self.real_player.name} після гри: {self.real_player.deposit}")
        print(f"Депозит гравця {self.bot.name} після гри: {self.bot.deposit}")

        self.play_again()

    def save_players(self):
        self.players_data['real_player']['deposit'] = self.real_player.deposit
        self.players_data['bots']['deposit'] = self.bot.deposit
        with open(self.json_file, 'w') as file:
            json.dump(self.players_data, file, indent=4)

    def play_again(self):
        while True:
            play_again = input("\nХочете зіграти? (y/n): ")
            if play_again.lower() == 'n':
                print("Гра завершена!")
                exit()
            elif play_again.lower() == 'y':
                print("\nНовий раунд:")
                print(f"Депозит гравця {self.real_player.name}: {self.real_player.deposit}")
                print(f"Депозит бота {self.bot.name}: {self.bot.deposit}")
                player1_bet = self.real_player.make_bet()
                player1_choice = self.real_player.make_choice()
                self.update_player(self.real_player, player1_bet, player1_choice)

                player2_bet = self.bot.make_bet()
                player2_choice = self.bot.make_choice()
                self.update_player(self.bot, player2_bet, player2_choice)

# Початок гри

import csv
import random
from typing import List, Union


class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender


class Parameters(Person):
    def __init__(self, name: str, age: int, gender: str, height: int, weight: int):
        super().__init__(name, age, gender)
        self.height = height
        self.weight = weight


class NicknameGenerator(Person):
    def __init__(self, name: str, age: int, gender: str, height: int, weight: int):
        super().__init__(name, age, gender)
        self.height = height
        self.weight = weight
        self.adjectives = self.read_csv_file("data/adjectives.csv")
        self.nouns = self.read_csv_file("data/nouns.csv")

    def generate_nickname(self) -> str:
        unique_adjectives = random.sample(self.adjectives, 1)
        unique_nouns = random.sample(self.nouns, 1)
        nickname = f"{unique_adjectives[0]} {unique_nouns[0]}"
        return nickname

    @staticmethod
    def read_csv_file(filename: str) -> List[str]:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            words = [row[0] for row in reader]
        return words


class Fighter(NicknameGenerator):
    def __init__(self, name: str, gender: str, age: int, weight: int, height: int):
        super().__init__(name, age, gender, height, weight)
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def record_win(self) -> None:
        self.wins += 1

    def record_loss(self) -> None:
        self.losses += 1

    def record_draw(self) -> None:
        self.draws += 1

    def get_statistics(self) -> str:
        return f"{self.name} {self.generate_nickname()} - Перемог: {self.wins}, Поразок: {self.losses}, Нічій: {self.draws}"
    @classmethod
    def load_fighters_from_csv(cls, filename: str) -> List['Fighter']:
        fighters_list = []
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                name, gender, age, weight, height = row
                fighter = cls(name, gender, int(age), int(weight), int(height))
                fighters_list.append(fighter)
        return fighters_list


class Combat:
    def __init__(self, fighters: List[Fighter], statistics, num_rounds: int = 5):
        self.fighters = fighters
        self.statistics = statistics
        self.num_rounds = num_rounds

    def start_combat(self) -> None:
        for round_num in range(self.num_rounds):
            print(f"Бій №{round_num + 1}")
            self.single_combat()

    def single_combat(self) -> None:
        fighter1, fighter2 = random.sample(self.fighters, 2)
        winner = self.determine_winner(fighter1, fighter2)
        losers = [fighter for fighter in [fighter1, fighter2] if fighter != winner]
        self.statistics.update_statistics(winner, losers)
        winner_name = winner.name if isinstance(winner, Fighter) else "Нічия"
        print(f"{fighter1.name} vs {fighter2.name} - Переможець: {winner_name}")

        print("Статистика після бою:")
        for fighter in [fighter1, fighter2]:
            print(fighter.get_statistics())
        print()

    @staticmethod
    def determine_winner(fighter1: Fighter, fighter2: Fighter) -> Union[Fighter, None]:
        # Визначення переможця
        if random.choice([True, False]):
            return fighter1
        elif random.choice([True, False]):
            return fighter2
        else:
            return None  # Нічия


class CombatStatistics:
    def __init__(self, fighters: List[Fighter]):
        self.fighters = fighters

    def update_statistics(self, winner: Fighter, losers: List[Fighter]) -> None:
        if winner:
            winner.record_win()
            for loser in losers:
                loser.record_loss()
        else:
            for loser in losers:
                loser.record_draw()

    def display_total_statistics(self) -> None:
        print("Загальна статистика після боїв:")
        for fighter in self.fighters:
            print(fighter.get_statistics())



# Почнемо бої з ініціалізаціі бійців, статистики та кількості раундів.
fighters_data = Fighter.load_fighters_from_csv("data/fighters_data.csv")
fighters_list = [Fighter(fighter.name, fighter.gender, fighter.age, fighter.weight, fighter.height) for fighter in
                 fighters_data]

statistics_instance = CombatStatistics(fighters_list)
num_rounds = 10  # Задаємо кількість раундів
combat_instance = Combat(fighters_list, statistics_instance, num_rounds)

# Проводимо бої

combat_instance.start_combat()

# Виводимо загальну статистику після боїв
statistics_instance.display_total_statistics()

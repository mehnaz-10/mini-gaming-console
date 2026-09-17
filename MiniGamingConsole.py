
import random
from dataclasses import dataclass


# ==========================================
# PLAYER CLASS
# ==========================================

@dataclass
class Player:
    name: str
    _score: int = 0

    # Getter
    @property
    def score(self):
        return self._score

    # Setter
    @score.setter
    def score(self, value):
        if value >= 0:
            self._score = value
        else:
            print("Score cannot be negative.")

    # Add points
    def add_score(self, points):
        self._score += points

    # Display player information
    def show_profile(self):
        print()
        print("----- PLAYER PROFILE -----")
        print("Name:", self.name)
        print("Score:", self.score)
        print("--------------------------")
        print()


# ==========================================
# PARENT GAME CLASS
# ==========================================

@dataclass
class Game:
    name: str
    description: str

    def play(self, player):
        print("Starting game...")


# ==========================================
# DICE GAME - CHILD CLASS
# ==========================================

@dataclass
class DiceGame(Game):

    def play(self, player):
        print()
        print("===== DICE GAME =====")

        player_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)

        print("You rolled:", player_roll)
        print("Computer rolled:", computer_roll)

        if player_roll > computer_roll:
            print("You win! +10 points")
            player.add_score(10)

        elif player_roll < computer_roll:
            print("Computer wins! +0 points")

        else:
            print("It's a tie! +5 points")
            player.add_score(5)

        print("Current score:", player.score)
        print()


# ==========================================
# GUESSING GAME - CHILD CLASS
# ==========================================

@dataclass
class GuessingGame(Game):

    def play(self, player):
        print()
        print("===== GUESS THE NUMBER =====")

        secret_number = random.randint(1, 10)

        try:
            guess = int(input("Guess a number from 1 to 10: "))

            if guess == secret_number:
                print("Correct! +20 points")
                player.add_score(20)

            else:
                print("Wrong!")
                print("The number was:", secret_number)

        except ValueError:
            print("Please enter a valid number.")

        print("Current score:", player.score)
        print()


# ==========================================
# ROCK PAPER SCISSORS - CHILD CLASS
# ==========================================

@dataclass
class RockPaperScissors(Game):

    def play(self, player):
        print()
        print("===== ROCK PAPER SCISSORS =====")

        choices = ["rock", "paper", "scissors"]

        computer_choice = random.choice(choices)

        player_choice = input(
            "Choose rock, paper, or scissors: "
        ).lower()

        if player_choice not in choices:
            print("Invalid choice.")
            return

        print("Computer chose:", computer_choice)

        if player_choice == computer_choice:
            print("It's a tie! +5 points")
            player.add_score(5)

        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or
            (player_choice == "paper" and computer_choice == "rock")
            or
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win! +15 points")
            player.add_score(15)

        else:
            print("Computer wins!")

        print("Current score:", player.score)
        print()


# ==========================================
# GAME CONSOLE CLASS
# ==========================================

class GameConsole:

    def __init__(self, player):
        self.player = player

        # Create game objects
        self.games = [
            DiceGame(
                "Dice Game",
                "Roll the dice against the computer."
            ),
            GuessingGame(
                "Guess the Number",
                "Guess a number from 1 to 10."
            ),
            RockPaperScissors(
                "Rock Paper Scissors",
                "Play rock, paper, scissors."
            )
        ]

    # Display the main menu
    def show_menu(self):
        print("================================")
        print("       MY GAMING CONSOLE")
        print("================================")

        for number, game in enumerate(self.games, start=1):
            print(number, ".", game.name)

        print("4. View Player Profile")
        print("5. Exit")
        print("================================")

    # Start the console
    def start(self):

        while True:

            self.show_menu()

            choice = input("Choose an option: ")

            if choice in ["1", "2", "3"]:

                game_number = int(choice) - 1

                game = self.games[game_number]

                # Demonstrating isinstance()
                if isinstance(game, Game):
                    game.play(self.player)

            elif choice == "4":
                self.player.show_profile()

            elif choice == "5":
                print()
                print("Thanks for playing,", self.player.name + "!")
                print("Final score:", self.player.score)
                break

            else:
                print("Invalid choice.")
                print()


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    print("Welcome to My Gaming Console!")

    name = input("Enter your player name: ")

    # Create Player object
    player = Player(name)

    # Create GameConsole object
    console = GameConsole(player)

    # Start the console
    console.start()


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":
    main()


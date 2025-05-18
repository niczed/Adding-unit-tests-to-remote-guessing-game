# guessing_game.py
import random

class GuessingGame:
    def __init__(self, number_generator=None, max_attempts=3):
        self.secret_number = number_generator() if number_generator else random.randint(1, 10)
        self.max_attempts = max_attempts
        self.attempts = 0

    def guess(self, number):
        self.attempts += 1
        if self.attempts > self.max_attempts:
            return "No attempts left."
        if number == self.secret_number:
            return "Correct!"
        elif number < self.secret_number:
            return "Too low."
        else:
            return "Too high."

    def has_attempts_left(self):
        return self.attempts < self.max_attempts

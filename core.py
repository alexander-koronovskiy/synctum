import random

class Roulette:
    def __init__(self):
        self.numbers = list(range(1, 11))
        self.drawn_numbers = []

    def spin(self, nums):
        self.drawn_numbers = [int(x) for x in nums]
        if len(self.drawn_numbers) < 9:
            result = random.choice(self.numbers)
            self.drawn_numbers.append(result)
        else:
            result = "Jackpot"
        return result

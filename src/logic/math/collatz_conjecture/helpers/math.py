from abc import ABC, abstractmethod


class CollatzMathStrategy(ABC):
    @abstractmethod
    def apply_math(self, number: [int, float]):
        """Method that applies some sort of math."""


class EvenStrategy(CollatzMathStrategy):
    def apply_math(self, number: [int, float]):
        return number / 2


class OddStrategy(CollatzMathStrategy):
    def apply_math(self, number: [int, float]):
        return (number * 3) + 1


class CollatzMath:
    """A simple class that applies the collatz math."""
    def __init__(self, strategy: CollatzMathStrategy, number):
        self._strategy = strategy
        self.number = number

    @property
    def strategy(self) -> CollatzMathStrategy:
        return self._strategy

    def set_strategy(self, strategy: CollatzMathStrategy) -> None:
        self._strategy = strategy

    def run(self) -> int:
        return int(self._strategy.apply_math(self.number))





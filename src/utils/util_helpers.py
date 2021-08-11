import time
from abc import ABC


class PrintTimeStrategy(ABC):
    """Abstract class for different time strategies."""
    def __init__(self, calculated_time: time.time, description: str):
        self.calculated_time = calculated_time
        self.description = description

    def print_time(self):
        """Print the times."""


class HourPrintStrategy(PrintTimeStrategy):
    def __init__(self, calculated_time: time.time, description: str):
        super().__init__(calculated_time, description)

    def print_time(self):
        print(f"It took {self.calculated_time} hours to {self.description}.")


class MinutePrintStrategy(PrintTimeStrategy):
    def __init__(self, calculated_time: time.time, description: str):
        super().__init__(calculated_time, description)

    def print_time(self):
        print(f"It took {self.calculated_time} minutes to {self.description}.")


class SecondPrintStrategy(PrintTimeStrategy):
    def __init__(self, calculated_time: time.time, description: str):
        super().__init__(calculated_time, description)

    def print_time(self):
        print(f"It took {self.calculated_time} seconds to {self.description}.")


class MillisecondPrintStrategy(PrintTimeStrategy):
    def __init__(self, calculated_time: time.time, description: str):
        super().__init__(calculated_time, description)

    def print_time(self):
        print(f"It took {self.calculated_time} milliseconds to {self.description}.")


class PrintTimeFactory:
    def __init__(self, start_time: time.time, end_time: time.time, description: str):
        self.start_time = start_time
        self.end_time = end_time
        self.description = description

    def _calculate(self):
        return self.end_time - self.start_time

    def choose(self):
        interval = self._calculate()

        if interval > 3600:
            return HourPrintStrategy(interval, self.description)

        if interval > 60:
            return MinutePrintStrategy(interval, self.description)

        if interval > 1:
            interval = round(interval)

            return SecondPrintStrategy(interval, self.description)

        interval = interval * 1000
        interval = round(interval)

        return MillisecondPrintStrategy(interval, self.description)

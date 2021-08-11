import time

from src.utils.util_helpers import PrintTimeStrategy, PrintTimeFactory


def print_time(start: time.time, end: time.time, description: str):
    strategy: PrintTimeStrategy = PrintTimeFactory(start, end, description).choose()

    strategy.print_time()

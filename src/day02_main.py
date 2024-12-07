from advent_of_code_io import read_as_lists_of_integers
from day02 import safe_count, safe_count_with_dampener


def run():
    reports = read_as_lists_of_integers('data/day02.txt')
    print(f'Number of reports: {len(reports)}')
    num_safe = safe_count(reports)
    print(f'Number of safe reports: {num_safe}')
    num_safe_with_dampener = safe_count_with_dampener(reports)
    print(f'Number of safe reports with dampener: {num_safe_with_dampener}')


if __name__ == "__main__":
    run()

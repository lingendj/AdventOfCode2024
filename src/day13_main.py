from day13 import tokens_to_win_all_prizes


def main():
    with open('data/13.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    tokens = tokens_to_win_all_prizes(lines, 0)
    print(f'Part 1: {tokens}')
    tokens_two = tokens_to_win_all_prizes(lines, 10000000000000)
    print(f'Part 2: {tokens_two}')


if __name__ == "__main__":
    main()

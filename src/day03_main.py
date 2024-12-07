from day03 import sum_of_product, sum_of_product_with_instructions


def run():
    with open('data/03.txt', 'r') as f:
        text = f.read()
    print(f'Part 1: {sum_of_product(text)}')
    print(f'Part 2: {sum_of_product_with_instructions(text)}')


if __name__ == "__main__":
    run()

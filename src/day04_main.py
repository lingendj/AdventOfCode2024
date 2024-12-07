from day04 import word_search_count, num_kernel_matches


def run():
    with open('data/04.txt', 'r') as f:
        grid = f.readlines()

    num_matches = word_search_count("XMAS", grid)
    print(f'Part 1: {num_matches}')

    kernels = [["M.S",
                ".A.",
                "M.S"],
               ["S.S",
                ".A.",
                "M.M"],
               ["M.M",
                ".A.",
                "S.S"],
               ["S.M",
                ".A.",
                "S.M"]]

    print(f'Part 2: {num_kernel_matches(kernels, grid)}')


if __name__ == "__main__":
    run()

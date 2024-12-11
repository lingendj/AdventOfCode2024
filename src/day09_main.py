from day09 import checksum, checksum_brute_force, checksum_part_two


def run():
    with open('data/09.txt', 'r') as f:
        disk_map = f.read().strip()

    print(len(disk_map))
    print(f'Part 1: {checksum_brute_force(disk_map)}')
    print(f'Part 2: {checksum_part_two(disk_map)}')


if __name__ == "__main__":
    run()

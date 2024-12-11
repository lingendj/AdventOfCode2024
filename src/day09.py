from collections import defaultdict
"""
232
i_free =1
i_right = 2
num_left = 3
num_right = 2



"""


def file_id_from_array_index(index: int):
    return index // 2


def sum_positions(start: int, end: int):
    """
    Sum of integers on [start, end)
    """
    return end*(end-1)//2 - (start*(start-1))//2


def checksum(disk_map_str: str) -> int:
    disk_map = [int(c) for c in disk_map_str]
    i_left = 0
    i_right = len(disk_map) - 1
    checksum = 0
    # If the string has even length, the last entry is free space and
    # doesn't need to be moved
    if i_right % 2 == 1:
        i_right -= 1

    num_left = disk_map[1]
    num_right = disk_map[i_right]
    position = 0
    debug_output = []
    while i_left < i_right:
        if i_left % 2 == 0:
            end_position = position + disk_map[i_left]
            checksum += sum_positions(position, end_position) * \
                file_id_from_array_index(i_left)
            for i in range(position, end_position):
                debug_output += [file_id_from_array_index(i_left)]
            position = end_position
            i_left += 1

        else:
            num_moved = min(num_left, num_right)
            end_position = position + num_moved
            for i in range(position, end_position):
                debug_output += [file_id_from_array_index(i_right)]
            checksum += file_id_from_array_index(i_right) * \
                sum_positions(position, end_position)
            position = end_position
            num_left -= num_moved
            num_right -= num_moved
            if num_left == 0:
                i_left += 1
                if i_left < i_right:
                    num_left = disk_map[i_left + 1]
                else:
                    checksum += num_right * \
                        sum_positions(position, position + num_right) * \
                        file_id_from_array_index(i_right)
                    for i in range(position, position + num_right):
                        debug_output += [file_id_from_array_index(i_right)]
            if num_right == 0:
                i_right -= 2
                num_right = disk_map[i_right]
    debug_sum = 0
    for i, c in enumerate(debug_output):
        debug_sum += int(c) * i
    return checksum


def expand_disk_map(disk_map):
    expanded_map = []
    for i_block, block_size in enumerate(disk_map):
        if i_block % 2 == 0:
            value = i_block // 2
        else:
            value = None
        for _ in range(block_size):
            expanded_map += [value]
    return expanded_map


def checksum_brute_force(disk_map_str: str):
    disk_map = [int(c) for c in disk_map_str]
    expanded_map = expand_disk_map(disk_map)
    i_left = 0
    i_right = len(expanded_map) - 1
    while i_right > i_left:
        if expanded_map[i_left] is not None:
            i_left += 1
            continue
        if expanded_map[i_right] is None:
            i_right -= 1
            continue
        expanded_map[i_left] = expanded_map[i_right]
        expanded_map[i_right] = None
        i_left += 1
        i_right -= 1
    sum = 0
    for i, value in enumerate(expanded_map):
        if value is not None:
            sum += i * value
    return sum


def checksum_part_two(disk_map_str: str):
    disk_map = [int(c) for c in disk_map_str]
    size_by_position = defaultdict(lambda: None)
    index_by_position = defaultdict(lambda: None)
    position = 0
    for i, size in enumerate(disk_map):
        size_by_position[position] = size
        index_by_position[position] = i
        position += size

    expanded_map = expand_disk_map(disk_map)
    i_left = 0
    i_right = len(expanded_map) - 1
    prev_value = None
    file_size = 0
    for i_right in range(len(expanded_map) - 1, -1, -1):
        if size_by_position[i_right] is None:
            continue
        if expanded_map[i_right] is None:
            continue
        for i_left in range(i_right):
            if size_by_position[i_left] is None:
                continue
            if expanded_map[i_left] is not None:
                continue
            if size_by_position[i_right] <= size_by_position[i_left]:
                for i in range(size_by_position[i_right]):
                    expanded_map[i_left + i] = expanded_map[i_right + i]
                    expanded_map[i_right + i] = None
                if size_by_position[i_left] - size_by_position[i_right] > 0:
                    size_by_position[i_left + size_by_position[i_right]
                                     ] = size_by_position[i_left] - size_by_position[i_right]
                size_by_position[i_left] = size_by_position[i_right]
                size_by_position[i_right] = 0
                break
    sum = 0
    for i, value in enumerate(expanded_map):
        if value is not None:
            sum += i * value
    return sum

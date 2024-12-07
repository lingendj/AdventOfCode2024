from typing import List

DIRECTIONS = [(1, 0),  # Right
              (-1, 0),  # Left
              (0, 1),  # Down
              (0, -1),  # Up
              (1, 1),  # Diagonal Right Down
              (1, -1),  # Diagonal Right Up
              (-1, 1),  # Diagonal Left Down
              (-1, -1)  # Diagonal Left Up
              ]


def word_matches(word: str,
                 row_start: int,
                 col_start: int,
                 direction_horizontal: int,
                 direction_vertical: int,
                 word_search_grid: List[str]) -> bool:
    i_row = row_start
    i_col = col_start
    for i_word in range(len(word)):
        # print(f"i_row: {i_row}, i_col: {i_col}, letter: {word[i_word]}")
        if i_row < 0 or i_row >= len(word_search_grid):
            return False
        if i_col < 0 or i_col >= len(word_search_grid[i_row]):
            return False
        if word_search_grid[i_row][i_col] != word[i_word]:
            return False
        i_row += direction_vertical
        i_col += direction_horizontal
    return True


def num_matches_at_start(word: str,
                         row_start: int,
                         col_start: int,
                         word_search_grid: List[str]) -> int:
    match_count = 0
    for dir_horizontal, dir_vertical in DIRECTIONS:
        if word_matches(word, row_start, col_start, dir_horizontal,
                        dir_vertical, word_search_grid):
            match_count += 1
    return match_count


def word_search_count(word: str, grid: List[str]) -> bool:
    match_count = 0
    for i_row in range(len(grid)):
        for i_col in range(len(grid[i_row])):
            match_count += num_matches_at_start(word,
                                                i_row,
                                                i_col,
                                                grid)
    return match_count


def kernel_matches(kernel: List[str],
                   row_start: int,
                   col_start: int,
                   word_search_grid: List[str]) -> bool:
    i_row_grid = row_start
    i_col_grid = col_start
    for i_row_kernel in range(len(kernel)):
        for i_col_kernel in range(len(kernel[i_row_kernel])):
            grid_row_index = i_row_grid + i_row_kernel
            if (grid_row_index >= len(word_search_grid)):
                return False
            grid_col_index = i_col_grid + i_col_kernel
            if (grid_col_index >= len(word_search_grid[grid_row_index])):
                return False
            if kernel[i_row_kernel][i_col_kernel] == '.':
                continue
            if kernel[i_row_kernel][i_col_kernel] != word_search_grid[grid_row_index][grid_col_index]:
                return False
    return True


def num_kernel_matches(kernels: List[List[str]], grid: List[str]):
    match_count = 0
    for i_row in range(len(grid)):
        for i_col in range(len(grid[i_row])):
            for kernel in kernels:
                if kernel_matches(kernel, i_row, i_col, grid):
                    match_count += 1
    return match_count

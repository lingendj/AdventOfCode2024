import unittest
from src.day12 import Region, get_region, get_fencing_cost


class TestDay12(unittest.TestCase):
    def test_get_region(self):
        grid = ['AAAA',
                'BBCD',
                'BBCC',
                'EEEC']
        region = Region()
        region = get_region(1, 0, grid[1][0], region, grid)
        self.assertEqual(region.perimeter, 8)
        self.assertEqual(region.area(), 4)

    def test_get_fencing_cost(self):
        grid = ['RRRRIICCFF',
                'RRRRIICCCF',
                'VVRRRCCFFF',
                'VVRCCCJFFF',
                'VVVVCJJCFE',
                'VVIVCCJJEE',
                'VVIIICJJEE',
                'MIIIIIJJEE',
                'MIIISIJEEE',
                'MMMISSJEEE']
        self.assertEqual(get_fencing_cost(grid), 1930)

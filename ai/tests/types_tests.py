from unittest import TestCase, main
from ai.types import Grid

__author__ = "Bilal El Uneis"
__since__ = "Dec 2019"
__email__ = "bilaleluneis@gmail.com"


class TypesTests(TestCase):

    def test_grid(self) -> None:
        grid: Grid[int] = Grid[int](3, 3)
        grid[0][0] = 0
        self.assertEqual(grid[0][0], 0)


if __name__ == '__main__':
    main()

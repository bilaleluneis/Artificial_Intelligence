from unittest import TestCase, main
from ai.types.grid import Grid

__author__ = "Bilal El Uneis"
__since__ = "Dec 2019"
__email__ = "bilaleluneis@gmail.com"


class GridTests(TestCase):

    def setUp(self) -> None:
        self.__grid_a: Grid[int] = Grid[int](4, 4)  # one way to init
        self.__grid_b: Grid[int] = Grid(4, 4)  # another way to init and keep type checker happy !
        self.__grid_c: Grid[int] = Grid(2, 2)
        self.__grid_d: Grid[str] = Grid(4, 4)

    def test_bad_init(self) -> None:
        with self.assertRaises(IndexError):
            Grid[int](0, -1)

    def test_good_init(self) -> None:
        rows, cols = self.__grid_a.dimension
        self.assertEqual((rows, cols), (4, 4))
        for row in range(rows):
            for col in range(cols):
                self.assertEqual(self.__grid_a[row][col], None)

    def test_index_access(self) -> None:
        self.__grid_a[0][3] = 1
        self.assertEqual(self.__grid_a[0][3], 1)

    def test_out_of_range_index_access(self) -> None:
        with self.assertRaises(IndexError):
            self.__grid_a[0][5] = 1  # access invalid col
        with self.assertRaises(IndexError):
            self.__grid_a[5][1] = 1  # access invalid row

    def test_contains(self) -> None:
        self.assertFalse(1 in self.__grid_a)
        self.__grid_a[3][3] = 1
        self.assertTrue(1 in self.__grid_a)


if __name__ == '__main__':
    main()

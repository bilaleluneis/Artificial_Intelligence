from typing import TypeVar, List, Generic, Tuple, Union

__author__ = "Bilal El Uneis"
__since__ = "Dec 2019"
__email__ = "bilaleluneis@gmail.com"

_Type = TypeVar('_Type')


class Grid(Generic[_Type]):
    __slots__ = ('__rows', '__cols', '__grid')

    def __init__(self, rows: int, cols: int) -> None:
        self.__rows: int = rows
        self.__cols: int = cols
        self.__grid: List[List[Union[_Type, None]]] = []
        self.__initalize()

    def __repr__(self) -> str:
        return self.__describe()

    def __getitem__(self, row: int, col: int) -> Union[_Type, None]:
        if row not in range(self.__rows) or col not in range(self.__cols):
            raise IndexError(f"[row][col] = [{row}][{col}] is not valid index on Grid")
        return self.__grid[row][col]

    @property
    def dimension(self) -> Tuple[int, int]:
        return self.__rows, self.__cols

    def __describe(self) -> str:
        if not self.__grid:
            return "[]"
        grid_repr: str = ""
        for row_index in range(self.__rows):
            row: List[Union[_Type, None]] = self.__grid[row_index]
            grid_repr += "[ "
            for col_index in range(self.__cols):
                grid_repr += str(row[col_index])
                grid_repr += " "
            grid_repr += "]\n"
        return grid_repr

    def __initalize(self) -> None:
        for row_index in range(self.__rows):
            row: List[Union[_Type, None]] = []
            for col_index in range(self.__cols):
                row.append(None)
            self.__grid.append(row)

from __future__ import annotations
from typing import TypeVar, List, Generic, Tuple, Union, Any, Iterator

__author__ = "Bilal El Uneis"
__since__ = "Dec 2019"
__email__ = "bilaleluneis@gmail.com"

_Type = TypeVar('_Type')


class Grid(Generic[_Type]):
    __slots__ = ('__rows', '__cols', '__grid')

    def __init__(self, rows: int, cols: int) -> None:
        if rows <= 0 or cols <= 0:
            raise IndexError(f"Init with Grid Dimension [{rows}][{cols}] is Invalid!")
        self.__rows: int = rows
        self.__cols: int = cols
        self.__grid: List[List[Union[_Type, None]]] = []
        self.__initalize()

    def __repr__(self) -> str:
        return self.__describe()

    def __len__(self) -> int:
        return len(self.__grid)

    def __getitem__(self, row: int) -> List[Union[_Type, None]]:
        if row not in range(self.__rows):
            raise IndexError(f"[row]= [{row}] is not a valid index on Grid")
        return self.__grid[row]

    def __iter__(self) -> Iterator[Union[_Type, None]]:
        rows, cols = self.dimension
        for row in range(rows):
            for col in range(cols):
                yield self[row][col]

    def __contains__(self, value: Union[_Type, None]) -> bool:
        for item in self:
            if item == value:
                return True
        return False

    def __eq__(self, grid: Any) -> bool:
        if type(grid) is not Grid[_Type]:
            return False
        if self.dimension != grid.dimension:
            return False
        for row in range(self.__rows):
            for col in range(self.__cols):
                if self[row][col] != grid[row][col]:
                    return False
        return True

    def __ne__(self, grid: Any) -> bool:
        return not self.__eq__(grid)

    @property
    def dimension(self) -> Tuple[int, int]:
        return self.__rows, self.__cols

    def __describe(self) -> str:
        if not self.__grid:
            return "[ ]"
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

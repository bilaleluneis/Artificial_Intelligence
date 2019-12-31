from typing import TypeVar, Generic

__author__ = "Bilal El Uneis"
__since__ = "Dec 2019"
__email__ = "bilaleluneis@gmail.com"

S = TypeVar('S')


class State(Generic[S]):
    __slots__ = '__state_data'

    def __init__(self, state_data: S) -> None:
        self.__state_data: S = state_data

    @property
    def value(self) -> S:
        return self.__state_data

    # TODO: Implement __str__ and __rper__

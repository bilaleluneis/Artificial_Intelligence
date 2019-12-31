from typing import List, Iterable, Tuple
from ai.state import State
from ai.problem import Problem, StateTransition, Successor
from more_itertools import ilen  # type: ignore # make MyPy ignore the type check on ilen

__author__ = "Bilal El Uneis"
__since__ = "Dec 2019"
__email__ = "bilaleluneis@gmail.com"

IntTuple = Tuple[int, int]


class SimpleGridProblem(Problem[IntTuple, str, float]):
    """
    a Test Problem that implement the Problem Protocol to be used to smoke test Problem Protocol:
    Problem: E = Empty Space, S = Start, G = Goal
    [E, S, E]
    [E, E, E]
    [G, E, E]

    """
    __slots__ = ('__maze', '__num_rows', '__num_col')

    def __init__(self) -> None:
        self.__maze: List[List[str]] = [['E', 'S', 'E'], ['E', 'E', 'E'], ['G', 'E', 'E']]
        self.__num_rows: int = 3
        self.__num_col: int = 3

    def get_start_state(self) -> State[IntTuple]:
        for row in range(self.__num_rows):
            for col in range(self.__num_col):
                if self.__maze[row][col] == 'S':
                    return State((row, col))
        return State((-1, -1))

    def is_goal_state(self, state: State[IntTuple]) -> bool:
        row, col = state.value
        return self.__maze[row][col] == 'G'

    def get_successors(self, state: State[IntTuple]) -> Iterable[Successor[IntTuple, str, float]]:
        row, col = state.value
        successors: List[Successor[IntTuple, str, float]] = []
        if row - 1 >= 0:
            successors.append(Successor(State((row - 1, col)), 'UP', 1.0))
        if row + 1 < self.__num_rows:
            successors.append(Successor(State((row + 1, col)), 'DOWN', 1.0))
        if col - 1 >= 0:
            successors.append(Successor(State((row, col - 1)), 'LEFT', 1.0))
        if col + 1 < self.__num_col:
            successors.append(Successor(State((row, col + 1)), 'RIGHT', 1.0))
        return successors

    def get_cost_of_actions(self, actions: Iterable[StateTransition[IntTuple]]) -> float:
        return float(1.0 * ilen(actions))

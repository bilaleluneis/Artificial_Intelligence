from typing import Iterable, List
from ai.types import list_of_lists
from ai.state import S, State
from ai.problem import Problem, StateTransition, C, Successor, A
from typing_extensions import Final

__author__ = "Bilal El Uneis"
__since__ = "Dec 2019"
__email__ = "bilaleluneis@gmail.com"

EIGHT_PUZZLE_DATA: Final[list_of_lists[int]] = [[1, 0, 2, 3, 4, 5, 6, 7, 8],
                                                [1, 7, 8, 2, 3, 4, 5, 6, 0],
                                                [4, 3, 2, 7, 0, 5, 1, 6, 8],
                                                [5, 1, 3, 4, 0, 2, 6, 7, 8],
                                                [1, 2, 5, 7, 6, 8, 0, 4, 3],
                                                [0, 3, 1, 6, 8, 2, 7, 5, 4]]


class EightPuzzle:
    pass


class EightPuzzleSearchProblem(Problem):
    """ Search Problem that is based on code from the berkeley pacman projects """

    def get_start_state(self) -> State[S]:
        return super().get_start_state()

    def is_goal_state(self, state: State[S]) -> bool:
        return super().is_goal_state(state)

    def get_successors(self, state: State[S]) -> Iterable[Successor[S, A, C]]:
        return super().get_successors(state)

    def get_cost_of_actions(self, actions: Iterable[StateTransition[S]]) -> C:
        return super().get_cost_of_actions(actions)

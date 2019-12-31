from typing import List, Iterable
from ai.state import State
from ai.problem import Problem, StateTransition, Successor
from unittest import TestCase, main
from .simple_grid_problem import IntTuple, SimpleGridProblem  # type: ignore

__author__ = "Bilal El Uneis"
__since__ = "Dec 2019"
__email__ = "bilaleluneis@gmail.com"


class ProblemTests(TestCase):

    def setUp(self) -> None:
        self.__test_problem: Problem[IntTuple, str, float] = SimpleGridProblem()

    def test_cannot_instantiate_protocol(self) -> None:
        with self.assertRaises(TypeError):
            Problem[IntTuple, str, float]()

    def test_start_state(self) -> None:
        start_state: State[IntTuple] = self.__test_problem.get_start_state()
        self.assertEqual(start_state.value, (0, 1))

    def test_successors(self) -> None:
        state: State[IntTuple] = self.__test_problem.get_start_state()
        successors: Iterable[Successor[IntTuple, str, float]] = self.__test_problem.get_successors(state)
        for successor in successors:
            self.assertIn(successor.action, ['DOWN', 'LEFT', 'RIGHT'])

    def test_cost_of_action(self) -> None:
        from_state: State[IntTuple] = self.__test_problem.get_start_state()
        successors: Iterable[Successor[IntTuple, str, float]] = self.__test_problem.get_successors(from_state)
        transitioned_states: List[StateTransition[IntTuple]] = [StateTransition(from_state, successor.state)
                                                                for successor in successors]
        cost: float = self.__test_problem.get_cost_of_actions(transitioned_states)
        self.assertEqual(cost, 3.0)


if __name__ == '__main__':
    main()

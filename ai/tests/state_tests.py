from unittest import TestCase, main
from ai.state import State
from typing import Tuple

__author__ = "Bilal El Uneis"
__since__ = "Dec 2019"
__email__ = "bilaleluneis@gmail.com"


class StateTests(TestCase):

    def test_cannot_add_dynamic_property(self) -> None:
        with self.assertRaises(AttributeError):
            state: State[str] = State('A')
            state.x = state.value

    def test_valid_state(self) -> None:
        state_value: Tuple[str, float, int] = ("left", 1.0, 0)
        state = State(state_value)
        self.assertEqual(state.value, state_value)


if __name__ == '__main__':
    main()

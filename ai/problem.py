from typing_extensions import Protocol, runtime_checkable
from typing import Iterable, Generic, TypeVar
from dataclasses import dataclass
from ai.state import State, S

__author__ = "Bilal El Uneis"
__since__ = "Dec 2019"
__email__ = "bilaleluneis@gmail.com"

A = TypeVar("A")
C = TypeVar("C")


@dataclass(frozen=True)
class Successor(Generic[S, A, C]):
    __slots__ = ("state", "action", "cost")
    state: State[S]
    action: A
    cost: C


@dataclass(frozen=True)
class StateTransition(Generic[S]):
    __slots__ = ("from_", "to_")
    from_: State[S]
    to_: State[S]


@runtime_checkable
class Problem(Protocol[S, A, C]):
    def get_start_state(self) -> State[S]: ...
    def is_goal_state(self, state: State[S]) -> bool: ...
    def get_successors(self, state: State[S]) -> Iterable[Successor[S, A, C]]: ...
    def get_cost_of_actions(self, actions: Iterable[StateTransition[S]]) -> C: ...

from dataclasses import dataclass
from enum import Enum
from typing import Any
from typing import Protocol


class Direction(Enum):
    N = "n"
    E = "e"
    S = "s"
    W = "w"
    NE = "ne"
    SE = "se"
    SW = "sw"
    NW = "nw"


@dataclass
class Movement:
    """A movement by an object in a direction."""

    obj: Any
    distance_meters: int
    direction: Direction


class Waiter(Protocol):
    def wait(self, actions_spent: int, direction: Direction) -> Movement:
        ...  # pass or comment can be used instead of ...


class Flyer(Protocol):
    def fly(self, actions_spent: int, direction: Direction) -> Movement:
        """A Flyer can fly"""


class Runner(Protocol):
    def run(self, actions_spent: int, direction: Direction) -> Movement:
        """A Runner can run"""


class BaseHero:
    @property
    def max_speed(self) -> int:
        return 1

    def wait(self, actions_spent: int, direction: Direction) -> Movement:
        return Movement(obj=self, distance_meters=0, direction=direction)


class RunningHero(BaseHero):
    """This hero can run, which is better than nothing."""

    @property
    def run_speed(self) -> int:
        return self.max_speed * 2

    def run(self, actions_spent: int, direction: Direction) -> Movement:
        return Movement(
            obj=self,
            distance_meters=self.run_speed * actions_spent,
            direction=direction,
        )


class FlyingHero(BaseHero):
    """This hero can fly, which is BEAST."""

    @property
    def fly_speed(self) -> int:
        return self.max_speed * 5

    def fly(self, actions_spent: int, direction: Direction) -> Movement:
        return Movement(
            obj=self,
            distance_meters=self.fly_speed * actions_spent,
            direction=direction,
        )


class Board:
    """An imaginary game board that doesn't do anything."""

    def make_wait(
        self, obj: Waiter, direction: Direction, actions_spent: int
    ) -> Movement:
        """Make an object wait.

        ``obj`` is the object to make wait
        ``actions`` is the number of consecutive actions taken to wait

        Returns the total distance in meters that ``piece`` moved on the board
        while waiting (could happen...).
        """
        return obj.wait(actions_spent, direction)

    def make_run(
        self, obj: Runner, direction: Direction, actions_spent: int
    ) -> Movement:
        """Make an object run.

        ``obj`` is the object to make run
        ``actions`` is the number of consecutive actions taken to move

        Returns the total distance in meters that ``obj`` moved on the board.
        """
        return obj.run(actions_spent, direction)

    def make_fly(
        self, obj: Flyer, direction: Direction, actions_spent: int
    ) -> Movement:
        """Make an object fly.

        ``obj`` is the object to make fly
        ``actions`` is the number of consecutive actions taken to move

        Returns the total distance in meters that ``obj`` moved on the board.
        """
        return obj.fly(actions_spent, direction)


def main() -> None:
    board = Board()
    waiter_move = board.make_wait(BaseHero(), Direction.N, 2)
    runner_move = board.make_run(RunningHero(), Direction.NW, 2)
    flyer_move = board.make_fly(FlyingHero(), Direction.S, 2)
    heroes = (
        ("Hero", "Total spaces moved (M)"),
        ("a waiting hero", waiter_move.distance_meters),
        ("a running hero", runner_move.distance_meters),
        ("a flying hero", flyer_move.distance_meters),
    )
    print("\n")
    for description, movement in heroes:
        print("\t{:<22} {:>25}".format(description, movement))


if __name__ == "__main__":
    main()


# Source to blog: https://andrewbrookins.com/technology/building-implicit-interfaces-in-python-with-protocol-classes/

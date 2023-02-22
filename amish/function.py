from typing import Callable

from amish.stack import Stack


def function(fnc: Callable) -> Callable[[Stack], None]:
    """ Decorator to annotate function """

    annotations = fnc.__annotations__

    if (
        annotations.get("vm") != Stack
        or len(annotations.keys()) != 1
    ):
        raise Exception("Functions must be defined with: def name(vm: Stack) -> None:")

    return fnc

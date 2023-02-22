from typing import Callable

from amish.stack import Stack


def function(fnc: Callable) -> Callable[[Stack], None]:
    """ Decorator to annotate function """

    annotations = fnc.__annotations__

    if (
        annotations.get("vm") != Stack
        or annotations.get("return") != None
        or (len(annotations.keys()) != 1 and not annotations.get("return"))
    ):
        raise Exception("Functions must be defined with: def name(vm: Stack) -> None:")

    return fnc

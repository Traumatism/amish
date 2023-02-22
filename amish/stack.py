from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")


class Stack(Generic[T]):
    """ Stack data structure implementation """

    def __init__(self, data: List[T] = []) -> None:
        self.data = data

        super().__init__()

    def push(self, value: T):
        """ Push a value (T) to the stack """
        self.data.append(value)

    def pop(self) -> Optional[T]:
        """ Remove and return a value (T) from the stack """

        try:
            value = self.data[-1]
        except IndexError:
            return None

        self.data = self.data[:-1]

        return value

    def __repr__(self) -> str:
        return " | ".join(map(str, self.data))

from string import ascii_letters
from typing import Callable, Generator

from amish.stack import Stack

Numeric = int | float
Token   = int | float | str | Callable[[Numeric, Numeric], Numeric]


def tokenize_expression(expression: str) -> Generator[Token, None, None]:
    """ Convert an expression into tokens """

    chars_stack = Stack(list(reversed(expression)))

    while next_char := chars_stack.pop():

        if next_char.isalpha():
            content = next_char

            while next_char_b := chars_stack.pop():
                if next_char_b not in ascii_letters:
                    chars_stack.push(next_char_b)
                    break

                content += next_char_b

            yield content

        elif next_char.isalnum():
            content = next_char
            found_dot = False

            while next_char_b := chars_stack.pop():
                if next_char_b == ".":
                    found_dot = True
                    content += "."
                elif not next_char_b.isalnum():
                    chars_stack.push(next_char_b)
                    break
                else:
                    content += next_char_b

            yield (int if found_dot is False else float)(content)

        elif next_char == "+":
            yield lambda x, y: (y + x)

        elif next_char == "-":
            yield lambda x, y: (y - x)

        elif next_char == "*":
            yield lambda x, y: (y * x)

        elif next_char == "/":
            yield lambda x, y: (y / x)

        elif next_char in ("\n", "\t", " "):
            continue

        else:
            raise Exception(f"Unknown symbol: {next_char}")

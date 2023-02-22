from amish.tokenizer import tokenize_expression, Numeric
from amish.stack import Stack

from amish.functions.sqrt import sqrt

VERSION = "1.0.0"

FUNCTIONS = {
    "sqrt": sqrt
}


if __name__ == "__main__":
    print(f"-- Amish version {VERSION}")

    vm_stack: Stack[Numeric] = Stack()

    while True:
        print(f"-- {repr(vm_stack)}")

        user_input = input(">>> ")

        for token in tokenize_expression(user_input):

            # token is a numeric
            if isinstance(token, int) or isinstance(token, float):
                vm_stack.push(token)

            # token is a function
            elif isinstance(token, str):
                FUNCTIONS[token](vm_stack)

            # token is a binary operator
            else:
                x, y = vm_stack.pop(), vm_stack.pop()

                if not (x and y):
                    raise

                vm_stack.push(token(x, y))

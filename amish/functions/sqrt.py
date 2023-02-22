import math

from amish.function import function
from amish.stack import Stack


@function
def sqrt(vm: Stack):
    value = vm.pop()

    if value is None:
        raise

    vm.push(math.sqrt(value))

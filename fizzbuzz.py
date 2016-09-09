"""
Regras do FizzBuzz:

1. Se a posição for multipla de 3 fala "Fizz";
2. Se a posição for multipla de 5 fala "Buzz";
3. Se a posição não for múltipla de 3 nem de 5, fala a posição;
4. E se a posição for multipla de 3 e 5 fala "FizzBuzz".
"""
from functools import partial

multiple_of = lambda base, num : num % base == 0
multiple_of_5 = partial (multiple_of, 5)
multiple_of_3 = partial (multiple_of, 3)


def robot (pos):
    say = str(pos)

    if multiple_of_3(pos) and multiple_of_5(pos):
        say = "FizzBuzz"
    elif multiple_of_5(pos):
        say = "Buzz"
    elif multiple_of_3 (pos):
        say = "Fizz"

    return say

from math import sqrt, sin 
# квадрат: функция принимает число и возвращает его квадрат;
# куб: функция принимает число и возвращает его куб;
# корень: функция принимает число и возвращает корень квадратный из этого числа;
# модуль: функция принимает число и возвращает его модуль;
# синус: функция принимает число (в радианах) и возвращает синус этого числа.


def quad(num: int) -> int:
    return num**2

def cube(num: int) -> int:
    return num**3

def root(num: int) -> float:
    return sqrt(num)

def module(num: int) -> int:
    return abs(num)

def sinus(num: int) -> float:
    return sin(num)



functions = {'квадрат': quad, 'куб': cube, 'корень': root, 'модуль': module, 'синус': sinus}
num, flag = int(input()), input()


print(functions[flag](num))
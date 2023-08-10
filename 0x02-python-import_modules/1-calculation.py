#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
a = 10
b = 5
add_result = add(a, b)
subtract_result = subtract(a, b)
multiply_result = multiply(a, b)
divide_result = divide(a, b)

print("{} + {} = {}".format(a, b, add_result))
print("{} + {} = {}".format(a, b, subtract_result))
print("{} + {} = {}".format(a, b, multiply_result))
print("{} + {} = {}".format(a, b, divide_result))

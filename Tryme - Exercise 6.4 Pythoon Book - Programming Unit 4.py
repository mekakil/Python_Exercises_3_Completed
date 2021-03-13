"""@Mekakil"""
import math
def divisible(a, b):
    if int(a) and int(b) and a>0 and b>0:
        if a%b == 0:
            result1 = b**a
            return int(result1)
        else:
            result2 = b**(a/b)
            return int(result2)
    else:
        return "number is negative or not integer"

def is_power(g, y):
    a = g
    b = y
    if a == b:
        return "the arguments are equal, provide different numbers"
    elif a != b and b == 1:
        return "the second argument is equal 1"
    else:
        divisible(a, b)
        return divisible(a, b)

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))



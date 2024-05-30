import sys

sys.set_int_max_str_digits(1000000)


def fibonacci_generator():
    a = 0
    b = 1
    while True:
        yield a
        a = b
        b = a + b


def get_fibonacci(n):
    count = 1
    for i in fibonacci_generator():
        if count == n:
            return i
        count += 1


print('5th Fibonacci number: ', get_fibonacci(5))
print('200th Fibonacci number: ', get_fibonacci(200))
print('1000th Fibonacci number: ', get_fibonacci(1000))
print('100000th Fibonacci number: ', get_fibonacci(100000))

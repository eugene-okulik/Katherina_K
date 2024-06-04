first_user_number = int(input('Enter first number: '))
second_user_number = int(input('Enter second number: '))


def operation_determ(func):
    
    def wrapper(first, second):

        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'
        elif first < 0 or second < 0:
            operation = '*'
        else:
            operation = None
        return func(first, second, operation)
        
    return wrapper


@operation_determ
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return second - first
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    else:
        print('Check your numbers and try one more time')


result = calc(first_user_number, second_user_number)


print("Your result:", result)

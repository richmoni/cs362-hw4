def fib(n):
    '''Return the `n`th number in the Fibonacci sequence.'''
    if (n == 1):
        return 0
    elif (n == 2):
        return 1

    num1 = 0
    num2 = 1

    for i in range(2, n):
        temp = num1 + num2
        num1 = num2
        num2 = temp

    return num2

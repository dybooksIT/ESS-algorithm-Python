for i in range(1, 51):
    if i % 3 == 0:
        if i % 5 == 0:
            print('FizzBuzz', end=' ')
        else:
            print('Fizz', end=' ')
    elif i % 5 == 0:
        print('Buzz', end=' ')
    else:
        print(i, end=' ')

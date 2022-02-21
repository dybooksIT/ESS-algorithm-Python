import math, time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_prime_time(n):
    for i in range(n):
        if is_prime(i):
            print(i, end=' ')

start = time.time()
is_prime_time(100000)
end = time.time()
print('\n')
print(f"{end - start:.5f} sec")
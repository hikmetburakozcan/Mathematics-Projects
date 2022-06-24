def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

import math

def eratosthenesSieve(N):
    numbers = list(range(2, N+1))
    for p in range(2, int(math.sqrt(N) + 1)):
        if is_prime(p):
            trial = p * 2
            while trial <= N:
                if trial in numbers:
                    numbers.remove(trial)
                trial += p
    return numbers

def get_primes_factor(N):
    print(N, '=', end = ' ')
    prime_factors = []
    candidate_primes = eratosthenesSieve(N)
    for prime in candidate_primes:
        while N % prime == 0:
            prime_factors.append(prime)
            N //= prime
    print(*prime_factors, sep='.')

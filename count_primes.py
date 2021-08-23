class Solution:
    def countPrimes(self, n: int) -> int:
        if n in [0, 1]:
            return 0
        
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
            if not primes[i]:
                continue
            j = i * i
            while j < n:
                primes[j] = False
                j += i
        
        count = 0
        for i in range(2, n):
            if primes[i]:
                count += 1
        return count

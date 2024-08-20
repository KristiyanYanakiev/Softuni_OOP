from typing import List


def get_primes(nums: List[int]):
    for num in nums:
        if num <= 1:
            continue
        for divisor in range(2, num):
            if num % divisor == 0:
                break
        else:
            yield num




print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
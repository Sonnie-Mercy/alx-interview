#!/usr/bin/python3
"""The prime game"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game for x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers where each integer is the maximum number
                     in the range for that round.

    Returns:
        str: Name of the player that won the most rounds, or None for tie.
    """
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # If the number of primes is odd, Maria wins; otherwise, Ben wins
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

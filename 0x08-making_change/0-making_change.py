#!/usr/bin/python3
"""
Determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to make a given total.

    Args:
        coins (list): List of coin denominations available.
        total (int): The total amount to achieve.

    Returns:
        int: The fewest number of coins needed to meet the total,
             or -1 if it's not possible.
    """
    if total <= 0:
        return 0
    if not coins:
        return -1

    # Initialize a list to hold the minimum coins for each value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins to make total 0

    # Iterate over each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

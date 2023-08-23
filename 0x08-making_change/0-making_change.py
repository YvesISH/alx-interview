#!/usr/bin/python3
"""
    python script that determines the fewest number of coins to make change
"""


def makeChange(coins, total):
    """
        function that determines the fewest number of coins to make change
        param:
            -coins: list of the values of the coins in your possession
            -total: total of the change
        :return: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    if len(coins) is 0:
        return -1
    coins = sorted(coins)
    dynamic = [float('inf')] * (total + 1)
    dynamic[0] = 0
    for i in range(total + 1):
        for coin in coins:
            if coin > i:
                break
            if dynamic[i - coin] != -1:
                dynamic[i] = min(dynamic[i - coin] + 1, dynamic[i])
    if dynamic[total] == float('inf'):
        return -1
    return dynamic[total]

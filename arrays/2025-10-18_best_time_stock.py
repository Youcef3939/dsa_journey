"""
you are given an array prices where prices[i] is the price of a stock on day i
you want to maximize your profit by choosing one day to buy and one day to sell. return the maximum profit
if no profit is possible, return 0

Problem: best time to buy and sell stock
Difficulty: Easy
Date: 2025-10-18
Notes: Track the minimum price so far, update max profit each step
"""

from typing import List

def max_profit(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit # type: ignore

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print("Prices:", prices)
    print("Max Profit:", max_profit(prices))  # expected: 5

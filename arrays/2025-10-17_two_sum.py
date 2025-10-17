"""
Problem: Two Sum
Difficulty: Easy
Date: 2025-10-17
Notes: Used hash map for O(n) solution
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
    return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print("Input:", nums, "Target:", target)
    print("Output:", two_sum(nums, target))  # expected output: [0, 1]
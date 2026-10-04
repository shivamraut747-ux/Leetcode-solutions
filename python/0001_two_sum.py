"""
LeetCode 1: Two Sum
Difficulty: Easy
Approach: <one or two sentences about how you solved it>
Time: O(n)   Space: O(n)
"""


def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
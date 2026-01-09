---
layout: default
title: "Algo Patterns: The Two Pointer Technique"
excerpt: "Why iterate once when you can iterate from both ends? A guide to reducing O(N^2) to O(N)."
---

# The Two Pointer Technique

*January 9, 2026 • 4 min read*

In my interview prep, I've noticed a recurring theme: any time I see a "sorted array" or need to find a "pair" of elements, the naive solution is usually $O(N^2)$. The optimized solution is almost always **Two Pointers**.

## The Intuition
Imagine you have a sorted list of numbers and you want to find two that add up to a target.



* **Naive:** Pick the first number, check it against every other number. (Nested loops = Slow).
* **Two Pointers:** Put one finger on the start (Left) and one on the end (Right).
    * Sum too big? Move `Right` down.
    * Sum too small? Move `Left` up.

You touch each element at most once. $O(N)$ time. $O(1)$ space.

## The Template
Here is the Python blueprint I use for these problems:

```python
def solve_two_pointers(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum > target:
            right -= 1  # We need a smaller sum
        else:
            left += 1   # We need a bigger sum
            
    return None
```

## Problem List
This pattern destroys the following LeetCode problems:
1.  **Two Sum II (Sorted):** The classic example.
2.  **Valid Palindrome:** Compare `str[left]` vs `str[right]` moving inward.
3.  **Container With Most Water:** A variation where you greedily shrink the window based on height.

## Key Takeaway
If the input is **sorted**, think Two Pointers immediately. It trades "searching" for "shrinking the search space."

---
layout: default
title: "The Lying CPU: Branch Prediction & Speculation"
excerpt: "Your CPU executes code you didn't write. An introduction to Branch Prediction, Speculative Execution, and why sorted arrays are faster."
---

# The Lying CPU

*January 8, 2026 • 6 min read*

We often think of the CPU as a diligent worker that executes our instructions one by one, in order. We trust it to run the code we wrote.

**We are wrong.**

Modern CPUs are pathological liars. They execute instructions out of order, guess the future, and speculatively run code that might never actually need to be run. If they guess right, we get a massive speedup. If they guess wrong, they have to "flush" their work and pretend nothing happened.

This concept is the foundation of modern performance engineering—and famously, the root cause of vulnerabilities like Spectre and Meltdown.

## The Pipeline Problem

To understand *why* the CPU lies, we have to look at the **Instruction Pipeline**. 

A CPU doesn't just "do" an instruction in one step. It usually follows a cycle like this:
1.  **Fetch:** Get the instruction from memory.
2.  **Decode:** Figure out what it means.
3.  **Execute:** Do the math.
4.  **Write-back:** Save the result.

If we waited for one instruction to finish before starting the next, our fancy 4GHz processor would spend most of its time idle. Instead, CPUs use **Pipelining**. While Instruction A is being *Executed*, Instruction B is being *Decoded*, and Instruction C is being *Fetched*.

### The Hazard: If / Else
Pipelining works great for straight-line code. But what happens when we hit an `if` statement (a branch)?

```python
if x > 10:
    do_thing_A()
else:
    do_thing_B()
```

The CPU fetches the `if` check. But while it is calculating `x > 10`, it needs to fetch the *next* instruction to keep the pipeline full.
**Which one should it fetch?** `do_thing_A` or `do_thing_B`?

It doesn't know yet. The result of `x > 10` is still stuck in the "Execute" phase.

## The Solution: Branch Prediction
The CPU guesses. It looks at the history of this branch and says, *"Last time we were here, we went to `else`. Let's assume we go to `else` again."*

It starts speculatively executing `do_thing_B`. 
* **If it guessed right:** Free performance! The work is already done.
* **If it guessed wrong:** **Pipeline Flush.** The CPU has to throw away all the work it did for `do_thing_B` and start over with `do_thing_A`. This is expensive.

## The Project: Simulating a Branch Predictor
To visualize this, let's build a **2-bit Saturating Counter**, the standard algorithm used in many real CPUs.

It has four states:
* **00:** Strongly Not Taken
* **01:** Weakly Not Taken
* **10:** Weakly Taken
* **11:** Strongly Taken

It requires *two* wrong guesses to change its mind from "Strongly Taken" to "Strongly Not Taken". This adds "hysteresis" (momentum) so a single outlier doesn't ruin the prediction.

Here is a simulation in Python:

```python
import random

class SaturatingCounter:
    def __init__(self):
        # Start at 01 (Weakly Not Taken)
        self.state = 1
        
    def predict(self):
        # Predict Taken (True) if state is 2 or 3
        return self.state >= 2
        
    def update(self, actual_outcome):
        if actual_outcome:
            # If Taken, increment state (max 3)
            self.state = min(3, self.state + 1)
        else:
            # If Not Taken, decrement state (min 0)
            self.state = max(0, self.state - 1)

def run_simulation(pattern_name, data):
    predictor = SaturatingCounter()
    correct_guesses = 0
    
    for actual in data:
        prediction = predictor.predict()
        if prediction == actual:
            correct_guesses += 1
        predictor.update(actual)
        
    accuracy = (correct_guesses / len(data)) * 100
    print(f"Pattern: {pattern_name:15} | Accuracy: {accuracy:.2f}%")

# 1. Random Pattern (The Worst Case)
# T, N, T, N, N, T...
random_data = [random.choice([True, False]) for _ in range(10000)]

# 2. Structured Pattern (The Loop)
# T, T, T, T, T, N (Repeat) - Like a loop running 5 times then exiting
loop_data = ([True]*5 + [False]) * 1600

print("--- Branch Prediction Simulator ---")
run_simulation("Random Noise", random_data)
run_simulation("Structured Loop", loop_data)
```

### The Results
If you run this, you will see something striking:

```text
--- Branch Prediction Simulator ---
Pattern: Random Noise    | Accuracy: 50.12%
Pattern: Structured Loop | Accuracy: 83.33%
```

The predictor fails completely on random noise (50% is just a coin flip). But on the loop, it achieves high accuracy because the loop behavior is predictable.

## Why This Matters
This explains a classic StackOverflow question: **Why is processing a sorted array faster than an unsorted array?**

If you iterate over an array and say `if (element > 50)`, the data determines the branch direction.
* **Sorted Array:** `F, F, F, F, T, T, T, T`. The pattern is stable. The predictor guesses right almost every time.
* **Unsorted Array:** `F, T, F, T, T, F, T, F`. The pattern is chaos. The predictor misfires constantly, causing pipeline flushes.

As systems engineers, our job is to write "predictable" code. The less we surprise the CPU, the faster it runs.

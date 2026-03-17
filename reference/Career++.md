# Career++

# Cure for Innumeracy

## Phase 1: Grasping Large Numbers (Scale)

**The Trap:** Humans evolved to count "1, 2, 3, many." We emotionally equate a million ($10^6$) and a billion ($10^9$), even though a million seconds is **11 days** and a billion seconds is **31 years**.

**1\. Theory & Intuition**

* **Powers of 10:** Moving the decimal point is a qualitative shift, not just quantitative.  
* **Volume vs. Linear Scale:** Why a giant ant would collapse under its own weight (Square-Cube Law).  
* **Time Scales:** Understanding nanoseconds (CPU cycle) vs. milliseconds (Disk seek) vs. seconds (Network packet to Europe).

**2\. Discovery (Resources)**

* 📖 **The Book:** *Innumeracy* \- Chapter 1 (Examples and Principles).Cha  
* 🎥 **Video:** [The Powers of Ten](https://www.youtube.com/watch?v=0fKBhvDjuy0) (1977 Eames Film). The classic visualization of scale.  
* 📝 **Interactive:** [The Scale of the Universe 2](https://htwins.net/scale2/). Scroll from Planck length to the Observable Universe.

**3\. The Project: "The Fermi Estimator"**

* **Task:** Create a Jupyter Notebook to solve "Napkin Math" problems using only powers of 10\.  
* **Problem 1:** How many piano tuners are there in Chicago? (The classic Fermi problem).  
* **Problem 2 (Engineering):** How many hard drives does YouTube need to store one year of video uploads? (Estimate users $\\to$ upload rate $\\to$ size/minute $\\to$ replication factor).

## Phase 2: Probability & Coincidence

**The Trap:** We attribute meaning to random events. We think it’s a "miracle" that we met a friend in Paris, ignoring the thousands of people we *didn't* know.

**1\. Theory & Intuition**

* **The Birthday Paradox:** Why you only need 23 people to have a 50% chance of a shared birthday. (Collision probability).  
* **Law of Large Numbers:** "With a large enough sample space, any outrageous thing is likely to happen."  
* **Expected Value:** $E\[X\] \= P(x) \\times Value$. Why lottery tickets are a tax on those bad at math.

**2\. Discovery (Resources)**

* 📖 **The Book:** *Innumeracy* \- Chapter 2 (Probability and Coincidence).  
* 🎥 **Video:** [The Birthday Paradox](https://www.google.com/search?q=https://www.youtube.com/watch%3Fv%3DofTb57a_VpM) (Veritasium). Visualizing the math of collisions.  
* 📝 **Article:** [Understanding the Monty Hall Problem](https://betterexplained.com/articles/understanding-the-monty-hall-problem/). The problem that stumped PhD mathematicians.

**3\. The Project: "The Coincidence Simulator"**

* **Task:** Write a Python script to simulate the Birthday Paradox.  
* **Experiment:** Run 10,000 simulations of groups of 23 people. Count how many times a collision occurs. Prove the math ($\~50.7\\%$) empirically.

## Phase 3: Conditional Probability (The Medical Test Paradox)

**The Trap:** "The test is 99% accurate, and I tested positive. I definitely have the disease." (Wrong. If the disease is rare, you are likely a false positive).

**1\. Theory & Intuition**

* **Bayes' Theorem:** Updating your belief based on new evidence.  
* **Base Rate Neglect:** Ignoring the prevalence of the event.  
* **False Positives vs. False Negatives:** Type I vs. Type II errors.

**2\. Discovery (Resources)**

* 📖 **The Book:** *Innumeracy* \- Chapter 4 (Statistics, Trade-Offs, and Society).  
* 🎥 **Video:** [The Bayesian Trap](https://www.youtube.com/watch?v=R13BD8qKeTg) (Veritasium). Why medical tests confuse doctors.  
* 📝 **Interactive:** [Visualizing Bayes' Theorem](https://seeing-theory.brown.edu/bayesian-inference/index.html) (Brown University).

**3\. The Project: "The Spam Filter"**

* **Task:** Build a Naive Bayes Classifier in Python.  
* **Data:** A small set of strings labeled "Spam" (offer, money, click) and "Ham" (meeting, hello, project).  
* **Logic:** Calculate $P(Spam | "Money")$. Use Bayes theorem to classify a new email.

## Phase 4: Statistics & Pseudoscience

**The Trap:** "Correlation implies Causation" and "Regression to the Mean."

**1\. Theory & Intuition**

* **Regression to the Mean:** Why the "Sophomore Slump" happens. Why highly intelligent parents often have average kids. (It's not genetics failing; it's statistics returning to average).  
* **Selection Bias:** Why "Survivorship Bias" makes you think starting a business is easy (you only hear about the winners).  
* **Standard Deviation ($\\sigma$):** Understanding that "Average" tells you nothing about the spread.

**2\. Discovery (Resources)**

* 📖 **The Book:** *Innumeracy* \- Chapter 5 (Pseudoscience).  
* 🖼️ **Visual:** [Survivorship Bias Plane](https://www.google.com/search?q=https://en.wikipedia.org/wiki/Survivorship_bias%23/media/File:Survivorship-bias.svg). The famous WWII plane diagram.  
* 📖 **Book:** *How to Lie with Statistics* (Darrell Huff). A short companion read to Innumeracy.

**3\. The Project: "The Stock Picker"**

* **Task:** Simulate 1,000 stock pickers flipping coins (Buy/Sell) for 10 rounds.  
* **Result:** Identify the "Gurus" who got 10/10 correct.  
* **Lesson:** Show that in a random distribution, *someone* will look like a genius purely by chance.

## Phase 5: Expected Value & Risk (Engineering Decisions)

**The Trap:** Focusing on the *Worst Case* scenario instead of the *Probable* scenario.

**1\. Theory & Intuition**

* **Availability Heuristic:** We fear plane crashes (spectacular, rare) more than car crashes (boring, common).  
* **Compound Probability:** $P(A \\text{ and } B) \= P(A) \\times P(B)$. Why "Five 9s" of reliability (99.999%) is so hard to achieve.

**2\. Discovery (Resources)**

* 📝 **Blog:** [Jacobolis on Risk](https://www.google.com/search?q=https://jacobolis.com/blog/). (If available, otherwise substitute with general Risk Engineering blogs).  
* 📝 **Article:** [Micromorts](https://en.wikipedia.org/wiki/Micromort). A unit of risk defined as a one-in-a-million chance of death. (Scuba diving \= 5 micromorts).

**3\. The Project: "The SLA Calculator"**

* **Task:** Calculate the availability of a system.  
* **Scenario:** You have a Load Balancer (99.9%), 3 App Servers (99% each), and a Database (99.9%).  
* **Calc:** What is the probability that the *entire* system is down?  
* **Calc:** What is the probability that *at least one* app server is up?

# Pragmatic Math & Computational Thinking

## Phase 1: The Numeracy of Systems (Estimation & Statistics)

**Objective:** Stop trusting the "Average" and start thinking in Distributions and Scale.

**1\. The Pragmatic Theory**

* **The "Average" Lie:** Why Average (Mean) is useless in systems. If 1% of your requests take 10 seconds, your "Average" might look fine, but your system is broken.  
* **Percentiles (P50, P99, P99.9):** The standard for measuring Latency. P99 means "How bad is it for the unluckiest 1% of users?"  
* **Logarithms:** The language of scale.  
  * Why we use Log Scale for charts (visualizing 10ms vs 10,000ms on the same graph).  
  * $O(\\log N)$ means "Doubling the data only adds 1 unit of work."  
* **Modulo Arithmetic:** The engine of distributed systems.  
  * Sharding: ServerID \= UserID % NumberOfServers.  
  * Rolling Windows: Index \= Counter % BufferSize.  
* **Fermi Estimation:** "Back of the Envelope" math. Calculating storage costs or capacity in your head during a meeting.

**2\. The Discovery (Resources)**

* 📝 **The Manifesto:** [Everything You Know About Latency Is Wrong](https://bravenewgeek.com/everything-you-know-about-latency-is-wrong/) (Brave New Geek). A breakdown of why averages hide outliers.  
* 📝 **Visualization:** [Logarithmic Scales Explained](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:logs/x2ec2f6f830c9fb89:log-intro/v/logarithms) (Khan Academy). Just the intuition part.  
* 📝 **Fermi Problems:** [Jeff Dean's Latency Numbers Every Programmer Should Know](https://gist.github.com/jboner/2841832). Memorize the powers of 10 differences between RAM, SSD, and Network.  
* 🎥 **Video:** [How not to measure latency](https://www.youtube.com/watch?v=lJ8ydIuPFeU) (Gil Tene). The definitive talk on the "Coordinate Omission" problem.

**3\. The Exercise: "The Capacity Planner"**

* **Scenario:** You have 10 million daily active users. Each user uploads 5 photos a day. Each photo is 2MB.  
* **Task:** Calculate the storage required for 1 year. Calculate the incoming bandwidth in Gbps. Do this on a napkin without a calculator (using powers of 2 approximations, e.g., $10^6 \\approx 2^{20}$).

## Phase 2: Recursive Thinking (The Infinite Mirror)

**Objective:** Trusting the "Leap of Faith." Understanding self-reference without getting dizzy.

**1\. The Pragmatic Theory**

* **The Leap of Faith:** Assume the function *already works* for a smaller input ($N-1$). You just need to handle the current step.  
* **The Stack:** Recursion isn't magic; it's just a stack of deferred operations.  
* **Tail Recursion:** When recursion is just a while loop in disguise (optimization).  
* **Fractals:** Visualizing recursion to build intuition.

**2\. The Discovery (Resources)**

* 📖 **The Holy Grail:** *The Little Schemer*. (It’s a bizarre, dialogue-based book. Read the first 3 chapters. It forces you to *think* recursively like nothing else).  
* 🎥 **Video:** [Recursion and Fractals](https://www.youtube.com/watch?v=gB9n2gHsHN4) (3Blue1Brown). Beautiful visualization of how simple rules create complex recursive structures.  
* 📝 **Article:** [Recursion: The Leap of Faith](https://www.google.com/search?q=https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1206/lectures/recursion/). Stanford's intro to the mindset.

**3\. The Exercise: "The Recursive Artist"**

* **Task:** Use Python (Turtle graphics) or JS (Canvas) to draw a **Sierpiński Triangle**.  
* **The "Aha":** You don't draw the whole triangle. You write a function that draws a triangle, then calls itself 3 times for the corners.

## Phase 3: Complexity & Amortization (The Cost of Work)

**Objective:** Knowing when $O(N)$ is faster than $O(1)$.

**1\. The Pragmatic Theory**

* **Big O vs. Reality:** Big O ignores constants. In the real world, constants matter. (e.g., iterating a small array is often faster than a Hash Map lookup due to CPU caching).  
* **Amortized Analysis:** The "Rent" concept. Resizing an ArrayList is expensive ($O(N)$), but it happens so rarely that the *average* cost is $O(1)$.  
* **Space-Time Tradeoff:** Caching. We spend memory (Space) to save computation (Time).

**2\. The Discovery (Resources)**

* 📝 **Deep Dive:** [Amortized Analysis Explained](https://www.google.com/search?q=https://medium.com/%40satorusasozaki/amortized-time-explained-43125879581f) (Medium). Using the "Dynamic Array" example.  
* 📝 **Engineering Truth:** [Latency Numbers: The Hidden Cost](https://people.eecs.berkeley.edu/~rcs/research/interactive_latency.html). An interactive infographic showing why "Linear Search in Cache" beats "Binary Search in RAM" for small N.  
* 🎥 **Video:** [P vs NP and Complexity](https://www.youtube.com/watch?v=YX40hbAHx3s) (Hackerdashery). A fun, high-level intuition builder.

**3\. The Exercise: "The Hidden Constant"**

* **Task:** Write a benchmark in C++ or Go.  
* **Compare:** Looking up a value in a HashMap vs. Linear Searching a Vector.  
* **Find the Crossing Point:** At what N (number of elements) does the HashMap actually become faster? (Hint: It's often higher than you think, around N=50-100, due to cache locality).

## Phase 4: Systems Dynamics (Queues, Bottlenecks & Time Series)

**Objective:** Debugging systems using math.

**1\. The Pragmatic Theory**

* **Little's Law:** $L \= \\lambda W$. (Avg items in system \= Arrival Rate $\\times$ Avg Wait Time). This explains why your queue memory explodes when processing slows down even slightly.  
* **The Bottleneck:** A system can only move as fast as its slowest component.  
  * *CPU Bound:* Spending time calculating.  
  * *IO Bound:* Spending time waiting (Network/Disk).  
* **Time Series Patterns:**  
  * *Seasonality:* Traffic spikes at 9 AM and 6 PM.  
  * *Noise vs. Signal:* Is that spike a bug or just a random fluctuation?

**2\. The Discovery (Resources)**

* 📝 **The Framework:** [The USE Method](https://www.brendangregg.com/usemethod.html) (Brendan Gregg). **Utilization, Saturation, Errors**. The mathematical checklist for debugging any server.  
* 📝 **Theory:** [Little's Law for Distributed Systems](https://www.google.com/search?q=https://www.vividcortex.com/resources/littles-law). How to predict queue growth.  
* 🎥 **Video:** [Stop Rate Limiting\! Capacity Management done right](https://www.youtube.com/watch?v=m64SWl9bfvk) (Jon Moore). Using Queueing Theory to handle load.  
* 📝 **Guide:** [Monitoring and Observability](https://sre.google/sre-book/monitoring-distributed-systems/) (Google SRE Book). Reading Time Series charts for golden signals.

**3\. The Exercise: "The Bottleneck Hunt"**

* **Task:** Run a simple web server (Python/Go).  
* **Stress Test:** Use a tool like wrk or locust to flood it with traffic.  
* **Monitor:** Watch CPU usage and Response Time.  
* **Modify:** Add a time.sleep(0.1) (IO Delay) to the handler. Watch CPU usage drop but Latency spike. (This demonstrates Little's Law: Latency increases, Concurrency increases, but Throughput is flat).

# Algorithms, Data Structures, Low-Level Design Track

## Phase 1: The Linear Foundations

*Mastering index manipulation and lookups.*

#### **1\. Arrays & Hashing (The Lookup Pattern)**

* **Focus:** $O(1)$ access and frequency counting.  
* **Problems:**  
  * **Easy:** [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/).  
  * **Easy:** [Valid Anagram](https://leetcode.com/problems/valid-anagram/).  
  * **Easy:** [Two Sum](https://leetcode.com/problems/two-sum/).  
  * **Medium:** [Group Anagrams](https://leetcode.com/problems/group-anagrams/) (Sorting key vs Hash key).  
  * **Medium:** [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (Bucket Sort).  
  * **Medium:** [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) (Prefix/Suffix logic).  
  * **Medium:** [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) (Set as a Graph).  
  * **Medium:** [Determine if Two Strings Are Close](https://leetcode.com/problems/determine-if-two-strings-are-close/) (**2025 Trend:** Frequency Map logic).

#### **2\. Two Pointers (The Shrinking Window)**

* **Focus:** Sorted arrays and meeting in the middle.  
* **Problems:**  
  * **Easy:** [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/).  
  * **Medium:** [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/).  
  * **Medium:** [3Sum](https://leetcode.com/problems/3sum/).  
  * **Medium:** [3Sum With Multiplicity](https://leetcode.com/problems/3sum-with-multiplicity/).  
  * **Medium:** [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) (Greedy shrinking).  
  * **Medium:** [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) (Greedy pairing).  
  * **Hard:** [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/).

#### **3\. Sliding Window (The Subarray)**

* **Focus:** Contiguous subarrays and invariant maintenance.  
* **Problems:**  
  * **Easy:** [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/).  
  * **Medium:** [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/).  
  * **Medium:** [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/).  
  * **Medium:** [Permutation in String](https://leetcode.com/problems/permutation-in-string/).  
  * **Medium:** [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/).  
  * **Hard:** [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/).  
  * **Hard:** [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) (Monotonic Deque).

## Phase 2: The Structures

*Ordering, Parsing, and Hierarchies.*

### Stacks (LIFO & Monotonic)

* **Focus:** Parsing logs, nested structures, and Next Greater Element.  
* **Problems:**  
  * **Easy:** [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/).  
  * **Medium:** [Min Stack](https://leetcode.com/problems/min-stack/).  
  * **Medium:** [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) (Monotonic).  
  * **Medium:** [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/).  
  * **Medium:** [Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions/) (**Must Do**).  
  * **Medium:** [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/).  
  * **Medium:** [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/).  
  * **Medium:** [Decode String](https://leetcode.com/problems/decode-string/).  
  * **Hard:** [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/).

### Heaps & Priority Queues (Ordering)

* **Focus:** Min/Max retrieval and Stream medians.  
* **Problems:**  
  * **Easy:** [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/).  
  * **Medium:** [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/).  
  * **Medium:** [Task Scheduler](https://leetcode.com/problems/task-scheduler/).  
  * **Medium:** [Design Twitter](https://leetcode.com/problems/design-twitter/).  
  * **Medium:** [Reorganize String](https://leetcode.com/problems/reorganize-string/).  
  * **Medium:** [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/).  
  * **Hard:** [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/).  
  * **Hard:** [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/).  
  * **Hard:** [IPO](https://leetcode.com/problems/ipo/).

### Intervals (Time Management)

* **Focus:** Sorting by start time and merging.  
* **Problems:**  
  * **Easy:** [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/).  
  * **Medium:** [Merge Intervals](https://leetcode.com/problems/merge-intervals/).  
  * **Medium:** [Insert Interval](https://leetcode.com/problems/insert-interval/).  
  * **Medium:** [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/).  
  * **Medium:** [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/).  
  * **Medium:** [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/).  
  * **Hard:** [Employee Free Time](https://leetcode.com/problems/employee-free-time/).

## Phase 3: Search & Sort

*Finding data in non-linear spaces.*

### Binary Search (The Answer Space)

* **Focus:** Search on arrays vs search on value range.  
* **Problems:**  
  * **Easy:** [Binary Search](https://leetcode.com/problems/binary-search/).  
  * **Medium:** [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/).  
  * **Medium:** [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/).  
  * **Medium:** [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/).  
  * **Medium:** [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/).  
  * **Medium:** [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/).  
  * **Medium:** [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/).  
  * **Hard:** [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/).  
  * **Hard:** [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/).

## Phase 4: Trees & Graphs

*Hierarchy and Connectivity.*

### Trees (DFS/BFS)

* **Focus:** Recursion, Depth, and Levels.  
* **Problems:**  
  * **Easy:** [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/).  
  * **Easy:** [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/).  
  * **Easy:** [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/).  
  * **Easy:** [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/).  
  * **Easy:** [Same Tree](https://leetcode.com/problems/same-tree/).  
  * **Easy:** [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/).  
  * **Medium:** [Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/).  
  * **Medium:** [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/).  
  * **Medium:** [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/).  
  * **Medium:** [Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/).  
  * **Hard:** [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/).  
  * **Hard:** [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/).

### Tries (Prefix Trees)

* **Focus:** String prefixes and wildcards.  
* **Problems:**  
  * **Medium:** [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/).  
  * **Medium:** [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/).  
  * **Medium:** [Replace Words](https://leetcode.com/problems/replace-words/).  
  * **Hard:** [Word Search II](https://leetcode.com/problems/word-search-ii/).

### Graphs (Connectivity & Path Finding)

* **Focus:** BFS/DFS, Topo Sort, Dijkstra, Union-Find.  
* **Problems:**  
  * **Medium:** [Number of Islands](https://leetcode.com/problems/number-of-islands/).  
  * **Medium:** [Max Area of Island](https://leetcode.com/problems/max-area-of-island/).  
  * **Medium:** [Clone Graph](https://leetcode.com/problems/clone-graph/).  
  * **Medium:** [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/).  
  * **Medium:** [Course Schedule](https://leetcode.com/problems/course-schedule/) (Topo Sort).  
  * **Medium:** [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/).  
  * **Medium:** [Redundant Connection](https://leetcode.com/problems/redundant-connection/) (Union-Find).  
  * **Medium:** [Network Delay Time](https://leetcode.com/problems/network-delay-time/) (Dijkstra).  
  * **Medium:** [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/).  
  * **Hard:** [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) (Topo Sort).  
  * **Hard:** [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) (Dijkstra on Grid).

## Phase 5: The Specialized

*Optimization, Probability, and Linked Lists.*

### Dynamic Programming & Greedy

* **Focus:** Subproblems and local optimums.  
* **Problems:**  
  * **Easy:** [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/).  
  * **Medium:** [Coin Change](https://leetcode.com/problems/coin-change/).  
  * **Medium:** [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/).  
  * **Medium:** [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/).  
  * **Medium:** [Word Break](https://leetcode.com/problems/word-break/).  
  * **Medium:** [Unique Paths](https://leetcode.com/problems/unique-paths/).  
  * **Medium:** [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/).  
  * **Medium:** [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/).  
  * **Medium:** [House Robber](https://leetcode.com/problems/house-robber/).  
  * **Medium:** [House Robber II](https://leetcode.com/problems/house-robber-ii/).  
  * **Medium:** [Jump Game](https://leetcode.com/problems/jump-game/).  
  * **Medium:** [Jump Game II](https://leetcode.com/problems/jump-game-ii/).

### Probability & Sampling

* **Focus:** Streaming algorithms and Randomness.  
* **Problems:**  
  * **Medium:** [Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/) (Reservoir Sampling).  
  * **Medium:** [Random Pick Index](https://leetcode.com/problems/random-pick-index/).  
  * **Medium:** [Shuffle an Array](https://leetcode.com/problems/shuffle-an-array/).  
  * **Medium:** [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/).

### Linked Lists

* **Focus:** Pointers and Reversal.  
* **Problems:**  
  * **Easy:** [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/).  
  * **Easy:** [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/).  
  * **Easy:** [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/).  
  * **Medium:** [Reorder List](https://leetcode.com/problems/reorder-list/).  
  * **Medium:** [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/).  
  * **Medium:** [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/).  
  * **Medium:** [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/).

## Phase 6: The 2025 Real-World Drop

*Problems verified from Feb-Mar 2025 Interview Loops (Microsoft, Amazon, Google, Meta).*

### Google: The "Hidden" Logic

*Google is moving away from pure graph/DP toward "Grid & Parsing" hybrids.*

* **Hard:** [Race Car](https://leetcode.com/problems/race-car/) (BFS on an infinite state space).  
* **Medium:** [Snapshot Array](https://leetcode.com/problems/snapshot-array/) (Design \+ Binary Search).  
* **Medium:** [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) (Queue/HashMap Design).  
* **Medium:** [Step-By-Step Directions From a Binary Tree Node to Another](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/) (LCA \+ Traversal).  
* **Hard:** [Guess the Word](https://leetcode.com/problems/guess-the-word/) (Minimax / Logic).

### Meta: Arrays & "K" Variants

*Meta continues to heavily favor variations of "Top K", "Valid Strings", and "Sparse Vectors".*

* **Easy:** [Buildings With an Ocean View](https://leetcode.com/problems/buildings-with-an-ocean-view/) (Monotonic Stack \- **Extremely Frequent**).  
* **Medium:** [Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/).  
* **Medium:** [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/).  
* **Medium:** [Dot Product of Two Sparse Vectors](https://leetcode.com/problems/dot-product-of-two-sparse-vectors/) (Design / Array).  
* **Medium:** [Simplify Path](https://leetcode.com/problems/simplify-path/) (Stack).  
* **Hard:** [Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/) (Solve in $O(\\log N)$).

### Amazon: Trees & Leadership

*Coding questions often involve file systems or tree properties.*

* **Medium:** [Analyze User Website Visit Pattern](https://leetcode.com/problems/analyze-user-website-visit-pattern/) (HashMap Heavy).  
* **Medium:** [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) (Trie / Sorting).  
* **Medium:** [Count Univalued Subtrees](https://www.google.com/search?q=https://leetcode.com/problems/count-univalued-subtrees/) (Tree DFS).  
* **Medium:** [All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) (Graph conversion).

### Uber/DoorDash: The Graph Gauntlet

*Focus on Intervals and heavy Graph traversals.*

* **Hard:** [Bus Routes](https://leetcode.com/problems/bus-routes/) (BFS optimization).  
* **Hard:** [Text Justification](https://leetcode.com/problems/text-justification/) (String Manipulation Hell).  
* **Medium:** [Design Underground System](https://leetcode.com/problems/design-underground-system/) (HashMap Design).  
* **Medium:** [Meeting Scheduler](https://leetcode.com/problems/meeting-scheduler/) (Interval Intersection).

## Phase 7: The Hybrid / LLD Trend

*Coding rounds that turn into Mini-System Design.*

### Concurrency & Design

*These require thread-safety or class design, not just algorithms.*

* **Medium:** [Design Hit Counter](https://leetcode.com/problems/design-hit-counter/) (Scalability discussion).  
* **Medium:** [Design Circular Deque](https://leetcode.com/problems/design-circular-deque/) (Ring Buffer).  
* **Medium:** [Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/).  
* **Medium:** [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/).  
* **Hard:** [Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/) (Trie \+ Map).

## Phase 8: Low-Level Design (The "Code It" Round)

*Turning vague requirements into working, extensible classes.*

### The Theory (Don't Skip This)

*Before designing, you must know the rules of the road.*

* **Theory:**  
  * **SOLID Principles:** If you violate "Open-Closed" (modifying existing code to add a feature instead of extending it), you fail.  
  * **Design Patterns:**  
    * **Strategy:** For different pricing algorithms (Uber/Parking Lot).  
    * **State:** For complex state machines (Vending Machine/Elevator/ATM).  
    * **Observer:** For notification systems (Group Chat/Stock Ticker).  
    * **Factory/Singleton:** Basic object creation.  
  * **Concurrency:** ReentrantLock, synchronized, CompletableFuture (Java), or Mutex/Channels (Go).  
* **Discovery:**  
  * 📝 **Refactoring Guru:** [Design Patterns Catalog](https://refactoring.guru/design-patterns).  
  * 🎥 **Video:** [SOLID Principles \~ Christopher Okhravi](https://www.google.com/search?q=https://www.youtube.com/playlist%3Flist%3DPLwLLcwQk52tKzJc9D7J8b6c0g9k8a2_C-).

### The "Big 5" Real-World Problems

*These appear in 80% of LLD interviews.*

**Problem A: Design an Elevator System (Your Request)**

* **The Trap:** Designing for just one elevator. Real interviews ask for a **Dispatcher** managing a *bank* of elevators.  
* **Key Challenges:**  
  * **Algorithm:** FCFS (Bad) vs. LOOK/SCAN (Disk Scheduling algo applied to floors).  
  * **State Machine:** IDLE $\\to$ MOVING\_UP $\\to$ STOPPED\_OPEN\_DOOR.  
  * **Optimization:** assigning the "Best" elevator (closest moving in the same direction).  
* **The "Delta" (Senior Level):** How do you handle a "VIP" elevator? If you used the **Strategy Pattern** for dispatching, this is a 1-line code change. If you used if/else, you have to rewrite the system.

**Problem B: Design a Parking Lot**

* **The Context:** Amazon/Microsoft classic.  
* **Key Challenges:**  
  * **Spot Allocation:** Finding the nearest free spot for a specific vehicle type (Compact, Large, Motorcycle).  
  * **Pricing:** Variable rates (First hour $4, then $2). This requires the **Strategy Pattern**.  
  * **Concurrency:** Two cars enter different gates at the exact same millisecond. Who gets the last spot? (Requires Mutex/Locks).

**Problem C: Design a Movie Ticket Booking System (BookMyShow)**

* **The Context:** Concurrency heavy.  
* **Key Challenges:**  
  * **Locking:** User A selects Seat D4. User B selects Seat D4. How do you prevent double booking? (Optimistic vs. Pessimistic Locking).  
  * **Search:** Finding 4 contiguous seats.

**Problem D: Design a Vending Machine / ATM**

* **The Context:** The ultimate **State Design Pattern** test.  
* **Key Challenges:**  
  * **States:** IdleState $\\to$ SelectionState $\\to$ MoneyInsertedState $\\to$ DispensingState.  
  * **Inventory:** Managing count of items and change (coins/notes) inside the machine.

**Problem E: Design Splitwise (Expense Sharing)**

* **The Context:** Atlassian/Uber.  
* **Key Challenges:**  
  * **Simplification:** User A owes B $10. B owes C $10. The system should tell A to pay C $10 directly (Graph Simplification / Max Flow).  
  * **Split Types:** Equal, Exact Amount, Percentage (Strategy Pattern).

### The "Game" Problems

*Often asked to test clean logic and separation of concerns.*

* **Design Chess / Tic-Tac-Toe:**  
  * **Focus:** Representing the Board, checking Win Conditions efficiently ($O(1)$ for Tic-Tac-Toe), and Command Pattern for "Undo" functionality.  
* **Design Snake & Ladder:**  
  * **Focus:** Injecting the Dice (to make it testable), define Jumper entities (Snakes/Ladders).

### LLD Resources (Specific)

* **Course:** [Grokking the Low Level Design Interview](https://www.educative.io/courses/grokking-the-object-oriented-design-interview) (Standard text).  
* **YouTube Channel:** **Concept && Coding** (Shreyansh Jain) – He has the best breakdown of the Elevator and Parking Lot code in Java.  
* **Repo:** [Low Level Design Primer](https://github.com/prasadgujar/low-level-design-primer) (Python/Java/Go implementations of the above).

## Phase 9: Assorted Questions

### Robinhood: Design a backend system for a trading application that displays real-time stock price charts.

1. **Ingestion:** Your system connects to an external exchange (like NASDAQ) via a TCP/UDP stream to receive raw tick data (price updates) for thousands of symbols.  
2. **Processing:** You must aggregate this raw data into different time-based resolutions (candlesticks): 1-minute, 5-minute, 1-hour, and Daily.  
3. **Serving:** When a user opens the app and clicks a ticker (e.g., AAPL), the system must serve the historical chart data for the requested resolution with low latency."

**Key Challenges They Were Testing:**

* **Write-Heavy vs. Read-Heavy:** The system must write millions of incoming data points per second (Write-Heavy) but also serve millions of users reading charts (Read-Heavy).  
* **Downsampling (Rollups):** You cannot store or send every single trade to the mobile phone. You need a mechanism to convert raw "ticks" into "OHLC" (Open, High, Low, Close) bars.  
  * *The question implies:* Do you compute these rollups on the fly (slow reads) or pre-compute them as data comes in (complex writes)? (Answer: Pre-compute/Materialized Views).  
* **Database Choice:** Standard SQL (MySQL/PostgreSQL) usually struggles here. They were looking for **Time-Series Databases** (e.g., InfluxDB, TimescaleDB, Cassandra).  
* **API Design:** How do you push updates to the phone?  
  * *Polling:* The app asks every 1 second (inefficient).  
  * *WebSockets/Server-Sent Events:* The server pushes price changes immediately (preferred).

### Google: Merging Sorted Streams (with Latency/Network constraints)

You are given two Connection objects, each representing a live socket connection to a stock exchange. Each connection provides a stream of (timestamp, price) tuples.

* **Constraint 1:** Within a single stream, timestamps are guaranteed to be monotonically increasing ($t\_1 \< t\_2 \< t\_3 \\dots$).  
* **Constraint 2:** There is no guarantee of synchronization between the two streams. Stream A might deliver a packet with $t=100$, while Stream B is lagging and just delivered $t=95$.

Write an iterator or generator that yields a **single** unified stream of updates strictly sorted by timestamp.

**Key Challenges They Were Testing**:

If this was a pure **coding** round, it was likely an Iterator problem:

* **The Problem:** You cannot simply peek at Stream A, see $t=100$, and output it. Why? Because Stream B might be silent right now, but 10 milliseconds later it could send a packet with $t=99$. If you already outputted $t=100$, you have broken the sort order.  
* **The Solution:** This usually requires a **Buffer** or a **Peeking Iterator**.  
  1. You must read one item from *both* streams first.  
  2. Compare the heads of both streams.  
  3. Emit the smaller one.  
  4. Refill the buffer only for the stream you just emitted from.

If this was a **Systems/Concurrency** round, they were asking about **Watermarks**:

* *Question:* "What if Stream A is very fast and Stream B stops sending data for 5 minutes? Do we block the whole system?"  
* *Answer:* You need a heuristic (a timeout or watermark). If Stream B is silent for X seconds, you assume it has nothing older than the current time minus X, or you accept that data might arrive "late" and decide how to handle out-of-order data (drop it or re-process)

### Google: Design a Fault-Tolerant "Virtual Global Order Book" (improved version of the above question)

We connect to 10+ different exchanges (NASDAQ, NYSE, Tokyo, London, etc.). Each exchange provides a high-throughput stream of trade executions via UDP multicast.

**Your Goal:** Build a distributed system that ingests these disjoint streams and publishes a single, globally sorted 'Tape' (unified stream) to downstream consumers.

**The Real-World Constraints:**

1. **No Global Clock:** You cannot trust the timestamp from the exchange perfectly (clock skew exists). You rely on your local reception time, but network jitter messes this up.  
2. **UDP Packet Loss:** We use UDP for speed. Packets drop. However, streams usually have sequence numbers. If you miss Sequence \#50 from NYSE, how do you handle the global sort? Do you wait? For how long?  
3. **Connection Failure:** The connection to Tokyo goes dark. Do you halt the global stream (impacting availability) or continue publishing partial data (impacting correctness)?  
4. **Scale:** The total volume is 5 million messages/second.

**What This Tests (The "Senior" Level Signals):**

* **Watermarking & Windowing:** You cannot sort an infinite stream. You need to define a time window (e.g., "We sort data in 100ms buckets"). How do you determine when a bucket is "done" and ready to be flushed?  
* **Head-of-Line Blocking:** If you are strictly sorting by time, a delayed packet from one slow exchange halts the entire system.  
  * *Solution:* You must implement a "Max Delay" heuristic. If data is late by $\> t\_{max}$, we publish without it and send the late data to a "correction stream" later.  
* **Sequence Gap Handling:** If you see Seq \#51 but missed \#50, you buffer \#51 and send a NACK (Negative Acknowledgement) to re-request \#50.

### More Interview Questions in this Domain

These questions sit at the intersection of **FinTech**, **High-Concurrency**, and **Distributed Systems**.

1\. The Limit Order Book (The "Holy Grail" Question)

* **Prompt:** Design a data structure to maintain the buy/sell orders for a stock. It must support add\_order(), cancel\_order(), and match\_order() in $O(1)$ or $O(\\log N)$ time.  
* **The Twist:** Now make it thread-safe for a multi-core engine processing 1 million orders/sec.  
* **Key Concept:** Double Linked Lists \+ Hash Maps for $O(1)$ cancellation; minimizing lock contention.

2\. The "Flash Crash" Detector (Streaming Anomaly Detection)

* **Prompt:** You have a stream of stock prices. You need to trigger an alert if the price drops by more than 5% within any rolling 5-minute window.  
* **The Twist:** You have 10,000 symbols. You cannot store all history.  
* **Key Concept:** Sliding Window algorithms, Deques (Double-ended queues) maintaining monotonic properties.

3\. High-Frequency Counter / Rate Limiter

* **Prompt:** Design a rate limiter for a trading API (e.g., "User can only make 5 trades per second").  
* **The Twist:** This is a distributed system with 50 server nodes. The user's requests might hit different nodes. The limit must be strictly enforced globally.  
* **Key Concept:** Token Bucket algorithm, Redis (with Lua scripts for atomicity), or a "gossip" protocol for approximate counting.

4\. The "Top K" Active Stocks

* **Prompt:** Display the top 10 most traded stocks in real-time on a dashboard.  
* **The Twist:** The volume is massive. You cannot aggregate everything in one DB.  
* **Key Concept:** Count-Min Sketch (probabilistic data structure) or MapReduce style aggregation (Map on edge nodes $\\rightarrow$ Reduce on central node).

5\. Distributed ID Generation

* **Prompt:** Every trade needs a unique 64-bit ID. The ID should be roughly sortable by time (so we know which trade happened first).  
* **The Twist:** You have data centers in NY, London, and Tokyo. They cannot coordinate with a central master DB for every ID (too slow).  
* **Key Concept:** Twitter Snowflake ID approach (Bits for Timestamp \+ Bits for Datacenter ID \+ Bits for Sequence).

6\. Smart Order Router (Graph/Network Flow)

* **Prompt:** A user wants to buy 100 shares of AAPL. You can buy it from Exchange A ($150.00), Exchange B ($150.01), or a "Dark Pool".  
* **The Twist:** Exchange A has a 5ms latency, Exchange B has 1ms latency. Where do you route the order to maximize fill probability and best price?  
* **Key Concept:** Dijkstra’s algorithm modified for latency/probability weights; Load balancing.

7\. Exactly-Once Payment Processing

* **Prompt:** Design a system to transfer funds from a user's bank to their brokerage wallet.  
* **The Twist:** The system crashes immediately after sending the "deduct money" request to the bank. When it restarts, how do you ensure you don't deduct it again?  
* **Key Concept:** Idempotency keys, Two-Phase Commit (2PC), or Saga patterns.

8\. The "Thundering Herd" Market Open

* **Prompt:** At 9:30 AM EST, the market opens. 5 million users log in simultaneously to check their portfolio value.  
* **The Twist:** How do you cache this? If the price changes every second, your cache is always stale.  
* **Key Concept:** Cache Stampede prevention, Coalescing requests (collapsing 1000 requests for the same data into 1 backend call).

9\. Historical Data Replay (Time Travel)

* **Prompt:** We found a bug in our trading algorithm. We need to replay yesterday's market data exactly as it happened to debug it.  
* **The Twist:** The replay must respect the original timing delays between messages (e.g., if Message B came 50ms after Message A, the replay must pause for 50ms).  
* **Key Concept:** Event Sourcing, storing relative time deltas, high-precision timers.

10\. Dependency Resolution (Build System)

* **Prompt:** A complex financial derivative (an Option) depends on the price of the underlying stock. If the Stock price changes, the Option price must re-calculate.  
* **The Twist:** You have a chain of dependencies (Stock $\\rightarrow$ Index $\\rightarrow$ ETF $\\rightarrow$ Option). How do you efficiently propagate updates without re-calculating everything unnecessarily?  
* **Key Concept:** Directed Acyclic Graphs (DAGs), Topological Sort, Reactive Programming (spreadsheets).

# Single Node Systems

## Phase 1: The Hardware (CPU, Branch Prediction & Speculation)

**Objective:** Understand the "lying" CPU. It executes instructions out of order, guesses branches, and speculates on memory.

**1\. Theory & Math**

* **The Pipeline:** Fetch $\\to$ Decode $\\to$ Execute $\\to$ Write-back.  
* **CPI (Cycles Per Instruction):** How Pipeline Stalls and Pipeline Flushes (due to bad branch prediction) kill performance.  
* **Speculative Execution:** Executing code before we know if we need it (Spectre/Meltdown foundations).

**2\. Discovery (The Library)**

* 📖 **The Bible (Optimization):** [Agner Fog’s Software Optimization Resources](https://www.agner.org/optimize/). Specifically the "Microarchitecture" PDF. This is what C++ compiler engineers read.  
* 📖 **Textbook:** *Computer Systems: A Programmer's Perspective (CSAPP)*. Read **Chapters 4 (Processor Architecture)** and **5 (Optimizing Program Performance)**.  
* 📝 **Visual Deep Dive:** [Branch Prediction \- Why is processing a sorted array faster?](https://stackoverflow.com/questions/11227809/why-is-processing-a-sorted-array-faster-than-processing-an-unsorted-array). The top answer is a masterclass in modern CPU architecture.  
* 📝 **Paper:** [Spectre Attacks: Exploiting Speculative Execution](https://spectreattack.com/spectre.pdf). Read Section 1 & 2 to understand how CPUs "guess" ahead.  
* 📝 **Article:** [A Journey Into the Linux Scheduler](https://os.phil-opp.com/async-await/). Explains how the CPU context switches at a register level.

**3\. The Project: "The Branch Predictor Simulator"**

* **Task:** Implement a **2-bit Saturating Counter** in Python.  
* **Simulation:** Feed it a stream of Taken (T) and Not Taken (N) branches.  
* **Experiment:** Compare a random pattern T, N, N, T, N vs. a structured pattern T, T, N, T, T, N (like a loop). Measure the misprediction rate.

## Phase 2: The Memory Hierarchy (Caching & Coherence)

**Objective:** Mastering the "Distance to Data." L1 is your pocket; RAM is Mars.

**1\. Theory & Math**

* **The Hierarchy:** L1 (SRAM, \~1ns) $\\to$ L2 $\\to$ L3 $\\to$ Main Memory (DRAM, \~100ns).  
* **Cache Lines:** The 64-byte unit of transfer. Understanding Spatial Locality.  
* **MESI Protocol:** The state machine (Modified, Exclusive, Shared, Invalid) that maintains coherence between cores.  
* **False Sharing:** When two threads write to different variables that happen to sit on the same cache line.

**2\. Discovery (The Library)**

* 📝 **The Absolute Standard:** [What Every Programmer Should Know About Memory](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf) (Ulrich Drepper). **Read Section 3 (CPU Caches)** and **Section 6 (NUMA)**.  
* 📝 **Interactive Visualization:** [Memory Latency Numbers Every Programmer Should Know](https://gist.github.com/jboner/2841832).  
* 🎥 **Talk:** [False Sharing and the MESI Protocol](https://www.google.com/search?q=https://www.youtube.com/watch%3Fv%3DWzYx77mX6LU) (Scott Meyers). The best explanation of why "shared state" kills performance.  
* 📝 **Deep Dive:** [Gallery of Processor Cache Effects](https://igoro.com/archive/gallery-of-processor-cache-effects/). Code examples showing how "Stride Length" impacts L1/L2 hits.

**3\. The Project: "The False Sharing Demo"**

* **Task:** Spawn 4 threads. Each increments an integer in a shared array long\[\] counters.  
* **Scenario A (Bad):** counters\[0\], counters\[1\], counters\[2\], counters\[3\] (All on the same 64-byte cache line).  
* **Scenario B (Good):** Pad the struct so each counter is 64 bytes apart (alignas(64) in C++).  
* **Result:** Scenario A will be 10x slower due to "Cache Line Bouncing" (The MESI protocol invalidating the line constantly).

## Phase 3: The Build Process (Linkers, Loaders & ELF)

**Objective:** What happens between writing main() and the process actually starting?

**1\. Theory & Math**

* **ELF Format:** Sections (.text code, .data variables, .bss uninitialized) vs. Segments (Loadable chunks).  
* **Dynamic Linking:** How the **PLT** (Procedure Linkage Table) and **GOT** (Global Offset Table) resolve printf at runtime.  
* **Startup:** \_start $\\to$ \_\_libc\_start\_main $\\to$ constructors $\\to$ main.

**2\. Discovery (The Library)**

* 📖 **Book:** [Linkers and Loaders](https://www.iecc.com/linker/) (John R. Levine).  
* 📝 **Tutorial:** [A Whirlwind Tutorial on Creating Really Teensy ELF Executables for Linux](https://www.muppetlabs.com/~breadbox/software/tiny/teensy.html). Learn to build a binary byte-by-byte.  
* 📝 **Article:** [Linux x86 Program Start Up](http://dbp-consulting.com/tutorials/debugging/linuxProgramStartup.html). Visualizing the stack before main runs.  
* 📝 **Paper:** [How to Write a Shared Library](https://akkadia.org/drepper/dsohowto.pdf) (Ulrich Drepper).

**3\. The Projects: "The Binary Surgeon"**

* **Task A (Inspection):** Use readelf \-a and nm to dissect a binary. Find the entry point address.  
* **Task B (LD\_PRELOAD):** Write a shared library that overrides rand() to always return 42. Inject it into a running program using export LD\_PRELOAD=./hacker.so.

## Phase 4: Operating Systems & Syscalls (The Toolsmith)

**Objective:** Recreating core Unix utilities to master Syscalls and File I/O.

**1\. Theory & Math**

* **Syscalls:** The bridge between Ring 3 (User) and Ring 0 (Kernel).  
* **VFS (Virtual File System):** Inodes, File Descriptors, and Page Cache buffering.

**2\. Discovery (The Library)**

* 📖 **Book:** [The Linux Programming Interface](https://man7.org/tlpi/) (Michael Kerrisk). The comprehensive reference for Linux syscalls.  
* 📖 **Book (Free):** [Operating Systems: Three Easy Pieces (OSTEP)](https://pages.cs.wisc.edu/~remzi/OSTEP/).  
* 📝 **Guide:** [Beej's Guide to Unix IPC](https://beej.us/guide/bgipc/).  
* 🎥 **Video:** [The magic of 'ls'](https://www.google.com/search?q=https://www.youtube.com/watch%3Fv%3DkYgHpVpVgOK) (Explaining strace ls).

**3\. The Projects: "Unix Utils from Scratch"**

* **Tiny-LS:** Use opendir, readdir, and stat.  
* **Tiny-WC:** Count bytes/lines. **Challenge:** Compare reading 1 byte at a time vs 4KB blocks (Page Size).  
* **Tiny-Tail:** Implement tail \-f. Use inotify (Linux) to watch for file changes event-driven style.  
* **Tiny-Shell:** Implement fork, exec, wait, and dup2 (for pipes |).

## Phase 5: Concurrency (Threads & Folly)

**Objective:** Managing execution resources efficiently.

**1\. Theory & Math**

* **User vs. Kernel Threads:** 1:1 (Pthreads) vs M:N (Go Runtime).  
* **Context Switching:** The cost of swapping registers (approx 1-5 microseconds).  
* **Thread Pools:** CPU-bound pools (count \= NumCores) vs IO-bound pools.

**2\. Discovery (The Library)**

* 📝 **Documentation:** [Folly Executors](https://github.com/facebook/folly/blob/main/folly/docs/Executors.md). Understand CPUThreadPoolExecutor vs IOThreadPoolExecutor.  
* 📝 **Article:** [Go's work-stealing scheduler](https://rakyll.org/scheduler/). How M:N threading works in practice.  
* 📝 **Article:** [The C10k Problem](http://www.kegel.com/c10k.html). The history of Event Loops.

**3\. The Project: "Green Threads Scheduler"**

* **Task:** Implement "User Level Threads" in C.  
* **Mechanism:** Use ucontext.h (or assembly) to swap stack pointers manually.  
* **Scheduler:** A simple Round-Robin loop that yields control between tasks.

## Phase 6: Storage (SSD & Engines)

**Objective:** Optimizing for the physical medium (Flash).

**1\. Theory & Math**

* **Write Amplification:** $WA \= \\frac{\\text{Data Written to Flash}}{\\text{Data Written by Host}}$.  
* **Data Structures:** B-Trees (Read heavy) vs. LSM Trees (Write heavy).

**2\. Discovery (The Library)**

* 📝 **Paper:** [The Log-Structured Merge-Tree](https://www.cs.umb.edu/~poneil/lsmtree.pdf) (O'Neil).  
* 📝 **Paper:** [WiscKey: Separating Keys from Values in SSD-conscious Storage](https://www.usenix.org/system/files/conference/fast16/fast16-papers-lu.pdf).  
* 📖 **Book:** *Database Internals* (Alex Petrov). Read Part 1 on Storage Engines.  
* 📝 **Deep Dive:** [B-Trees, LSM-Trees, and Write Amplification](https://tikv.org/deep-dive/key-value-engine/b-tree-vs-lsm/).

**3\. The Project: "Mini-Grep" (mmap)**

* **Task:** Implement grep.  
* **Optimization:** Use mmap to map the file into virtual memory instead of using read(). Benchmark the difference on a 10GB file.

## Phase 7: Virtualization (Containers & Cgroups)

**Objective:** Building the Cloud on localhost.

**1\. Theory & Math**

* **Namespaces:** PID (Process ID), NET (Network), MNT (Mount), UTS (Hostname).  
* **Cgroups:** Limiting CPU and RAM usage.

**2\. Discovery (The Library)**

* 🎥 **Must Watch:** [Containers from Scratch](https://www.youtube.com/watch?v=8fi7uSYlOdc) (Liz Rice). She builds Docker in Go live.  
* 📝 **Kernel Docs:** [Control Groups v2](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html).  
* 📝 **Article:** [What is a Container? (Julia Evans)](https://jvns.ca/blog/2016/10/10/what-even-is-a-container/).

**3\. The Capstone Projects**

* **Tiny-Docker:**  
  * Use unshare (Linux command) or syscall.Syscall(CLONE\_NEWPID) in Go.  
  * chroot into a folder with an Alpine Linux filesystem.  
  * Mount the /proc filesystem.  
* **Tiny-K8s (Control Loop):**  
  * Write a program that takes a YAML file (desired\_state).  
  * Runs a loop: current\_state \= get\_running\_processes().  
  * diff \= desired \- current.  
  * if diff: apply\_changes().

## Phase 8: Modern Linux Primitives

**Objective:** Master the shift from synchronous syscalls to high-performance, asynchronous kernel interaction.

* 1\. Theory & Math  
  * **The Cost of a Syscall:** Understanding the overhead of context switching and memory copying in traditional `read()`/`write()` loops.  
  * **Async I/O Evolution:** From `select`/`poll` to `epoll`, and finally the Ring Buffer model of `io_uring`.  
  * **Kernel Programmability:** Understanding how **eBPF** allows safe, JIT-compiled code execution inside the kernel for networking and observability.  
* 2\. Discovery (The Library)  
  * **The Manual:** *Lord of the Io\_uring* (Axboe). The definitive guide to the `io_uring` interface.  
  * **The Tool:** `bpftrace`. A high-level tracing language for Linux eBPF.  
  * **Reading:** *The ScyllaDB io\_uring guide*. Why the next generation of databases is moving to a thread-per-core, async I/O model.  
* 3\. The Project: "The Zero-Copy Echo Server"  
  * **Task:** Build a TCP echo server in C or Zig using `io_uring`.  
  * **Challenge:** Implement the `IORING_OP_READ` and `IORING_OP_WRITE` operations without any blocking syscalls in the main loop.  
  * **Comparison:** Benchmark throughput against a standard `epoll`\-based server.

## Phase 9: Hardware Acceleration (SIMD & Bit-Packing)

* **Objective:** Use data-level parallelism to maximize single-core throughput.  
* **Theory:** SIMD (Single Instruction, Multiple Data) on AVX-512/NEON; Succinct Data Structures that approach information-theoretic limits.  
* **Project:** Build a SIMD-accelerated string search or a bit-packed Cuckoo Filter.

# Building Blocks of Scale

## Phase 1: The Request & Coordination Layer

**Objective:** How do you handle the first entry point of a request and ensure the cluster knows "who is where"?

1\. Theory & Intuition

* **The Power of Hashing:** Understanding **Consistent Hashing** to minimize data movement when nodes join or leave.  
* **Load Balancing Strategies:** Moving beyond Round Robin to **Least Connections** and **Shuffle Sharding** to isolate "poison pill" requests.  
* **Service Discovery & Consensus:** Why systems like **Zookeeper** or **Etcd** are the "Source of Truth" for cluster state.

2\. Discovery (Resources)

* **🎥 Video:** [MIT 6.824: Distributed Systems \- Introduction](https://www.google.com/search?q=https://www.youtube.com/watch%3Fv%3DU3NInM4S2S8)  
* **📝 Blog:** [Consistent Hashing (Tom White)](http://www.tom-e-white.com/2007/11/consistent-hashing.html)  
* **📝 Paper:** [AWS Builders' Library: Workload Isolation using Shuffle Sharding](https://aws.amazon.com/builders-library/workload-isolation-using-shuffle-sharding/)  
* **📄 Paper:** [The Chubby Lock Service for Loosely-Coupled Distributed Systems (Google)](https://research.google.com/archive/chubby-osdi06.pdf)

## Phase 2: The Storage Primitives (The "State" Block)

**Objective:** Deciding how to store data based on the access pattern (Read-heavy vs. Write-heavy).

1\. Theory & Intuition

* **LSM Trees vs. B-Trees:** The math of **Write Amplification**. Why LSM (used in Cassandra/RocksDB) is the king of high-speed ingestion.  
* **Distributed File Systems:** The "Master/Chunkserver" pattern popularized by **GFS**.  
* **Global Clocks & Time:** Why you can't trust system time and how Google uses **TrueTime** to achieve strict serializability.

2\. Discovery (Resources)

* **📖 The Bible:** [Designing Data-Intensive Applications (Chapter 3\)](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/)  
* **📄 Paper:** [The Google File System (SOSP 2003\)](https://research.google.com/archive/gfs-sosp2003.pdf)  
* **🎥 Video:** [LSM Trees vs B-Trees (Mark Callaghan)](https://www.youtube.com/watch?v=I6jB0nM9SKU)  
* **📄 Paper:** [Spanner: Google’s Globally-Distributed Database](https://research.google.com/archive/spanner-osdi2012.pdf)

## Phase 3: The Messaging & Streaming Layer (The "Pipe" Block)

**Objective:** How data flows between services asynchronously to ensure reliability and decoupling.

1\. Theory & Intuition

* **The Log as a Primitive:** Why the **Append-only Log** is the most important data structure in distributed systems.  
* **Pub/Sub vs. Queues:** The trade-off between **competing consumers** (RabbitMQ) and **ordered streaming** (Kafka).  
* **Exactly-Once Processing:** The math of **Idempotency** and **Deduplication Windows**.

2\. Discovery (Resources)

* **📝 Blog:** [The Log: What every software engineer should know (Jay Kreps)](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying)  
* **📝 Article:** [Designing Robust APIs with Idempotency (Stripe)](https://stripe.com/blog/idempotency)  
* **🎥 Video:** [How Discord Stores Billions of Messages](https://www.google.com/search?q=https://www.youtube.com/watch%3Fv%3Dx7W_M9vS3vA)

## Phase 4: High-Performance Search & Spatial Blocks

**Objective:** Finding specific data in N-dimensional space (Search, Geography).

1\. Theory & Intuition

* **Inverted Indexes:** The core of web search and monitoring—mapping terms to document IDs.  
* **Geometric Primitives:** How **Geohashing** and **Quad-Trees** turn 2D coordinates into a 1D string for efficient range queries.  
* **Bloom Filters:** The probability math of checking set membership without storing the data.

2\. Discovery (Resources)

* **📝 Blog:** [How Uber’s Highest QPS Service (H3) Works](https://www.uber.com/blog/h3/)  
* **📝 Interactive:** [The Secret Lives of Data (Raft/Visuals)](https://www.google.com/search?q=https://www.secretlivesofdata.com/raft/)  
* **📄 Paper:** [Bloom Filters (A Case Study)](https://www.google.com/search?q=https://dl.acm.org/doi/10.1145/365230.365253)

## Phase 5: Computation & Aggregation Layer

**Objective:** Processing massive datasets through Batch or Stream.

1\. Theory & Intuition

* **MapReduce & Spark:** Understanding **Data Locality** and the shuffle phase.  
* **Approximate Counting:** How systems like YouTube or Twitter count billions of events using **Count-Min Sketches** and **HyperLogLog**.

2\. Discovery (Resources)

* **📄 Paper:** [MapReduce: Simplified Data Processing on Large Clusters (Google)](https://research.google.com/archive/mapreduce-osdi04.pdf)  
* **📝 Blog:** [Netflix: Distributed Counter Abstraction](https://www.google.com/search?q=https://netflixtechblog.com/introducing-the-distributed-counter-abstraction-9db07865c1f0)

## Phase 6: Capstone Project: The Distributed Observability Engine

Instead of building 10 small things, build one system that uses all these primitives.

* **Task:** Build a distributed monitoring system (like a mini-Datadog/Prometheus).  
* **Primitive Integration:**  
  * **Inbound:** Use a **Distributed Queue** (Kafka) to ingest log lines.  
  * **Storage:** Store metrics in a **TSDB** (LSM Tree) and metadata in a **Distributed Hash Table**.  
  * **Search:** Use an **Inverted Index** to search logs by "Service Name" or "Error Code."  
  * **Scale:** Implement **Consistent Hashing** to distribute the metric shards across 3 nodes.

# Distributed Systems

## General Reading

### Distributed Systems: Queues, Logs, & Counting

1. [**LinkedIn: The Log (Jay Kreps)**](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying)  
   * *Why it fits:* The foundational text on why the log is the heart of distributed data flow, influencing Kafka and modern stream processing.  
2. [**Netflix: Distributed Counter Abstraction**](https://netflixtechblog.com/netflixs-distributed-counter-abstraction-8d0c45eb66b2)  
   * *Why it fits:* Details the struggle of counting events (likes/views) at global scale, comparing "Eventually Consistent" vs. "Best Effort" architectural patterns.  
3. [**Twitter: Announcing Snowflake**](https://blog.twitter.com/engineering/en_us/a/2010/announcing-snowflake)  
   * *Why it fits:* The classic design of a distributed ID generation service that works without coordination, solving the "ordering" problem in sharded systems.  
4. [**Segment: Delivering Billions of Messages Exactly Once**](https://www.google.com/search?q=https://segment.com/blog/exactly-once-delivery/)  
   * *Why it fits:* A war story on solving the "double send" problem during network partitions using deduplication windows and RocksDB.  
5. [**AWS Builders Library: Avoiding Overload**](https://aws.amazon.com/builders-library/avoiding-overload-in-distributed-systems-by-putting-the-smaller-service-in-control/)  
   * *Why it fits:* A masterclass on "load shedding" and why you should design systems where the control plane (smaller service) pulls work rather than having it pushed.  
6. [**Stripe: Designing Robust APIs with Idempotency**](https://stripe.com/blog/idempotency)  
   * *Why it fits:* Explains the "idempotency key" pattern in distributed payments to prevent double-charging during timeouts.  
7. [**Discord: How Discord Stores Billions of Messages**](https://discord.com/blog/how-discord-stores-billions-of-messages)  
   * *Why it fits:* A narrative of their migration from MongoDB to Cassandra (and later ScyllaDB), detailing partition strategies and compaction issues.  
8. [**Facebook: Memcache at Facebook (NSDI Paper)**](https://www.google.com/search?q=https://research.facebook.com/publications/memcached-at-facebook-scaling-distributed-key-value-store/)  
   * *Why it fits:* The gold standard on scaling a look-aside cache to billions of requests per second, dealing with "thundering herds" and "stale sets."  
9. [**Uber: Building a Scalable and Reliable Job Queue (Cherami)**](https://www.google.com/search?q=https://www.uber.com/blog/cherami-message-queue-architecture/)  
   * *Why it fits:* Discusses why they built their own durable task queue over Kafka to handle competing consumer patterns and delayed delivery.  
10. [**Slack: Scaling the Job Queue**](https://slack.engineering/scaling-slacks-job-queue/)  
    * *Why it fits:* Discusses how they manage massive spikes in background jobs using Redis and elaborate rate-limiting strategies.

### Distributed Databases

1. [**Amazon: Aurora \- Design Considerations for High Throughput Cloud-Native Relational Databases**](https://www.google.com/search?q=https://www.allthingsdistributed.com/2019/02/amazon-aurora-design-considerations.html)  
   * *Why it fits:* Explains the "Log is the Database" concept, separating compute from storage to achieve massive replication speed.  
2. [**FoundationDB: Testing Distributed Systems with Deterministic Simulation**](https://www.youtube.com/watch?v=4fFDFbi3toc)  
   * *Why it fits:* Explains how they simulate years of failure modes (disk corruption, network partitions) in minutes to ensure database correctness.  
3. [**ScyllaDB: Shard per Core Architecture**](https://www.scylladb.com/product/technology/shard-per-core-architecture/)  
   * *Why it fits:* A deep dive into "shared-nothing" architecture where every CPU core acts as its own mini-node to minimize locking and context switching.  
4. [**TigerBeetle: The Design of a Financial Accounting Database**](https://www.google.com/search?q=https://tigerbeetle.com/blog/designing-for-safety/)  
   * *Why it fits:* Focuses on "Strict Serializability" and how they handle subtle hardware failures (like bit rot) that other DBs ignore.  
5. [**Facebook: TAO \- The Power of the Graph**](https://engineering.fb.com/2013/06/25/core-infra/tao-the-power-of-the-graph/)  
   * *Why it fits:* Details the read-optimized graph store that backs the social graph, focusing on eventual consistency and caching edges.  
6. [**CockroachDB: Living Without Atomic Clocks**](https://www.cockroachlabs.com/blog/living-without-atomic-clocks/)  
   * *Why it fits:* How they implement Google Spanner’s concepts on commodity hardware using "uncertainty windows" for time synchronization.  
7. [**PingCAP: Online DDL in TiDB**](https://www.google.com/search?q=https://www.pingcap.com/blog/online-ddl-in-tidb/)  
   * *Why it fits:* Addresses the hard problem of changing a database schema (adding columns/indexes) across a distributed cluster without locking the table.  
8. [**Altinity: ClickHouse MergeTree Engine Internals**](https://www.google.com/search?q=https://altinity.com/blog/2019-7-10-clickhouse-mergetree-a-guide-to-storage-engines)  
   * *Why it fits:* Explains the Log-Structured Merge (LSM) tree variants used in columnar stores for high-speed ingestion and compression.  
9. [**DynamoDB: Under the Hood (Video)**](https://www.youtube.com/watch?v=yvBR71D0nAQ)  
   * *Why it fits:* An internal look at how Amazon manages partitions, leader election, and heat management in a multi-tenant DB.  
10. [**Google: Spanner, TrueTime and the CAP Theorem**](https://research.google/pubs/spanner-truetime-and-the-cap-theorem/)  
    * *Why it fits:* The seminal paper on how using atomic clocks (TrueTime) allows a system to act as if it breaks the CAP theorem by minimizing the "uncertainty" of time.

### RAFT and PAXOS (Applied)

1. [**Google: Paxos Made Live**](https://www.google.com/search?q=https://research.google/pubs/paxos-made-live-an-engineering-perspective/)  
   * *Why it fits:* The most famous "theory vs. practice" paper, detailing the struggle of implementing Paxos for the Chubby lock service in C++.  
2. [**Cloudflare: Raft does not Guarantee Liveness**](https://blog.cloudflare.com/a-byzantine-failure-in-the-real-world/)  
   * *Why it fits:* A war story about a "Byzantine" failure where a node was flaky enough to disrupt consensus but healthy enough to stay in the cluster.  
3. [**HashiCorp (Consul): Consistency Protocols**](https://www.consul.io/docs/architecture/consensus)  
   * *Why it fits:* Defines the practical implementation of Raft for service discovery, specifically how they handle "stale reads" vs. "consistent reads."  
4. [**Etcd: Raft Implementation Internals**](https://www.google.com/search?q=https://etcd.io/docs/v3.5/learning/design-raft/)  
   * *Why it fits:* Explains the specific optimizations Etcd added to Raft, such as request batching and pipelining, to improve throughput.  
5. [**TiKV: Optimizing Raft for Geo-Replication**](https://www.google.com/search?q=https://tikv.org/blog/raft-optimization/)  
   * *Why it fits:* Discusses "Pre-Vote" and "Joint Consensus" (changing cluster membership dynamically) to prevent instability during leader election.  
6. [**Redpanda: Raft at the Speed of Hardware**](https://www.google.com/search?q=https://redpanda.com/blog/raft-architecture)  
   * *Why it fits:* How they implemented Raft in C++ with a thread-per-core model to bypass the JVM garbage collection pauses that plague Kafka.  
7. [**Splunk: Paxos to Raft Migration**](https://www.google.com/search?q=https://www.splunk.com/en_us/blog/devops/raft-consensus-algorithm-distributed-systems.html)  
   * *Why it fits:* A retrospective on migrating a critical metadata service from a custom Paxos implementation to Raft for better maintainability.  
8. [**Elastic: Resiliency in Elasticsearch (Zen Discovery vs Raft)**](https://www.elastic.co/blog/a-new-era-for-cluster-coordination-in-elasticsearch)  
   * *Why it fits:* Explains why Elasticsearch had to abandon their custom discovery protocol for a Raft-like consensus model to prevent "split-brain" scenarios.  
9. [**NATS: JetStream Clustering**](https://www.google.com/search?q=https://docs.nats.io/nats-concepts/jetstream/clustering)  
   * *Why it fits:* How they use Raft not just for one stream, but for "Meta-groups" to manage the placement of data across a fleet.  
10. [**Heidi Howard: Distributed Consensus & Paxos**](https://www.youtube.com/watch?v=s8JqcZtvnsM)  
    * *Why it fits:* A lecture from a top researcher that bridges the gap, explaining how "Flexible Paxos" allows for different quorum sizes in read/write paths.

## Zero to Hero

### Phase 1: The Storage Engine (LSM Trees & Bitcask)

**The Goal:** Understand how databases persist data to disk. We debunk the magic of "saving" data.

* **Math & Theory:**  
  * **The Memory Hierarchy:** Latency numbers every programmer should know (L1 cache vs. RAM vs. SSD vs. Network).  
  * **Log-Structured Merge (LSM) Trees:** The math of Write Amplification vs. Read Amplification.  
  * **Bloom Filters:** The probability math of false positives ($P \\approx (1 \- e^{-kn/m})^k$).  
* **The Discovery (Reading/Watching):**  
  * 📖 **The Holy Grail:** *Designing Data-Intensive Applications* by Martin Kleppmann (Chapter 3: Storage and Retrieval). *This is mandatory.*  
  * 📄 **Paper:** [Bitcask: A Log-Structured Hash Table for Fast Key/Value Data](https://riak.com/assets/bitcask-intro.pdf) (Riak). The simplest intro to append-only logs.  
  * 📄 **Paper:** [The Log-Structured Merge-Tree (LSM-Tree)](https://www.cs.umb.edu/~poneil/lsmtree.pdf) (O'Neil et al.). The original 1996 paper.  
  * 🎥 **Video:** [LSM Trees vs B-Trees](https://www.youtube.com/watch?v=I6jB0nM9SKU) (Mark Callaghan, Facebook/Db2 expert).  
* **The Project (Python Notebook):**  
  * **"Py-LSM":** Start with a Python dict. Add a Write-Ahead Log (WAL) for durability. Implement a flush() function that dumps the dict to a sorted CSV (SSTable). Implement a get() that checks the MemTable, then searches the SSTable on disk.  
* **Delta to Reality:**  
  * Production systems (RocksDB) use skiplists for MemTables (lock-free concurrency) and use mmap/direct I/O to bypass the OS page cache.

### Phase 2: Relational Structures (B-Trees & SQL)

**The Goal:** Understand structure, indexing, and the "ACID" promise.

* **Math & Theory:**  
  * **B+ Trees:** Fan-out ratios and tree height ($O(\\log\_B N)$). Why broadly shallow trees are better for disk I/O.  
  * **ACID:** The mechanics of Atomicity (Undo Logs) and Isolation (Locks vs. MVCC).  
* **The Discovery:**  
  * 🎥 **Lecture:** [CMU 15-445/645: Database Systems](https://www.youtube.com/playlist?list=PLSE8ODhjZXjbohkNBWQs_otTrBTrjyohi) by Andy Pavlo. (Specifically lectures on *Tree Indexes* and *Concurrency Control*).  
  * 📄 **Paper:** [Architecture of a Database System](https://dsf.berkeley.edu/papers/fntdb07-architecture.pdf) (Stonebraker et al.). The high-level view of how Postgres/Oracle works.  
  * 📝 **Doc:** [SQLite File Format](https://www.sqlite.org/fileformat.html). A masterclass in how to structure binary data on disk.  
* **The Project (Python Notebook):**  
  * **"Py-SQL":** Implement a B-Tree in Python (node \= list of keys/pointers). Implement a simple parser that takes SELECT \* FROM users WHERE id \= 5 and traverses the tree.  
* **Delta to Reality:**  
  * Real databases implement **MVCC** (Multi-Version Concurrency Control) so readers don't block writers. Our toy version will likely use global locks (simpler but slower).

### Phase 3: Distributed Storage (GFS & Sharding)

**The Goal:** Break the single-machine limit. Distribute files across a network.

* **Math & Theory:**  
  * **Consistent Hashing:** The geometry of the ring. Minimizing key movement ($K/N$) when scaling.  
  * **Replication Strategy:** Chain replication vs. Quorum reads ($R+W \> N$).  
* **The Discovery:**  
  * 📄 **The Paper:** [The Google File System](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf) (SOSP 2003). The paper that started the Big Data era.  
  * 📝 **Blog:** [Consistent Hashing](https://www.google.com/search?q=https://www.toptal.com/big-data/consistent-hashing) (Tom White). Visual explanation of the ring.  
  * 🎥 **Video:** [MIT 6.824: Distributed Systems \- GFS](https://www.youtube.com/watch?v=cQP8WApzIQQ) (Robert Morris). The definitive breakdown.  
* **The Project (Python Notebook):**  
  * **"Py-DFS":** \* NameNode.py: Stores metadata (filename \-\> \[chunk\_ids\]).  
    * DataNode.py: Stores raw bytes.  
    * Simulate a client uploading a file: Split it into chunks, ask NameNode for locations, send bytes to DataNodes.  
* **Delta to Reality:**  
  * GFS handles "bit rot" (disk corruption) using checksums. Our Python version assumes the disk is perfect.

### Phase 4: Time & Logical Ordering

**The Goal:** Realize that "Time" is an illusion in distributed systems.

* **Math & Theory:**  
  * **Clock Skew:** Why NTP can't be trusted.  
  * **Happens-Before Relationship:** $A \\to B$.  
  * **Vector Clocks:** Detecting concurrent updates (Version vectors).  
* **The Discovery:**  
  * 📄 **The Paper:** [Time, Clocks, and the Ordering of Events in a Distributed System](https://lamport.azurewebsites.net/pubs/time-clocks.pdf) (Leslie Lamport). The most cited paper in the field.  
  * 📄 **Paper:** [Dynamo: Amazon’s Highly Available Key-value Store](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf). How Amazon uses Vector Clocks for the shopping cart.  
* **The Project (Python Notebook):**  
  * **"Lamport-Chat":** Simulate 3 friends chatting with random network delays. Use integer timestamps (Lamport Clocks) to sort the messages in the correct causal order, even if they arrive out of order physically.  
* **Delta to Reality:**  
  * Production systems like **Spanner** use "TrueTime" (Atomic clocks \+ GPS) to force physical time to align with logical time. We don't have atomic clocks.

### Phase 5: Consensus (Raft & Paxos)

**The Goal:** Getting a cluster of unreliable nodes to agree on a single value.

* **Math & Theory:**  
  * **Quorums:** Why you need $2f+1$ nodes to tolerate $f$ failures.  
  * **The State Machine:** Leader, Follower, Candidate states.  
* **The Discovery:**  
  * 📄 **The Paper:** [In Search of an Understandable Consensus Algorithm (Raft)](https://raft.github.io/raft.pdf).  
  * 🎨 **Interactive:** [The Secret Lives of Data](http://thesecretlivesofdata.com/raft/). A beautiful visualization of Raft. **(Show this first\!)**  
  * 📄 **Paper:** [Paxos Made Simple](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf) (Lamport). Read this only if you want to suffer (but it's foundational).  
* **The Project (Python Notebook):**  
  * **"Py-Raft":** Use asyncio to simulate 5 nodes. Implement the "Leader Election" logic.  
  * *Experiment:* Kill the leader node in the notebook and print the logs to see a new leader get elected.  
* **Delta to Reality:**  
  * Real Raft (Etcd) implements **Log Compaction** (snapshotting) so the log doesn't grow forever. Our toy version will just keep appending until we run out of RAM.

### Phase 6: The Log & Streaming (Kafka)

**The Goal:** Decoupling systems using immutable event streams.

* **Math & Theory:**  
  * **Sequential I/O:** Why disk writes can be faster than random RAM access.  
  * **Backpressure:** Little's Law applied to queues ($L \= \\lambda W$).  
* **The Discovery:**  
  * 📝 **Blog:** [The Log: What every software engineer should know about real-time data's unifying abstraction](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying) (Jay Kreps, creator of Kafka). **This is a masterpiece.**  
  * 📄 **Paper:** [Kafka: a Distributed Messaging System for Log Processing](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/09/Kafka.pdf).  
* **The Project (Python Notebook):**  
  * **"Py-Broker":** A server that accepts strings and appends them to a file. A "Consumer" that reads from byte offset $X$. Support "Consumer Groups" by storing offsets in a JSON file.  
* **Delta to Reality:**  
  * Kafka uses the **Page Cache** aggressively and sendfile (Zero-Copy) to push data to the network card without copying it to user space. Python does not support zero-copy easily.

### Phase 7: Resilience & Blast Radius

**Objective:** Move beyond "correctness" (Raft/Paxos) into "availability" and failure isolation at scale.

* **1\. Theory & Math**  
  * **The Control Plane vs. Data Plane:** Separating the complex decision-making logic from the high-throughput path of moving bytes.  
  * **Cell-based Architectures:** Dividing a global service into independent, isolated "cells" to strictly limit the blast radius of a failure.  
  * **The Math of Retries:** Understanding Jitter, Exponential Backoff, and the "Retry Storm" phenomenon.  
* **2\. Discovery (The Library)**  
  * **Paper:** *AWS Builders' Library: Workload Isolation using Shuffle Sharding*.  
  * **Case Study:** *The Meta 'Internal' Outage*. Analyzing how dependencies between the control plane and data plane can lead to global failures.  
  * **Resource:** *The Site Reliability Workbook* (Google). Chapter on managing cascading failures.  
* **3\. The Project: "The Shuffle-Sharded Load Balancer"**  
  * **Task:** Implement a virtual load balancer that assigns users to "cells" using shuffle sharding.  
  * **Simulation:** Inject a "poison pill" request for one user and prove that it only impacts their specific cell, leaving the rest of the system healthy.

### Phase 8: Capstone (Real World Architectures)

**The Goal:** Designing full systems using the blocks from Phases 1-6.

* **Projects to Build:**  
  * **Snowflake ID Generator:** (Based on Twitter Snowflake).  
    * *Resource:* [Twitter Snowflake Source Code](https://www.google.com/search?q=https://github.com/twitter-archive/snowflake/tree/snowflake-2010).  
  * **Distributed Counter:** (CRDTs).  
    * *Resource:* [A comprehensive study of Convergent and Commutative Replicated Data Types](https://hal.inria.fr/inria-00555588/document).  
  * **Mini-Uber:** (Geospatial Indexing).  
    * *Resource:* [Uber Engineering: How We Built Uber Engineering’s Highest Query Per Second Service Using Go](https://www.google.com/search?q=https://eng.uber.com/go-geofence/).12  
* **General System Design Resources:34**  
  * 📚 **Repo:** [The System Design Primer56](https://github.com/donnemartin/system-design-primer).  
  * 📝 **Blog:** [High Scalability](http://highscalability.com/). (Read the "Real Life Architectures" section).

# Pragmatic Systems Toolsmith

## Phase 1: The Shell & Data Wrangling

**Objective:** Treat the terminal as a high-performance database and automation engine.

* **The Unix Philosophy**: Master the composition of small, single-purpose tools via pipes to process data without loading it into memory1.  
* **Log Processing at Scale**: Use grep, sed, and awk to filter and transform multi-gigabyte logs on the fly.  
* **Structured Data (JSON)**: Master jq for slicing and dicing JSON logs from cloud providers or distributed traces.  
* **Parallelism**: Use xargs \-P or parallel to run CLI tasks across all available CPU cores.  
* **Project**: "The Log Auditor." Write a one-line shell pipeline to find the top 10 IP addresses in a 10GB access log that returned 5xx errors during a specific time window.

## Phase 2: Version Control & Repository Mastery

**Objective:** Understand the history of code as a data structure (DAG) to navigate massive monorepos.

* **The Git DAG**: Visualizing commits, branches, and tags as a Directed Acyclic Graph (DAG) rather than a linear history.  
* **Strategic History**: Mastery of rebase \--interactive to keep histories clean and cherry-pick to move critical fixes between environments.  
* **Regression Hunting**: Using git bisect to perform a binary search through thousands of commits to find the exact change that introduced a bug.  
* **Disaster Recovery**: Using git reflog to recover "lost" commits or deleted branches after a botched rebase.  
* **Project**: "The Archaeology Lab." Given a repository with an intentional performance regression, use git bisect combined with an automated test script to identify the offending commit in under 60 seconds.

## Phase 3: The Runtime Environment (Containers)

**Objective:** De-mystify "The Cloud" by understanding the kernel-level primitives of isolation 2.

* **The Isolation Lies**: Learning how the Linux kernel uses **Namespaces** to isolate PIDs, Networks, and Mounts3.  
* **Resource Governance**: Using **Cgroups** to enforce strict limits on CPU, RAM, and I/O to prevent "noisy neighbor" problems4.  
* **Image Optimization**: Building multi-stage Dockerfiles to minimize attack surface and reduce "cold start" times for scaled services.  
* **The Control Loop**: Understanding the fundamental logic of orchestration—continually reconcile the "Desired State" vs. the "Actual State" 5.  
* **Project**: "Tiny-Docker." Use the unshare command to manually create a process that has its own network stack and filesystem without using the Docker binary 6.

## Phase 4: Networking & Security Pragmatism

**Objective:** Debugging the "wire" when the application code appears perfect.

* **Troubleshooting the Handshake**: Using curl \-v and tcpdump to identify where a request is failing: DNS, TCP connection, or TLS negotiation.  
* **DNS & Routing**: Mastery of dig to debug record propagation and nc (Netcat) to test port connectivity through firewalls.  
* **Identity & Encryption**: Understanding PKI by using openssl to inspect certificates, generate CSRs, and verify private/public key pairs.  
* **Simulating Failure**: Using tc (Traffic Control) to intentionally inject latency or packet loss into a local environment to test system resilience.  
* **Project**: "The Packet Detective." Capture a local HTTPS request using tcpdump and identify the exact duration of the DNS lookup, TCP handshake, and TLS session establishment.

## Phase 5: Observability & Performance

**Objective:** Moving from "guessing" to "measuring" through instrumentation and profiling7777.

* **The USE Method**: A systematic checklist for debugging: Check **U**tilization, **S**aturation, and **E**rrors for every resource8.  
* **Dynamic Profiling**: Using perf to sample the CPU and identify "hot" functions that are consuming cycles.  
* **Flame Graphs**: Visualizing stack traces to find deep recursion or expensive library calls at a glance.  
* **Latency Numbers**: Memorizing the "L1 cache vs. RAM vs. Disk" scale to recognize when an architectural choice is physically impossible9999.  
* **Project**: "The Hot-Path Hunt." Write a script with a hidden algorithmic bottleneck ($O(N^2)$) and use perf and a Flame Graph to prove exactly which function is the culprit.

## Phase 6: Operational Hygiene

**Objective:** The "soft" and "hard" skills of maintaining a system in production.

* **Database Pragmatism**: Using EXPLAIN ANALYZE to read query plans and understand why an index is (or isn't) being used10.  
* **Migration Safety**: Designing schema changes that are backward-compatible to allow for zero-downtime rolling deployments11.  
* **Incident Response**: Learning the "5 Whys" methodology to move past human error to the systemic root cause.  
* **Technical Storytelling**: Using Markdown and **Mermaid.js** to keep architecture diagrams version-controlled alongside the code12.  
* **Project**: "The Post-Mortem." Analyze a famous historical outage (e.g., a major Meta or AWS event) and write a formal incident report that identifies the "Golden Signal" that first alerted the team13.

# Deep Learning Track

## General Reading

### Distributed Deep Learning

1. [**Meta: Engineering Llama 3 Infrastructure**](https://engineering.fb.com/2024/03/12/data-center-engineering/building-metas-genai-infrastructure/)  
   * *Why it fits:* details the specific hardware (RoCE v2, InfiniBand) and checkpointing strategies needed for 24k GPU clusters.  
2. [**Microsoft: ZeRO & DeepSpeed**](https://www.microsoft.com/en-us/research/blog/zero-deepspeed-new-system-optimizations-enable-training-models-with-over-100-billion-parameters/)  
   * *Why it fits:* Explains the "Zero Redundancy Optimizer" (ZeRO) which partitions model states (optimizer, gradients, parameters) across GPUs to fit massive models in memory.  
3. [**PyTorch: Distributed Data Parallel Design**](https://pytorch.org/docs/stable/notes/ddp.html)  
   * *Why it fits:* An architectural note on "Gradient Bucketing" and ring-allreduce, explaining how they overlap computation with communication.  
4. [**Google: GSPMD \- General and Scalable Parallelization for ML**](https://arxiv.org/abs/2105.04663)  
   * *Why it fits:* The architecture behind how Google trains on TPUs, allowing users to write "single device" code that is automatically sharded.  
5. [**OpenAI: Scaling Kubernetes to 7,500 Nodes**](https://openai.com/index/scaling-kubernetes-to-7500-nodes/)  
   * *Why it fits:* A war story on the limits of Etcd and the Kubernetes scheduler when bombarded with massive batch training jobs.  
6. [**Hugging Face: The Technology Behind BLOOM**](https://huggingface.co/blog/bloom-megatron-deepspeed)  
   * *Why it fits:* A transparent log of the failures (hardware crashes, loss spikes) encountered while training a 176B parameter model on Jean Zay supercomputer.  
7. [**NVIDIA: Megatron-LM Architecture**](https://www.google.com/search?q=https://developer.nvidia.com/blog/megatron-lm-training-multi-billion-parameter-language-models-using-model-parallelism/)  
   * *Why it fits:* Explains "Tensor Parallelism" (splitting a single matrix multiplication across GPUs) vs. "Pipeline Parallelism."  
8. [**MosaicML: Fault Tolerance in Large Scale Training**](https://www.google.com/search?q=https://www.mosaicml.com/blog/fault-tolerance)  
   * *Why it fits:* Analysis of hardware failure rates (A100 vs H100) and how to architect software that resumes training automatically without human intervention.  
9. [**Uber: Horovod**](https://www.uber.com/blog/horovod/)  
   * *Why it fits:* How they adapted MPI (Message Passing Interface) from high-performance computing to make distributed TensorFlow training easier.  
10. [**ByteDance: MegaScale**](https://arxiv.org/abs/2402.15627)  
    * *Why it fits:* A detailed paper on training on 10,000+ GPUs, discussing the specific network diagnostic tools needed to find "slow nodes" that drag down the whole cluster.

### AI Infrastructure (Serving & Platforms)

1. [**Pinterest: Powering Machine Learning at Scale**](https://www.google.com/search?q=https://medium.com/pinterest-engineering/powering-machine-learning-at-pinterest-scale-2487431a4738)  
   * *Why it fits:* Covers the transition from ad-hoc scripts to a unified feature store and serving platform for billions of pins.  
2. [**Uber: Michelangelo \- Machine Learning Platform**](https://www.uber.com/blog/michelangelo-machine-learning-platform/)  
   * *Why it fits:* One of the first and most influential "ML Ops" platform architectures, introducing the concept of a Feature Store.  
3. [**Netflix: Mezzanine \- The Media Supply Chain**](https://www.google.com/search?q=https://netflixtechblog.com/mezzanine-the-exact-opposite-of-a-zero-copy-architecture-4e2078696778)  
   * *Why it fits:* While focused on media encoding, it details the orchestration of massive parallel compute jobs, which parallels AI inference pipelines.  
4. [**Ray: Architecture of a Distributed Runtime**](https://docs.ray.io/en/latest/ray-core/key-concepts.html)  
   * *Why it fits:* Explains the "Actor" model applied to AI, handling stateful workers (like simulators) differently from stateless tasks.  
5. [**Lyft: Flyte \- Cloud Native Machine Learning Orchestration**](https://eng.lyft.com/introducing-flyte-cloud-native-machine-learning-and-data-processing-platform-fb2bb3046a59)  
   * *Why it fits:* A look at the "workflow" engine, handling data lineage, caching of intermediate results, and spot instance management.  
6. [**LinkedIn: Pro-ML Architecture**](https://www.google.com/search?q=https://engineering.linkedin.com/blog/2019/01/scaling-machine-learning-productivity-at-linkedin)  
   * *Why it fits:* Discusses the integration of AI models directly into the CI/CD pipeline, treating models as software artifacts.  
7. [**DoorDash: Real-Time ML Predictions**](https://www.google.com/search?q=https://doordash.engineering/2020/05/29/building-a-gig-economy-machine-learning-platform/)  
   * *Why it fits:* Focuses on the latency constraints of the "Gig Economy"—predicting delivery times (ETAs) where freshness of data is critical.  
8. [**Instacart: Griffin**](https://www.google.com/search?q=https://tech.instacart.com/griffin-how-we-built-our-ml-platform-4787114b0a51)  
   * *Why it fits:* A practical look at unifying disparate ML tools (Python, SQL, R) into a single containerized platform.  
9. [**Airbnb: Bighead**](https://www.google.com/search?q=https://medium.com/airbnb-engineering/bighead-airbnbs-end-to-end-machine-learning-platform-98b7a098b950)  
   * *Why it fits:* Highlights the "Zipline" component for handling "point-in-time" correctness in data, preventing data leakage during training.  
10. [**Discord: Midjourney & AI Serving**](https://discord.com/blog/how-discord-supercharges-network-disks-for-extreme-low-latency)  
    * *Why it fits:* While more general infra, this post (and others in their series) touches on the read/write intensity of serving AI-generated content to millions of users.

## Structured Learning

### Model Evolution & Algorithms

#### 1\. The Transformer Foundation

* **The Big One:** [Attention Is All You Need (Vaswani et al.)](https://arxiv.org/abs/1706.03762) – Read the first 6 pages multiple times.  
* **Rotary Embeddings (RoPE):** [RoFormer Paper](https://arxiv.org/abs/2104.09864) & [EleutherAI Explainer Blog](https://blog.eleuther.ai/rotary-embeddings/). RoPE is the industry standard for relative position encoding.  
* **Activation Functions:** [GLU Variants Improve Transformer (Shazeer, 2020\)](https://arxiv.org/abs/2002.05202) – Explains why SwiGLU replaced ReLU.  
* **Practical Implementation:** [Andrej Karpathy's "Let's build GPT" (Video)](https://www.youtube.com/watch?v=kCc8FmEb1nY). A 2-hour masterclass in coding a Transformer from scratch in PyTorch.

#### 2\. Scaling & Efficiency

* **Scaling Laws:**  
  * [Kaplan's Original Scaling Laws (OpenAI)](https://arxiv.org/abs/2001.08361).  
  * [The Chinchilla Paper (DeepMind)](https://arxiv.org/abs/2203.15556) – Proves we were undertraining models.  
* **FlashAttention:** [FlashAttention 1 & 2 (Tri Dao)](https://arxiv.org/abs/2307.08691) – A must-read on how to write IO-aware kernels.  
* **Mixture of Experts (MoE):** [Mixture-of-Experts Blog (HuggingFace)](https://huggingface.co/blog/moe). A great high-level breakdown of the gating logic.

#### 3\. Alignment & Reasoning

* **PPO/RLHF:** [InstructGPT Paper (OpenAI)](https://arxiv.org/abs/2203.02155).  
* **DPO:** [Direct Preference Optimization (Stanford)](https://arxiv.org/abs/2305.18290) – The breakthrough that simplified alignment.  
* **GRPO (Modern Alignment):** [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437). Look at Section 5.2.2 for the Group Relative Policy Optimization details.  
* **Chain of Thought:** [Chain of Thought Prompting (Wei et al.)](https://arxiv.org/abs/2201.11903).

### Infrastructure & Systems Engineering

#### 1\. Hardware & Frameworks

* **NVIDIA Hopper:** [H100 Architecture Whitepaper](https://resources.nvidia.com/en-us-tensor-core/gtc22-whitepaper-hopper). Focus on the **Transformer Engine** and **NVLink** sections.  
* **Google TPU:** [TPU v4 Paper (Google)](https://arxiv.org/abs/2304.01433).  
* **JAX/XLA:** [JAX Documentation: The Sharp Bits](https://jax.readthedocs.io/en/latest/notebooks/Common_Gotchas_in_JAX.html). Essential for understanding functional programming in ML.  
* **Triton:** [Triton: An Intermediate Language for GPU Programming](http://www.eecs.harvard.edu/~htk/publication/2019-mapl-tillet-kung-cox.pdf).

#### 2\. Distributed Training & Parallelism

* **DeepSpeed/ZeRO:** [ZeRO: Memory Optimizations for Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054). Explains how to shard gradients and optimizer states.  
* **FSDP:** [PyTorch Fully Sharded Data Parallel (FSDP) Blog](https://pytorch.org/blog/introducing-pytorch-fully-sharded-data-parallel-api/). Meta’s approach to scaling training.  
* **Megatron-LM:** [Efficient Large-Scale Language Model Training on GPU Clusters](https://arxiv.org/abs/2104.04473). Covers 3D Parallelism.

#### 3\. Inference at Scale

* **vLLM/PagedAttention:** [Efficient Memory Management for LLM Serving (Paper)](https://arxiv.org/abs/2309.06180). This is the current state-of-the-art for production inference.  
* **Continuous Batching:** [AnyScale Blog on Continuous Batching](https://www.anyscale.com/blog/continuous-batching-llm-inference). A visual and intuitive explanation of how to maximize GPU throughput.

## Zero to Hero

### Phase 0: Visual Systems & Technical Storytelling

* **0.1 Programmatic Animation (Manim)**  
  * **Theory:** Mathematical coordinate systems and programmatic "tweening."  
  * **Discovery:** [Manim Community Documentation](https://www.manim.community/) and the [3Blue1Brown Source Code](https://github.com/3b1b/manim).  
  * **Project:** Animate a dot product projection.  
* **0.2 Neural Architecture Visualization**  
  * **Discovery:** [ManimML Github](https://github.com/helblazer811/ManimML) – Specific for neural net animations.  
  * **Project:** A pulsing 3-layer MLP forward pass.  
* **0.3 Static Engineering Assets**  
  * **Discovery:** [Penrose](https://penrose.github.io/) (Math-to-Diagram) and [Excalidraw](https://excalidraw.com/) (Engineering sketches).  
  * **Project:** Map a Distributed System architecture.

### Phase 1: The Foundation (1950s – 2010\)

* **1.1 The Rosenblatt Perceptron**  
  * **Math:** [The original 1958 Perceptron Paper](https://www.google.com/search?q=https://ia801903.us.archive.org/19/items/cornelluniversity_6127_001/6127_001.pdf).  
  * **Discovery:** [Minsky & Papert’s "Perceptrons"](https://en.wikipedia.org/wiki/Perceptrons_\(book\)) – Understand the XOR limitation.  
  * **Project:** Build a Perceptron in pure Python to solve AND/OR gates.  
* **1.2 The MLP & Backprop**  
  * **Math:** [Calculus on Computational Graphs (Colah's Blog)](https://colah.github.io/posts/2015-08-Backprop/).  
  * **Discovery:** [Micrograd by Karpathy](https://github.com/karpathy/micrograd) – Study the `Value` class.  
  * **Project:** Build a scalar autograd engine; solve the XOR problem.  
* **1.3 Tensors & Vectorization**  
  * **Math:** [Matrix Differentiation (Implicit Layers)](https://www.google.com/search?q=http://implicit-layers-tutorial.org/matrix_calculus/).  
  * **Project:** Re-implement the MLP using NumPy matrices; benchmark speedup.  
* **1.4 Modern Micro-Optimizations (The Nanochat Recipe)**  
  * **Theory & Intuition:** \* Value Embeddings (VEs): Adding trainable embeddings to V tokens every alternate layer (massive parameter increase with near-zero FLOPs)**.**  
    * **Activation & Normalization Tweaks**: Replacing SwiGLU with ReLU², and using RMSNorm *without* the learnable affine transform (scale/shift) to save parameters.  
    * **Logit Soft-Capping**: Bounding logits using `soft_cap * tanh(logits/soft_cap)` to stabilize training (popularized by Gemma 2).  
    * **QK Normalization**: Normalizing query and key matrices after RoPE to stabilize attention.  
    * **Sliding Window Attention**: Interleaving local attention (e.g., 1024 tokens) with global attention to save memory.  
    * **Untied Embeddings**: Decoupling the input embedding matrix from the final un-embedding matrix (unusual for tiny LMs, standard for LLMs).  
    * **Optimizers**: The shift toward the Muon optimizer over standard AdamW.  
  * **Discovery (Resources)**:  
    * Link to Karpathy's GitHub repo: \#481 Beating GPT-2 for \<\<$100: the nanochat journey  
  * **The Project**  
    * Take the Transformer built in Phase 4.1 and modify the `forward()` pass to implement RMSNorm without affine transformations and Logit Soft-capping.

### Phase 2: The Vision Era (CNNs)

* **2.1 LeNet-5 & Spatial Hierarchies**  
  * **Math:** [Gradient-Based Learning Applied to Document Recognition](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf).  
  * **Discovery:** [Understanding im2col](https://www.google.com/search?q=https://cs231n.github.io/convolutional-networks/%23conv) – Turning convolutions into Matrix Multiplications.  
  * **Project:** Implement `Conv2D` and `MaxPool2D` from scratch using `im2col`.  
* **2.2 AlexNet & The GPU Shift**  
  * **Math:** [ImageNet Classification with Deep CNNs](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf).  
  * **Discovery:** The "Dead ReLU" problem and local response normalization.  
  * **Project:** Train an AlexNet clone on CIFAR-100.  
* **2.3 ResNet & Residual Learning**  
  * **Math:** [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385).  
  * **Discovery:** [Identity Mappings in Deep Residual Networks](https://arxiv.org/abs/1603.05027).  
  * **Project:** Build ResNet-18 with skip-connections.

### Phase 3: The Sequence Era (RNNs to Seq2Seq)

* **3.1 Simple RNNs**  
  * **Math:** [The Unreasonable Effectiveness of RNNs](https://karpathy.github.io/2015/05/21/rnn-effectiveness/).  
  * **Project:** A character-level RNN; track gradient norms.  
* **3.2 LSTMs & GRUs**  
  * **Math:** [Long Short-Term Memory (Hochreiter & Schmidhuber)](https://www.bioinf.jku.at/publications/older/2604.pdf).  
  * **Discovery:** [Understanding LSTMs (Chris Olah)](https://colah.github.io/posts/2015-08-Understanding-LSTMs/).  
  * **Project:** Build an LSTM cell from scratch; generate fake C code.  
* **3.3 Seq2Seq & The Bottleneck**  
  * **Math:** [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215).  
  * **Project:** Build a machine translation system.

### Phase 4: Scaling, Alignment & Efficiency

* **4.1 Transformers & Self-Attention**  
  * **Math:** [Attention Is All You Need](https://arxiv.org/abs/1706.03762).  
  * **Discovery:** [The Annotated Transformer](https://nlp.seas.harvard.edu/2018/04/03/attention.html).  
  * **Project:** Implement a full Transformer from scratch in PyTorch.  
* **4.2 Scaling Laws & Chinchilla**  
  * **Math:** [Training Compute-Optimal LLMs (Chinchilla Paper)](https://arxiv.org/abs/2203.15556).  
  * **Discovery:** [Scaling Laws for Neural Language Models (Kaplan)](https://arxiv.org/abs/2001.08361).  
* **4.3 Mixture of Experts (MoE)**  
  * **Math:** [Hugging Face MoE Blog](https://huggingface.co/blog/moe) – Deep dive into gating.  
  * **Project:** Implement Top-K Gating MoE.  
* **4.4 Alignment: DPO & PPO**  
  * **Math:** [Direct Preference Optimization (DPO)](https://arxiv.org/abs/2305.18290).  
  * **Project:** Use DPO to align a small transformer to a style dataset.

### Phase 5: Infrastructure & Systems (The "Meta" Level)

* **5.1 GPU Kernels with Triton**  
  * **Discovery:** [Triton Tutorials (OpenAI)](https://triton-lang.org/main/getting-started/tutorials/index.html).  
  * **Project:** Write a custom Triton kernel for Softmax.  
* **5.2 Distributed Engineering**  
  * **Discovery:** [NVIDIA Collective Communications Library (NCCL)](https://developer.nvidia.com/nccl).  
  * **Project:** Manually implement **Ring All-Reduce** gradient sync on 2 nodes.  
* **5.3 The 1B Model Grand Finale**  
  * **Discovery:** [DeepSpeed ZeRO Whitepaper](https://arxiv.org/abs/1910.02054).  
  * **Project:** Train a 124M parameter model on [FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu).

### Phase 6: Data Engineering for AI (Deep Learning)

**Objective:** Solve the "Systems problem" that enables the "AI problem"11.

* **1\. Theory & Math**  
  * **The Data Lakehouse:** Understanding the evolution from S3/Data Lakes to structured, versioned storage like **Delta Lake** or **Iceberg**.  
  * **Tokenization at Scale:** The math of Byte-Pair Encoding (BPE) and how to process 10 Trillion tokens efficiently12.  
  * **Data Deduplication:** Using MinHash and LSH (Locality Sensitive Hashing) to remove billions of duplicate documents from training sets13131313.  
* **2\. Discovery (The Library)**  
  * **Paper:** *FineWeb: Decanting the Web for the Best AI Data*. A masterclass in large-scale data curation14.  
  * **Tool:** Dask or Ray Data. Frameworks for distributed data preprocessing that don't fit in a single node's RAM15.  
  * **Framework:** Unstructured.io. Learning how to parse complex PDFs/HTML into clean text for LLM training.  
* **3\. The Project: "The CommonCrawl Cleaner"**  
  * **Task:** Use a sample of CommonCrawl data (WET files).  
  * **Pipeline:** Implement a distributed cleaning pipeline: Language detection $\\to$ Gopher-style heuristic filtering $\\to$ MinHash deduplication.  
  * **Metric:** Measure the "Compression Ratio" (how much noise was removed) and the "Token Throughput"16.


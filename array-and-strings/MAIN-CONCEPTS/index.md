Two Pointers & Sliding Window:
Two Pointers and Sliding Window are two related techniques used to optimize algorithms that involve arrays or strings.


## 1. Two Pointers:
The two-pointer technique involves using two pointers to iterate through a collection (like an array or string) simultaneously, often from different directions or with different step sizes. This technique can significantly reduce time complexity in some problems.

How it Works:
You maintain two pointers (indices/indexes) on the array or string.

You move the pointers in a controlled manner to solve the problem more efficiently than iterating through the entire array.

Example Problems:
Pair Sum: Given a sorted array, find two elements whose sum equals a target. One pointer starts from the beginning (left), and the other starts from the end (right). You adjust the pointers based on the sum.

Palindrome Check: Check if a string is a palindrome by comparing characters from both ends using two pointers.

Advantages:
O(n) time complexity for many problems that would otherwise require O(n²) or higher (like nested loops).

Optimizes problems where you can reduce the problem space or avoid unnecessary iterations by adjusting the pointers.

## 2. Sliding Window:
The sliding window technique is a specialized form of the two-pointer technique, where the window is a range of elements, and the window size can be adjusted dynamically. This technique is commonly used when you need to find an optimal subarray or substring within a larger array/string that satisfies a specific condition.

How it Works:
You maintain a "window" (a contiguous block) within the array or string, where the window size may vary.

One pointer usually represents the start of the window, and the other pointer represents the end.

You "slide" the window across the array to examine all possible windows of different sizes, adjusting the pointers as necessary.

Example Problems:
Longest Substring Without Repeating Characters: Given a string, find the longest substring that doesn’t contain repeating characters. You use two pointers to dynamically expand and shrink the window.

Maximum Sum Subarray of Size K: Find the maximum sum of a subarray of size k. You can use the sliding window technique to calculate the sum in linear time (O(n)).

Subarrays with Sum Less Than K: Count the number of subarrays where the sum is less than k.

Advantages:
O(n) time complexity for problems where brute force might result in a O(n²) solution.

Great for problems involving contiguous subarrays or substrings and where the range of the window is adjustable.

## Order of learning
https://neetcode.io/roadmap

3Sum - Leetcode 15 - Python
https://youtu.be/jzZsG8n2R9A

Two Sum => Two Sum II - Input Array Is Sorted => 3Sum
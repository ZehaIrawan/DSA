Feature	Brute Force	Two Pointers
Time Complexity	O(n^2)	O(n)
Space Complexity	O(1)	O(1)
Speed on large inputs	🐌 Very slow	⚡ Very fast
Readability	✅ Simple	✅ Simple
Sorted list requirement	❌ Not needed	✅ Needed

✅ Two-pointer only works if the array is sorted.

If it’s not sorted, and sorting is allowed, you can sort first:

numbers.sort()  # O(n log n)
has_pair_with_sum(numbers, target)
Still better than O(n^2) overall.


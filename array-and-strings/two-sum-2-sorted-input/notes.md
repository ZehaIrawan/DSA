🔍 Comparison of Both Approaches
Approach	    Time 	Space 	Notes
Hashmap 	    O(n)	O(n)	  Uses extra space for hashmap
Two-Pointer 	O(n)	O(1)	  More efficient, uses constant space

✅ Why is the Two-Pointer Approach Better?
Lower space complexity: Since the input array is sorted, we don’t need a hashmap. We can find the solution using two pointers in O(1) space.

Same time complexity: Both approaches have O(n) time complexity, but the two-pointer approach is more cache-friendly and efficient in practice.

More elegant and simple: Less code, no need to manage a hashmap.

🚀 Final Verdict: Use the Two-Pointer Approach
If the input array is sorted, always prefer the two-pointer method. If the array is unsorted, then a hashmap or sorting + two-pointer could be options.

# Sorting add time complexity of O(n log n)
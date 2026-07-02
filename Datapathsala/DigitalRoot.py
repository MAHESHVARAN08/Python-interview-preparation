# QUESTION
"""
Digital Root

Given a non-negative integer n, repeatedly sum its digits until a single digit remains. Return that single digit.

Example 1

Input: n = 942
Output: 6
Explanation: 9 + 4 + 2 = 15, then 1 + 5 = 6

Example 2

Input: n = 38
Output: 2
Explanation: 3 + 8 = 11, then 1 + 1 = 2

Example 3

Input: n = 0
Output: 0

Constraints

0 <= n <= 10^9
"""
# SOLUTION
# METHOD 1 (ITERATIVE)

def digitalRoot(self, n: int) -> int:
        while n>=10:
            sum = 0
            while n>0:
                rem=n%10
                sum+=rem 
                qt=n//10
            n=sum
        return n

# METHOD 2

def digitalRoot(self, n: int) -> int:
        if n==0:
            return 0
        return 1 + (n-1)%9

# EXPLANATION

"""
METHOD 1 (ITERATIVE APPROACH):
================================

Time Complexity: O(log n) per iteration (digits extraction), with multiple iterations
Space Complexity: O(1) - only constant space used

Logic:
------
1. Outer Loop: while n >= 10
   - Continues until n becomes a single digit (0-9)
   - This means we keep repeating the process until only one digit remains

2. Inner Loop: while n > 0
   - Extracts each digit from the number using modulo operator
   - rem = n % 10: Gets the last digit
   - sum += rem: Adds that digit to the sum
   - qt = n // 10: Integer division to remove the last digit (note: qt is not used, it's redundant)
   - After inner loop completes, sum contains the sum of all digits

3. n = sum: Updates n with the sum of its digits
4. Return n: When n < 10, we have our digital root

Example Trace (n = 942):
- Iteration 1: sum = 9 + 4 + 2 = 15, n = 15
- Iteration 2: sum = 1 + 5 = 6, n = 6
- n < 10, so return 6

Drawback: The variable 'qt' is computed but never used. The inner loop should update n with n // 10.


METHOD 2 (MATHEMATICAL APPROACH - DIGITAL ROOT FORMULA):
=========================================================

Time Complexity: O(1) - constant time, just one calculation
Space Complexity: O(1) - only constant space used

Logic:
------
This method uses a mathematical property of digital roots known as the "Digital Root Formula":
Digital Root = 1 + (n - 1) % 9

Special Case: If n == 0, return 0 directly

Why does this work?
- The digital root is related to modulo 9 arithmetic
- For any positive integer n, repeatedly summing digits gives the same result as n % 9, with one exception
- When n % 9 == 0 (and n != 0), the digital root is 9, not 0
- Using (n - 1) % 9 + 1 elegantly handles this:
  * If n % 9 == 0: (n - 1) % 9 = 8, so result = 8 + 1 = 9 ✓
  * If n % 9 == k: (n - 1) % 9 = k - 1, so result = (k - 1) + 1 = k ✓

Examples:
- n = 942: (942 - 1) % 9 = 941 % 9 = 8, result = 1 + 8 = 9... Wait, let me recalculate
- n = 942: 942 = 104 * 9 + 6, so 942 % 9 = 6, digital root = 6 ✓
- n = 38: 38 = 4 * 9 + 2, so 38 % 9 = 2, digital root = 2 ✓
- n = 9: 9 = 1 * 9 + 0, so 9 % 9 = 0, but digital root = 9
  Using formula: (9 - 1) % 9 + 1 = 8 % 9 + 1 = 8 + 1 = 9 ✓

Advantage: O(1) time complexity - much faster than METHOD 1
This is the most efficient solution for this problem.


COMPARISON:
===========
Method 1: Good for understanding the concept, but slower O(log n) per iteration
Method 2: Optimal solution using mathematical insight, O(1) constant time
"""

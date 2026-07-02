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


#QUESTION
"""
Remove Duplicate Characters

Given a string s, return a new string with all duplicate characters removed, keeping only the first occurrence of each character. The original order of characters must be preserved.

Example 1

Input:

s = "programming"

Output:

"progamin"

Explanation:
The first occurrences in order are: p, r, o, g, a, m, i, n.

Example 2

Input:

s = "abcabc"

Output:

"abc"

Explanation:
Each of a, b, and c appears twice; only the first occurrence of each is kept.

Example 3

Input:

s = "aaa"

Output:

"a"

Explanation:
All characters are the same, so only one is kept.
"""

#SOLUTION
def removeDuplicates(self, s: str) -> str:
        d =set()
        str = ""
        for i in s:
            if i not in d:
                str+=i
                d.add(i)
            else:
                continue
        return str

#EXPLANATION

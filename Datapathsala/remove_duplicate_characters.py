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
"""
LOGIC BREAKDOWN:

1. DATA STRUCTURES USED:
   - Set 'd': Stores characters we've already encountered
   - String 'str': Builds the result string with only first occurrences

2. ALGORITHM STEPS:
   a) Initialize an empty set 'd' to track seen characters
   b) Initialize an empty string 'str' to store the result
   
   c) Iterate through each character 'i' in the input string 's':
      - CHECK: Is the character already in the set 'd'?
        * If NO (first occurrence):
          → Add the character to the result string 'str'
          → Add the character to set 'd' to mark it as seen
        * If YES (duplicate):
          → Skip it (continue to next iteration)
   
   d) Return the result string with only first occurrences

3. HOW IT WORKS WITH EXAMPLE:
   Input: s = "programming"
   
   Step-by-step execution:
   - 'p': not in d → add to str, add to d. str="p", d={'p'}
   - 'r': not in d → add to str, add to d. str="pr", d={'p','r'}
   - 'o': not in d → add to str, add to d. str="pro", d={'p','r','o'}
   - 'g': not in d → add to str, add to d. str="prog", d={'p','r','o','g'}
   - 'r': in d → skip. str="prog", d={'p','r','o','g'}
   - 'a': not in d → add to str, add to d. str="progra", d={'p','r','o','g','a'}
   - 'm': not in d → add to str, add to d. str="program", d={'p','r','o','g','a','m'}
   - 'm': in d → skip. str="program", d={'p','r','o','g','a','m'}
   - 'i': not in d → add to str, add to d. str="programi", d={'p','r','o','g','a','m','i'}
   - 'n': not in d → add to str, add to d. str="programin", d={'p','r','o','g','a','m','i','n'}
   - 'g': in d → skip. str="programin", d={'p','r','o','g','a','m','i','n'}
   
   Output: "programin"

4. TIME & SPACE COMPLEXITY:
   - Time Complexity: O(n) where n is the length of the string
     (We iterate through the string once, and set operations are O(1))
   - Space Complexity: O(k) where k is the number of unique characters
     (Set 'd' stores at most k characters, output string also stores k characters)

5. KEY INSIGHTS:
   - Set lookup (i not in d) is O(1) average case, making this efficient
   - We preserve order because we iterate through the original string left-to-right
   - Each character is processed exactly once
"""

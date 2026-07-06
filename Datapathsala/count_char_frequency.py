$QUESTION
"""
Count Character Frequency

Given a string s containing only lowercase letters, return a list of [character, count] pairs sorted alphabetically by character. Only include characters that appear at least once. Counts should be returned as strings.

Example 1

Input:

s = "abracadabra"

Output:

[["a","5"],["b","2"],["c","1"],["d","1"],["r","2"]]

Explanation:

a appears 5 times
b appears 2 times
c appears 1 time
d appears 1 time
r appears 2 times

The result is sorted alphabetically by character.

Example 2

Input:

s = "aaa"

Output:

[["a","3"]]

Explanation:
Only a is present, appearing 3 times.

Example 3

Input:

s = "zyx"

Output:

[["x","1"],["y","1"],["z","1"]]

Explanation:
Each character appears once. The result is sorted alphabetically: x, y, z.
"""

# SOLUTION METHOD 1 (MANUAL FREQUENCY COUNTING)

def charFrequency(self, s: str) -> List[List[str]]:
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        freq_list = []
        for i in sorted(freq):
            freq_list.append([i, freq[i]])
        return freq_list

# SOLUTION METHOD 2 (USING dict.get() + LIST COMPREHENSION)

class Solution:
    def charFrequency(self, s):
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        return sorted([[c, str(cnt)] for c, cnt in freq.items()])

# EXPLANATION

"""
METHOD 1 (MANUAL FREQUENCY COUNTING):
======================================

Time Complexity: O(n + k log k) 
  - O(n): Iterate through the string once to count frequencies
  - O(k log k): Sort the k unique characters in the dictionary
  where n = length of string, k = number of unique characters

Space Complexity: O(k) where k is the number of unique characters
  - We store at most 26 characters (lowercase only) in the dictionary

Logic:
------
1. Initialize empty dictionary 'freq' to store character -> count mappings

2. Iterate through each character in string s:
   - If character already exists in freq: increment its count (freq[i] += 1)
   - If character doesn't exist: add it with count 1 (freq[i] = 1)
   - After this loop, 'freq' contains all unique characters with their frequencies

3. Initialize empty list 'freq_list' to store results

4. Iterate through sorted keys of freq dictionary:
   - sorted(freq) sorts all unique characters alphabetically (a-z)
   - For each character 'i', append [character, count] pair to freq_list
   - Note: Count remains as integer (not converted to string)

5. Return freq_list with alphabetically sorted [char, count] pairs

Example Trace (s = "abracadabra"):
──────────────────────────────────
Step 1: Build frequency dictionary
  a → 1, b → 1, r → 1, a → 2, c → 1, a → 3, d → 1, a → 4, b → 2, r → 2, a → 5
  freq = {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

Step 2: Sort and build result
  sorted(freq) = ['a', 'b', 'c', 'd', 'r']
  Result: [['a', 5], ['b', 2], ['c', 1], ['d', 1], ['r', 2]]


METHOD 2 (USING dict.get() + LIST COMPREHENSION):
==================================================

Time Complexity: O(n + k log k)
  - Same as Method 1
  - List comprehension is O(k) and sorted() is O(k log k)

Space Complexity: O(k) where k is the number of unique characters

Logic:
------
1. Initialize empty dictionary 'freq'

2. Iterate through each character 'c' in string s:
   - freq[c] = freq.get(c, 0) + 1
   - freq.get(c, 0): Returns count of 'c' if it exists, else returns 0 (default)
   - Add 1 to the count and update the dictionary
   - This is more concise than the if-else approach in Method 1

3. Use list comprehension to create result:
   - [[c, str(cnt)] for c, cnt in freq.items()]
   - Iterate through all (character, count) pairs in freq
   - Convert count to string using str(cnt)
   - Create [character, count_as_string] pairs

4. Use sorted() on the list comprehension:
   - sorted() sorts the list by first element (character) alphabetically
   - Returns list of [character, count_as_string] pairs in sorted order

Example Trace (s = "abracadabra"):
──────────────────────────────────
Step 1: Build frequency dictionary
  freq = {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

Step 2: List comprehension and sort
  Before sort: [['a', '5'], ['b', '2'], ['r', '2'], ['c', '1'], ['d', '1']]
  After sort: [['a', '5'], ['b', '2'], ['c', '1'], ['d', '1'], ['r', '2']]


COMPARISON:
===========

Method 1 Advantages:
- Explicit and easy to understand for beginners
- Clear step-by-step logic

Method 1 Disadvantages:
- More verbose code
- Requires separate loops for frequency and result building

Method 2 Advantages:
- More Pythonic and concise
- Uses dict.get() which is cleaner than if-else
- Single-line comprehension makes code compact
- Counts are automatically converted to strings

Method 2 Disadvantages:
- May be harder to understand for beginners
- Less explicit flow

Recommendation:
===============
Method 2 is preferred in production code due to:
- Cleaner, more Pythonic syntax
- Better readability for experienced Python developers
- dict.get() is safer and more idiomatic
- Fewer lines of code = fewer potential bugs

Key Insights:
=============
1. Dictionary frequency counting is the standard approach for this problem
2. dict.get(key, default) is safer than manually checking if key exists
3. sorted() works on dictionaries by sorting keys (characters) alphabetically
4. List comprehension with sorted() is idiomatic Python
5. Time complexity O(n + k log k) is optimal where n = string length, k = unique chars
6. For lowercase only, k ≤ 26, so space complexity is effectively O(1)
"""

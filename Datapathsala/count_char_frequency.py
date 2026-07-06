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
# SOLUTION

def charFrequency(self, s: str) -> List[List[str]]:
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        freq_list = []
        for i in sorted(freq):
            freq_list.append([i,freq[i]])
        return freq_list
  # another solution
  class Solution:
    def charFrequency(self, s):
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        return sorted([[c, str(cnt)] for c, cnt in freq.items()])

#EXPLANATION

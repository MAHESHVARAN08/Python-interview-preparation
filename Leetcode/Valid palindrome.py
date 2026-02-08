"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""
#Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = ""
        for i in s:
            if i.isalnum():
                palin+=i.lower()
            else:
                continue
        return palin == palin[::-1]

  # Time complexity = o(n) , space complexity = o(n) 

"""
Explanation

1. will create a empty string which will hold the plaindrome
2. iterate through the string upto N
3. if a character in a string is alphanum then append it to palin with lowercase else continue
4. retrun palin and the reverse of it in the form of boolean

"""

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""
# Solution - sorting method - time cmplexity - o(n log n ), space - o(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)/2
        max_majority = 0
        nums.sort()
        i=0
        while i < len(nums):
            count=1
            while i+count<len(nums) and nums[i]==nums[i+count]:
                count+=1
            if count > majority:
                return nums[i]
            i+=count

# Hashmap - time - o(n) , space - o(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)/2
        freq = dict()
        for i in nums:
            freq[i] = freq.get(i,0)+1
            if freq[i] > majority:
                return i
        


        
            

        
        


        

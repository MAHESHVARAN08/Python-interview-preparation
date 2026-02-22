"""
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.
Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.

"""
#Two pass solution - it will traverse two time upto N
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if len(arr)==1:  # if length of an array is one then there is no second largest
            return -1
        maxi = max(arr) # first pass upto N - it will find the largest element in an array
        second_max = 0
        for i in range(len(arr)):   # second pass upto N - it will find an second largest element
            if arr[i] < maxi and arr[i]>second_max:
                second_max=arr[i]
        if second_max==0:  # if all the elements are same then second_max will till 0 only
            return -1
        return second_max

  #One pass solution - it will traverse one time upto N - Interview optimal
  class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if len(arr)==1:  # if length of an array is one then there is no second largest
            return -1
        maxi = 0
        second_maxi = 0
        for i in range(len(arr)): # first pass upto N - it will find the largest and second largest element in an array
            if arr[i]>maxi:
                second_maxi = maxi
                maxi = arr[i]
            elif arr[i] < maxi and arr[i] > second_maxi:
                second_maxi = arr[i]
        if second_maxi==0:  # if all the elements are same then second_max will till 0 only
            return -1
        return second_maxi
                
            

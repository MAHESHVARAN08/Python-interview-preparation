"""


Given a 2D array arr[][], where arr[i][0] is the starting time of ith meeting and arr[i][1] is the ending time of ith meeting,
the task is to check if it is possible for a person to attend all the meetings such that he can attend only one meeting at a particular time.

Note: A person can attend a meeting if its starting time is greater than or equal to the previous meeting's ending time.

Examples:

Input: arr[][] = [[1, 4], [10, 15], [7, 10]]
Output: true
Explanation: Since all the meetings are held at different times, it is possible to attend all the meetings.
Input: arr[][] = [[2, 4], [9, 12], [6, 10]]
Output: false
Explanation: Since the second and third meeting overlap, a person cannot attend all the meetings.

"""
# solution

class Solution:
    def canAttend(self, arr):
        # Code Here
        arr.sort()  # sort the array first then only we will get the meeting schedules in order
        count=0  # counter for successfull meeting attends
        for i in range(len(arr)-1):
            if arr[i][1]<=arr[i+1][0]: # check the meeting end time of current meeting and the meeting start time of the next meeting 
                count+=1 # increse the couter for successfull meeting 
        if count == len(arr)-1:  # if counter and no of meetings -1 is equal then a person can attend all meeting without overlap else false 
            return True
        else:
            return False
        
        

 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        arr = list(set(arr))
        arr.sort()
        count=1
        n=len(arr)
        maximum = -1e9
        
        for i in range(n-1):
            if arr[i+1] - arr[i] != 1:
                maximum = max(maximum, count)
                count=1
                
            else:
                count+=1
            
            maximum = max(maximum, count)
        return maximum 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().longestConsecutive(a))
        print("~")
# } Driver Code Ends
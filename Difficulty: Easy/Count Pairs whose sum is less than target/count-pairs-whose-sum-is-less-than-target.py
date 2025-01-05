#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        
        arr.sort()
        n=len(arr)
        count = 0
        
        i = 0  # Start pointer
        j = len(arr) - 1  # End pointer
        count = 0  # Initialize count
        while i < j:
            sum_val = arr[i] + arr[j]
            if sum_val < target:
                count += (j - i)  # This counts how many valid pairs exist between i and j
                i += 1  # Move left pointer to the right to increase sum
            else:
                j -= 1  # Move right pointer to the left to decrease sum

                    
        return count

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
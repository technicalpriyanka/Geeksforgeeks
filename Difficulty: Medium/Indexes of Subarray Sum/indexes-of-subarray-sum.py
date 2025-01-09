#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        # Initialize a hashmap to store the cumulative sum and its index
        prefix_sum = {}
        curr_sum = 0
        
        for i in range(len(arr)):
            # Add the current element to the cumulative sum
            curr_sum += arr[i]
            
            # Check if the current sum equals the target
            if curr_sum == target:
                return [1, i + 1]
            
            # Check if the difference between the current sum and target exists in the hashmap
            if (curr_sum - target) in prefix_sum:
                return [prefix_sum[curr_sum - target] + 2, i + 1]
            
            # Store the current cumulative sum with its index
            prefix_sum[curr_sum] = i
        
        return [-1]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends
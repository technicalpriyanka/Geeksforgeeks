#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def calculateSpan(self, arr):
        #write code here
        n = len(arr)
        ans = [0] * n  # To store the span values
        stack = []  # Stack to store indices of elements in arr
        
        for i in range(n):
            # Pop elements from the stack that are smaller than or equal to arr[i]
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            
            # If stack is empty, the span is i + 1 (all previous elements are smaller)
            if not stack:
                ans[i] = i + 1
            else:
                # The span is the difference between current index and the index at top of the stack
                ans[i] = i - stack[-1]
            
            # Push the current index to the stack
            stack.append(i)
        
        return ans

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        print("~")
        t -= 1
# } Driver Code Ends
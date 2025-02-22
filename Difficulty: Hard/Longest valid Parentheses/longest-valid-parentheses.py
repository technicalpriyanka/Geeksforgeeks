
class Solution:
    def maxLength(self, s):
        # code here
        maximum = 0
        stack = []
        dp = [0]*len(s)
        for i,c in enumerate(list(s)):
            if c == '(':
                stack.append(i)
            elif stack:
                pop_ind  = stack.pop()
                
                if s[pop_ind] == '(':
                    dp[i] = i - pop_ind + 1 + dp[pop_ind - 1]
                    maximum = max(maximum, dp[i])
                    
                else:
                    stack = []
                    
        return maximum
#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))
        print("~")

# } Driver Code Ends
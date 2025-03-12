#Back-end complete function Template for Python 3

class Solution:
    def minCostClimbingStairs(self, cost):
        stair_case = stair = 0
        for co in cost:
            stair_case, stair = stair, min(stair_case, stair) + co
        return min(stair_case, stair)


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array
    obj = Solution()
    res = obj.minCostClimbingStairs(arr)
    print(res)
    print("~")

# } Driver Code Ends

class Solution:
    def countTriplets(self, arr, target):
        # code here
        from collections import defaultdict
        m = defaultdict(int)
        for item in arr:
            m[item] += 1
            
            
        ans = 0 
        for i in range(len(arr)):
            m[arr[i]] -= 1
            for j in range(0, i):
                res = target - arr[i] - arr[j]
                ans += m[res]
                    
        return ans
        
        
        

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        ans = ob.countTriplets(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends
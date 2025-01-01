#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        # arr.sort()
        # unique_set=set(arr)
        # if len(unique_set) == 1:
        #     return -1
        # else:
        
        large=max(arr) #largest element from array
        for i in range(len(arr)-1, -1, -1):
            arr=sorted(arr)
            if arr[i] < large:
                return arr[i]
        return -1
            

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends
class Solution:
	def kLargest(self, arr, k):
		# Your code here
		ans=[]
		arr=sorted(arr)
		l=len(arr)
		for i in range(k):
		    ans.append(arr[l-1-i])
		    
		return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.kLargest(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends
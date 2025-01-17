#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        n=len(arr)
        count=0
        prod=1
        for i in range(n):
            if arr[i]==0:
                count+=1
                continue
            else:
                prod*=arr[i]
                
        if count  > 1:
            return [0 for i in range(n)]
            
        res=[0 for i in range(n)]
        for i in range(n):
            if count==1:
                if arr[i]==0:
                    res[i]=prod
                else:
                    res[i]=0
                    
            else:
                res[i]=prod//arr[i]
                
                
        return res
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends
#User function Template for python3

class Solution:

    def countPS(self, s):
        ans=0
        
        for i in range(len(s)):
            # odd length
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>=2:
                    ans+=1
                l-=1
                r+=1
            # even length
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>=2:
                    ans+=1
                l-=1
                r+=1
        return ans




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.countPS(s))

        print("~")
# } Driver Code Ends
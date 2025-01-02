#User function Template for python3

class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        # return the count
        bits=0
        i=0
        while (1<<i)<=n:
            cycle=1<<(i+1)
            full_cycle=n//cycle
            rem=n%cycle
            bits+=full_cycle*(1<<i)
            bits+=max(0,rem+1-(1<<i))
            i += 1
        return bits


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
        print("~")
# } Driver Code Ends
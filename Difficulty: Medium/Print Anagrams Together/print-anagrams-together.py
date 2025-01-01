#User function Template for python3


class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        dic=dict()
        for i in arr:
            l=sorted(i)
            st="".join(l)
            dic[st]=[]
            
            
        for i in range(len(arr)):
            l=sorted(arr[i])
            st="".join(l)
            if st in dic.keys():
                dic[st].append(i)
                
        ans=[]
        for j in dic.values():
            l=[]
            for i in j:
                l.append(arr[i])
            ans.append(l)
            
        ans.sort()
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends
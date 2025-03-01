
class Solution:
    def decodedString(self, s):
        # code here
        def decode(i):
            d = 0
            while s[i].isdigit():
                d = d * 10 + ord(s[i]) - ord("0")
                i += 1
            assert s[i] == "["
            i += 1
            out = []
            while s[i] != "]":
                if s[i].isdigit():
                    i, sub = decode(i)
                    out.append(sub)
                else:
                    out.append(s[i])
                    i += 1
            return i + 1, "".join(out) * d
        
        out, i, n = [], 0, len(s)
        while i < n:
            i, sub = decode(i)
            out.append(sub)
        return "".join(out)
 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends
#User function Template for python3

class Solution:
    def isSubSequence(self, A, B):
        #code here
        start = 0
        count = 0
        for char in A:
            if start < len(B):
                for i in range(start, len(B)):
                    if char == B[i]:
                        start = i +1
                        count += 1
                        break
                    else:
                        continue
                    
                    
        if count == len(A):
            return True
        else:
            return False
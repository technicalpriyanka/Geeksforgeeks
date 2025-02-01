class Solution:
	def isWordExist(self, mat, word):
		#Code here
		m, n = len(mat), len(mat[0])

        def dfs(r, c, index):
            if index == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or mat[r][c] != word[index]:
                return False

            mat[r][c], temp = '*', mat[r][c]
            res = dfs(r - 1, c, index + 1) or dfs(r + 1, c, index + 1) or dfs(r, c - 1, index + 1) or dfs(r, c + 1, index + 1)
            mat[r][c] = temp
            return res

        return any(dfs(r, c, 0) for r in range(m) for c in range(n) if mat[r][c] == word[0])


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            mat.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(mat, word)
        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
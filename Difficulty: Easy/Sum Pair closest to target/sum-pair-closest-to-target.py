#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # code here
        # arr.sort()
        # for i in range(len(arr)):
        #     for j in range(1, len(arr)):
        #         if arr[i] + arr[j] == target:
        #             return arr[i], arr[j]
                    
                
        if len(arr) < 2: return []
        arr.sort()
        left, right, closest, result = 0, len(arr) - 1, float('inf'), []
        while left < right:
            s = arr[left] + arr[right]
            if abs(target - s) < abs(target - closest) or (
                abs(target - s) == abs(target - closest) and abs(arr[left] - arr[right]) > abs(result[0] - result[1])):
                closest, result = s, [arr[left], arr[right]]
            left, right = (left + 1, right) if s < target else (left, right - 1)
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends
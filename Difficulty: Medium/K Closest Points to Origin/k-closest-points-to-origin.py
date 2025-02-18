#{ 
 # Driver Code Starts
#Initial Template for Python 3
from typing import List


# } Driver Code Ends

import math
from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Your code here
        dist = []
        heapify(dist)
        for x,y in points:
            ec_dis = math.sqrt((x)**2 + y**2)
            if len(dist)<k: heappush(dist, [-ec_dis, [x,y]])
            else:
                if ec_dis < abs(dist[0][0]):
                    heapreplace(dist, [-ec_dis, [x,y]])
        res = []
        while dist:
            res.append(dist[0][1])
            heappop(dist)
        return res

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        k = int(input())
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append([x, y])
        
        solution = Solution()
        ans = solution.kClosest(points, k)
        ans.sort()
        for point in ans:
            print(point[0], point[1])
        print("~")

# } Driver Code Ends
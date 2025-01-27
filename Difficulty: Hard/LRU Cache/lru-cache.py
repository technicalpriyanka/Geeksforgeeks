#User function Template for python3

# design the class in the most optimal way

class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self, cap):
        #code here
        self.cap = cap
        self.s = []
        self.res = []
        
        
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        for i in range(len(self.s)):
            if self.s[i][0] == key:
                self.s.append(self.s.pop(i))
                self.res.append(self.s[-1][1])
                return self.s[-1][1]
        self.res.append(-1)
        return -1
        
        
        
    #Function for storing key-value pair.   
    def put(self, key, value):
        #code here
        #for checking if key already exist
        for i in range(len(self.s)):
            if self.s[i][0] == key:
                self.s[i][1] = value
                self.s.append(self.s.pop(i))
                return
        #checking for new key
        if len(self.s) < (self.cap):
            self.s.append([key, value])
        else:
            self.s.pop(0)
            self.s.append([key, value])




#{ 
 # Driver Code Starts
#Initial Template for Python 3


def inputLine():
    return input().strip().split()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        capacity = int(input())
        cache = LRUCache(capacity)

        queries = int(input())
        for __ in range(queries):
            vec = inputLine()
            if vec[0] == "PUT":
                key = int(vec[1])
                value = int(vec[2])
                cache.put(key, value)
            else:
                key = int(vec[1])
                print(cache.get(key), end=" ")
        print()
        print("~")

# } Driver Code Ends
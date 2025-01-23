#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.random=None
        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
'''
class Solution:
    #Function to clone a linked list with next and random pointer.
    def cloneLinkedList(self, head):
        # code here
        newhead=Node(head.data)
        node=head.next
        temp=newhead
        while(node!=None):
            i=Node(node.data)
            temp.next=i
            temp=temp.next
            node=node.next
        lo=head
        lc=newhead
        while(lo!=None):
            ro=head
            rc=newhead
            if(lo.random!=None):
                while(ro!=lo.random):
                    ro=ro.next
                    rc=rc.next
                lc.random=rc
            lo=lo.next
            lc=lc.next
        return newhead
    



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None
        self.random = None


class LinkedList:

    def __init__(self):
        self.head = None


def insert(tail, data):
    tail.next = Node(data)
    return tail.next


def setrandom(head, a, b):
    h = head
    i = 1
    while i < a and h:
        h = h.next
        i += 1
    an = h

    h = head
    i = 1
    while i < b and h:
        h = h.next
        i += 1

    if an:
        an.random = h


def validation(head, res):
    headp = head
    resp = res

    d = {}

    while head and res:
        if head == res:
            return
        if head.data != res.data:
            return

        if head.random:
            if not res.random:
                return

            if head.random.data != res.random.data:
                return

        elif res.random:
            return
        if head not in d:
            d[head] = res
        head = head.next
        res = res.next

    if not head and res:
        return
    elif head and not res:
        return

    head = headp
    res = resp
    while head:
        if head == res:
            return
        if head.random:
            if head.random not in d:
                return
            if d[head.random] != res.random:
                return
        head = head.next
        res = res.next

    return True


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        __nodes = list(map(int, input().strip().split()))  # Input for nodes
        __arandom = list(map(
            int,
            input().strip().split()))  # Input for random pairs

        # Length of nodes and random pairs
        __n = len(__nodes)
        __m = len(__arandom)

        # Initialize two linked lists
        __ll = LinkedList()
        __ll2 = LinkedList()

        # Set the head for both linked lists
        __ll.head = Node(__nodes[0])
        __ll2.head = Node(__nodes[0])

        __tail = __ll.head
        __tail2 = __ll2.head

        # Insert the nodes into the linked lists
        for x in __nodes[1:]:
            __tail = insert(__tail, x)
            __tail2 = insert(__tail2, x)

        # Set the random pointers
        for i in range(0, len(__arandom), 2):
            setrandom(__ll.head, __arandom[i], __arandom[i + 1])
            setrandom(__ll2.head, __arandom[i], __arandom[i + 1])

        # Create a deep copy of the list
        obj = Solution()
        __res = obj.cloneLinkedList(__ll.head)

        # Validate the copy
        if __res is None or __res == __ll.head:
            print("false")
            continue

        if validation(__ll.head, __res) and validation(__ll2.head, __res):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
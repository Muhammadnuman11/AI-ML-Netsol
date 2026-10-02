from collections import deque


student = {
    "name" : "Ali",
    "age" : 20,
    "marks" : "85"
}

# print(student)

# A Set stores unique values, it does not allow duplicates
number ={ 0, 1,1,1,1, 2,3 ,3, 3,3, 4 }
# print(number)
# Results {0, 1, 2, 3, 4}


# Stack is a linear data structure that follows the principle of Last In First Out (LIFO). The last element added to the stack will be the first one to be removed. 



# Queue is a linear data structure that follows the principle of First In First Out (FIFO). The first element added to the queue will be the first one to be removed.

# Examples 
queue = deque()
queue.append(1) 
queue.append("Ali") 
queue.append("Ahmed") 
# print(queue)

queue.popleft() # remove the first element from the queue
# print(queue)


# Linked List is a linear data structure where each element is a separate object. Each element (we will call it a node) of a list is comprising of two items - the data and a reference to the next node. The last node has a reference to null. The entry point into a linked list is called the head of the list. It should be noted that head is not a separate node, but the reference to the first node. If the list is empty then the head is a null reference.   
# Example of a linked list in Python
# [10] -> [20] -> [30] -> [40] -> [50] -> None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        # create Nodes

        node1 = Node(10)
        node2 = Node(20)
        node3 = Node(30)
        # Connect them:
        node1.next = node2
        node2.next = node3

        # print(node1.data)  # Output: 10
        # print(node1.next.data)  # Output: 20    


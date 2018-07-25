class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next


node1 = Node(12)
node2 = Node(99)
node3 = Node(37)
node4 = Node(99)
node5 = Node(45)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def remove_duplicates(list):
    vals = []
    node = list
    while node != None:
        if node.val not in list:
            vals.append(node.val)
    

#print(node1.next.next.val)

node1.traverse()


node1.traverse()

#linkedlist implementation in python 
class Node:
    def _init_(self,data=None):
        self.data = data
        self.next = None

#
class linkedlist:
    def _init_(self):
        self.head = None   

    def listlist(self):
        new_node =self.head
        while new_node is not None:
            print(new_node.data)
            new_node = new_node.next

list = linkedlist() 
list.head = Node("Mon") 

#create nodes
e2 = Node("Tue")
e3 = Node("Wed")

#link first node to second node 
list.head.next =e2

#link second node to third node 
e2.next = e3

list.listlist()
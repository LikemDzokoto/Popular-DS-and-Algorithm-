class Node:
  def __init__(self, data=None,):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def show(self):
    node = self.head
    while node is not None:
      print(node.data)
      node = node.next

  def add(self, new,):
    new_node = Node(new)
    new_node.next = self.head
    self.head = new_node
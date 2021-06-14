class Node:
	
	def __init__(self,data):
		self.data = data
		self.link = None

class Linkedlist:

	def __init__(self):
		self.head = None

	def insert(self, nextnode):	
		if self.head:
			lastnode = self.head

			while lastnode.link:

				lastnode = lastnode.link

			lastnode.link = nextnode
		else:
			self.head = nextnode


	def read(self):
		nextNode = self.head
		while nextNode:
			print(nextNode.data, end=" => ")
			nextNode = nextNode.link
			
linkedList = Linkedlist()
nodeA = Node("Agam")
linkedList.insert(nodeA)

nodeB = Node("good")
linkedList.insert(nodeB)

nodeC = Node("scene")
linkedList.insert(nodeC)

nodeD = Node("on")
linkedList.insert(nodeD)

linkedList.read()

			



			
		
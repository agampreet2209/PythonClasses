class Node:
	def __init__(self,data):
		self.data = data
		self.link = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None


	# high time complexity O(n)
	def insertLast(self, data):	
		# for first element
		if (self.head == None):
			self.head = Node(data)
			return
		node = self.head
		while node.link != None:
			node = node.link
		node.link = Node(data)
		# for using insertlast2 on same object
		self.tail = node.link


	# low time complexity O(1)
	def insertLast2(self, data):	
		# for first element
		if (self.head == None):
			self.head = Node(data)
			self.tail = self.head
			return
		self.tail.link = Node(data)
		self.tail = self.tail.link


	def insertAfter(self, oData, nData):	
		# for first element
		if (self.head == None):
			return "empty list"
		node = self.head
		nNode = Node(nData)
		while node != None:
			if node.data == oData:
				node.link, nNode.link = nNode, node.link
				return f"{oData} Found"
			node = node.link
		return f"{oData} Not Found"


	def delete(self, data):
		print("deleting...", data)
		if (not self.head):
			return "empty list"
		node = self.head
		if node.data == data:
			self.head = node.link
			return f"{data} Found"
		prev = None
		while node:
			if node.data == data:
				prev.link = node.link
				return f"{data} Found"
			prev, node = node, node.link
		return f"{data} Not Found"


	def update(self, oData, nData):
		if (self.head == None):
			return "empty list"
		node = self.head
		while node:
			if node.data == oData:
				node.data = nData
				return "data updated"
			node = node.link
		return f"{data} Not Found"
	

	def read(self):
		nextNode = self.head
		while nextNode:
			print(nextNode.data, end=" => ")
			nextNode = nextNode.link
		print()



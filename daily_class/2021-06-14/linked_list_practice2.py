
class Node:
	def __init__(self,data):
		self.data = data
		self.link = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None


	def insertLast(self, data):	
		if (not self.head):
			self.head = Node(data)
			return
		node = self.head
		while node.link != None:
			node = node.link
		node.link = Node(data)
		self.tail = node.link


	def insertLast2(self, data):	
		if (self.head == None):
			self.head = Node(data)
			self.tail = self.head
			return
		self.tail.link = Node(data)
		self.tail = self.tail.link
	
	def read(self):
		cursor = self.head
		if not cursor: 
			print("emptylist")
			return
		while cursor:
			print(cursor.data, end=" => ")
			cursor = cursor.link 
		print()

	
	def delete(self, data):
		cursor = self.head
		if not cursor: 
			return "empty list"
		prev = None
		while cursor:
			if cursor.data == data:
				if prev:
					prev.link = cursor.link
				else:
					self.head = cursor.link
				return f"{data} deleted"
			prev = cursor
			cursor = cursor.link 
		return f"{data} not found"

	def update(self, odata, ndata):
		cursor = self.head
		if not cursor: 
			return "empty list"
		while cursor:
			if cursor.data == odata:
				cursor.data = ndata
				return f"{odata} updated to {ndata}"
			cursor = cursor.link 
		return f"{odata} not found"
		

		







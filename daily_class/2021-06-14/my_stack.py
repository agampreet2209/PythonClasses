

"""
 B -> C -> D -> A
"""


class Node:
	def __init__(self,data):
		self.data = data
		self.link = None

class Stack:
	def __init__(self):
		self.top = None

	def push(self, data):
		if self.top:
			node = Node(data)
			node.link, self.top =  self.top, node
		else:
			self.top = Node(data)
		return f" v {data} pushed on top"

	def pop(self):
		if self.top:
			self.top, data = self.top.link, self.top.data
			return f" ^ {data} poped"
		else:
			return "empty stack"


stack = Stack()
print(stack.push("Agam"))
print(stack.push("CM"))
print(stack.push("RADHA"))
print(stack.push("RAJ"))
print(stack.push("ASLAM"))


print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack.push("RAJ"))
print(stack.push("ASLAM"))

print(stack.pop())
print(stack.pop())





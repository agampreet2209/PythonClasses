# Linked list
# A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.
# Difference between a list/array and linked list is Linked list is not stored at contigous memory locations while list/Array is stored at contigous memory locations


# Types Linked List
# 1.Singly Linked List
# 2.Circular Linked List
# 3.Doubly Linked List



#  Singly linked list

'''
			link             link            link
	Node A -------> Node B -------> Node C ------->  Node D -------> null
	   ^
	   |
	   |
	  head
	
	A Node is an Object which contains a value and a link to next Node

'''

# Circula Linked List

'''
		---------------------------------------------------------------
	   |															   |
	   v	link             link            link             link     |
	Node A -------> Node B -------> Node C ------->  Node D -----------
	   ^
	   |
	   |
	  head
	
	A Node is an Object which contains a value and a link to next Node, and last node points link to head node

'''

# Doubly Linked List
'''
			link             link            link
	Node A -------> Node B -------> Node C ------->  Node D -------> null
		   <------         <------ 		   <------          <------
	   ^
	   |
	   |
	  head
	
	A Node is an Object which contains a value and a link to next Node

'''


'''
Why Linked List?
Arrays can be used to store linear data of similar types, but arrays have the following limitations.
1) The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage.
2) Inserting a new element in an array of elements is expensive because the room has to be created for the new elements and to create room existing elements have to be shifted.

For example, in a system, if we maintain a sorted list of IDs in an array id[].

id[] = [1000, 1010, 1050, 2000, 2040].
'''



# Advantages Single Linked List:
# 1) Dynamic size
# 2) Ease of insertion/deletion


#  Drawbacks Single Linked List:
#  1) Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists efficiently with its default implementation. Read about it here.
#  2) Extra memory space for a pointer is required with each element of the list.
#  3) Not cache friendly. Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists



# Example of Linked List creation with Python

class Node:

	def __init__(self, data):
		self.data = data
		self.link = None


class LinkedList:

	def __init__(self):
		self.head = None

	def insert(self, nextNode):
		if self.head:
			# assume head is last node
			lastNode = self.head
			# check whether head has a link or not
			while lastNode.link:
				# if last node has a link then we will assign link to lastNode
				lastNode = lastNode.link
			# now we have lastNode, we will assign nextNode to its link
			lastNode.link = nextNode
		else:
			self.head = nextNode

	def read(self):
		nextNode = self.head
		while nextNode:
			print(nextNode.data, end=" => ")
			nextNode = nextNode.link


linkedList = LinkedList()
nodeA = Node("Agam")
linkedList.insert(nodeA)

nodeB = Node("CM")
linkedList.insert(nodeB)

nodeC = Node("Tom")
linkedList.insert(nodeC)

nodeD = Node("Jerry")
linkedList.insert(nodeD)

linkedList.read()












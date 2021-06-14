import linked_list_practice2 as ll3


linkedList = ll3.LinkedList()


linkedList.insertLast2("Agam")
linkedList.insertLast2("preet")
linkedList.insertLast2("singh")
linkedList.insertLast2("go")
linkedList.insertLast2("for")
linkedList.insertLast2("it")

linkedList.read()

print(linkedList.delete("Agam"))
linkedList.read()

linkedList.update("singh", "just")
linkedList.read()



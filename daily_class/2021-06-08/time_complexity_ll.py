import linked_list2 as ll2
import timeit


# start time
start = timeit.default_timer()

linkedList = ll2.LinkedList()
for x in range(1,1000):
	linkedList.insertLast2("Agam")
	#print("inserting at", x)

# stop time
stop = timeit.default_timer()

print('insertLast2 Time: ', stop - start)  



# start time
start = timeit.default_timer()

linkedList2 = ll2.LinkedList()
for x in range(1,1000):
	linkedList2.insertLast("Agam")
	#print("inserting at", x)

# stop time
stop = timeit.default_timer()

print('insertLast Time: ', stop - start)  

mylist = ["Fortuner", "Z900", "Porsche 718"]
print(mylist)

list1 = ["Roadtrips", 718, True]
print(list1)

#It is also possible to use the list() constructor when creating a new list
newlist = list(("Toyota", "Kawasaki","Porsche"))
print(newlist)

thislist = ["Ferrari", "Lamborghini", "Porsche"]
if "Ferrari" in thislist:
    print("Ferrari is in the list")

#To change the value of a specific item, refer to the index number
mylist = ["Fortuner", "Z900", "Porsche 718"] 
mylist[1] = "Multistrada"  
print(mylist)

#To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values
mylist = ["Fortuner", "Z900", "Porsche 718"] 
mylist[0:2] = ["Endeavour", "Street Triple"]
print(mylist)

#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
mylist = ["Fortuner", "Z900", "Porsche 718"] 
mylist[0:1] = ["Endeavour", "Street Triple"]
print(mylist)

#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
mylist = ["Fortuner", "Z900", "Porsche 718"] 
mylist[1:3] = ["Endeavour"]
print(mylist)
#We do not have item specified in index[2]. We only mentioned Endeavour to be replaced in index[1]. So Z900 will be replaced as Endeavour and index[2] will be remained as empty and Porsche 718 will be moved to index[3].

#To insert a new list item, without replacing any of the existing values, we can use the insert() method
mylist = ["Fortuner", "Z900", "Porsche 718"] 
mylist.insert(2, "Lamborghini Huracan")
print(mylist)
#Lamborghini Huracan will be inserted in index[2] and Porsche 718 will be moved to index[3]

#To add an item to the end of the list, use the append() method
mylist = ["Fortuner", "Z900", "Porsche 718"] 
mylist.append("Nissan GTR")
print(mylist)

#To insert a list item at a specified index, use the insert() method
mylist = ["Fortuner", "Z900", "Porsche 718"] 
mylist.insert(1, "Nissan GTR")
print(mylist)

#To append elements from another list to the current list, use the extend() method
mylist = ["Fortuner", "Z900", "Porsche 718"] 
thislist = ["Ferrari", "Lamborghini", "Porsche"]
mylist.extend(thislist)
print(mylist)

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)
mylist = ["Fortuner", "Z900", "Porsche 718"] 
thistuple = ("Triumph", "Ducati", "Kawasaki")
mylist.extend(thistuple)
print(mylist)

#The remove() method removes the specified item
mylist = ["Fortuner", "Z900", "Porsche 718"] 
mylist.remove("Z900")
print(mylist)

#The pop() method removes the specified index
mylist = ["Fortuner", "Z900", "Porsche 718"] 
mylist.pop(2)
print(mylist)

#If you do not specify the index, the pop() method removes the last item
mylist = ["Fortuner", "Z900", "Porsche 718"] 
mylist.pop()
print(mylist)

#The del keyword also removes the specified index
mylist = ["Fortuner", "Z900", "Porsche 718"] 
del mylist[0]
print(mylist)

#The del keyword can also delete the list completely
# mylist = ["Fortuner", "Z900", "Porsche 718"] 
# del mylist
# print(mylist)

#The clear() method empties the list
mylist = ["Fortuner", "Z900", "Porsche 718"] 
mylist.clear()
print(mylist)

newlist = ["Ducati","Triumph","Kawasaki"]
for x in newlist:
    print(x)

newlist = ["Ducati","Triumph","Kawasaki"]
for i in range(len(newlist)):
    print(newlist[i])

newlist = ["Ducati","Triumph","Kawasaki"]
i = 0
while i < len(newlist):
    print(newlist[i])
    i=i+1

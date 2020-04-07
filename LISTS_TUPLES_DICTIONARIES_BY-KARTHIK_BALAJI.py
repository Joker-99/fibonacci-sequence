#TASK 1: ASSIGNING ELEMENTS TO DIFFERENT LISTS

 #create a list
mylist1 = [1,2,3,'orange','apple','mango']
mylist2 = [4,5,6,'choco','vanilla','grapes']
print(mylist1)
print(mylist2)

#to addd or remove items
mylist1.append('banana')
print(mylist1)

mylist2.remove(6)
print(mylist2)

#to print a range
print(mylist1[1:-1])
print(mylist2[2:-1])

#TASK 2: ACCESSING ELEMENTS FROM A TUPLE

#create a tuple
mytuple=(1,2,3,4,'english','tamil','french')
print(mytuple)

#to access the elements
print(mytuple[3])

#to print a range
print(mytuple[2:-2])
#note: elements cannot be removed or added to a tuple unlike lists.



#DELETING DICTIONARY ELEMTS

#create a dictionary
mydict = {'name':'Karthik', 'age':'20', 'height':'170cm', 'weight':'75kg'}
print(mydict)

#delete elements
mydict.pop('weight')
print(mydict)

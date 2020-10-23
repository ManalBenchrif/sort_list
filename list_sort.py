#Sort the list alphabetically:
#The sort() method sorts the list ascending by default.
#You can also make a function to decide the sorting criteria(s).

#Syntax :list.sort(reverse=True|False, key=myFunc)
#reverse:	Optional. reverse=True will sort the list descending. Default is reverse=False
# key	Optional. A function to specify the sorting criteria(s)

#Sort the list ascending:
liste=["manal","khadija","houda","lamiae"]
print(liste)
liste.sort()
print("Sort the list ascending: ",liste)
print()

##Sort the list descending:
liste=["manal","khadija","houda","lamiae"]
print(liste)
liste.sort(reverse=True)
print("Sort the list descending: ",liste)
print()

#Example :Sort the list by the length of the values:
def lenght_list(list1):
    return len(list1)

list1=["Fatimazahra","manal","salsabile","nouha","fatiha","khadija","sondos","ali"]
list1.sort(reverse=True,key=lenght_list)
print("sort using criteria: ",list1)



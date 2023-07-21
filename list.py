"""
List is a collection which is ordered and changeable. Allows duplicate members.
syntax:list=[int,str,float]
he lists are ordered.
The element of the list can access by index.
The lists are the mutable(change)type.
The lists are mutable types.
A list can store the number of various elements.
"""
#here just give all same datatype val
list1=[10,20,30]
print(list1)
#let us give different val
list2=('anu',25,90.78)
print(list2)
#lets check two list if two list are it should return True
l1=[1,2,'python',20.9]
l2=[1,2,'python',20.9]
print(l1 == l2)
#Acess list values through their index val '

list_val=[1,4,5,6,7,9]
print("values:",list_val)
#now lets acess the val positive indexing
print(list_val[5])
#Negative Indexing
print((list_val[-2]))
print((list_val[-2:]))
print((list_val[2:]))
print(list_val[:4])
#can we have lists in list Lets try../
list3=l1+l2
print(list3)
# USe list constructor to create a list
#here we declated values inside round braces but in output it shows in square.
List_const=list((1,2,3,4,4))
print(List_const)
#updating list val
list_val=[1,4,5,6,7,9]
#lets insert the val
list_val[3]=44
print(list_val)
#adding multiple val
list_val[1:5]=[22,33]
print(list_val)
#Adding at the element at the end
list_val[-1]=55
print(list_val)
#Now let us see list operations:
#repetation-->*
#first declare the list
list_rep=[1,2,3,3,4,5,6,7,8]
print(list_rep)
list=list_rep*3
print(list)
#concatination
l1=[1,2,'python',20.9]
l2=[1,2,'python',20.9]
l=l1+l2
print(l)
#len of the list
print(len(list_rep))
#iterating the list
list_rep=[1,2,3,3,4,5,6,7,8]
for i in list_rep:
    print(i)
#list build in
#sort In asscending order
"""
in sort method we have 2 extra parameters 
1. reverse --If True, the sorted list is reversed (or sorted in Descending order)
2. key-
"""
list_rep=[1,2,3,3,4,5,6,7,8,1]
list_rep.sort()
print(list_rep)
#sort in descending order
list_rep.sort(reverse=True)
print(list_rep)
#reverse
list_rep.reverse()
print(list_rep)
#pop
"""
here if doesnt give any index val it simply del the last ele of the list 

"""

list_rep.pop()
print(list_rep)
#copy

# mixed list
prime_numbers = [2, 3, 5]

# copying a list
numbers = prime_numbers.copy()


print('Copied List:', numbers)

#reverse
# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# reverse the order of list elements
prime_numbers.reverse()


print('Reversed List:', prime_numbers)

# Output: Reversed List: [7, 5, 3, 2]
#insert
# create a list of vowels
vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3 (4th position)
vowel.insert(3, 'o')


print('List:', vowel)

# Output: List: ['a', 'e', 'i', 'o', 'u']

#extend
# create a list
prime_numbers = [2, 3, 5]

# create another list
numbers = [1, 4]

# add all elements of prime_numbers to numbers
numbers.extend(prime_numbers)


print('List after extend():', numbers)

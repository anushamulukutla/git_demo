"""

A Python set is the collection of the unordered items.

Each element in the set must be unique, immutable, and the sets remove the duplicate elements.
Sets are mutable which means we can modify it after its creation.

Unlike other collections in Python, there is no index attached to the elements of the set, i.e.,
 we cannot directly access any element of the set by the index
 here in sets we use {}

"""
#creating  a set

set_1={1,2,3,4,8,102,78,58}
print(set_1)

#now here lets create a set with duplicate val and print them
set_2={1,2,2,2,2,23,3,4,5,5,5,5,7}
print(set_2)
#{1, 2, 3, 4, 5, 23, 7}

#Using set() method
Days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
print(Days)
print(type(Days))
print("looping through the set elements ... ")
for i in Days:
    print(i)

"""

after adding ele to sets it
set never follows a sequence .it just prints the list randomly
and it also removes the dupliccates
the reason is set uses the concept of hash .it fetches the ele as fast as possible 

"""

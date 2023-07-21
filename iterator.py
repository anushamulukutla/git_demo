"""
iterator name itseklf says it iterates the val


syntax:
iter(object,sentinel )
object can be a list and
sentinal -- a special value that is used to represent the end of a sequence


iter() and next

"""
#example for iter()
nums=[1,2,3,4,5,6]
print(iter(nums))#it gives list_iterator object at 0x10d5d3e50
#so get the vl in the list just give next()
iterable_nums=iter(nums).__next__()#it give the first value

print(iterable_nums)#o/p 1




# list of vowels
vowels = ["a", "e", "i", "o", "u"]

# iter() with a list of vowels
vowels_iter = iter(vowels)

print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))





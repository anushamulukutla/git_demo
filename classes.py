class Cal(object):
    # pi is a class variable
    pi = 3.142

    def __init__(self, radius):
        # self.radius is an instance variable
        self.radius = radius

    def area(self):
        pi=1
        return Cal.pi * (self.radius ** 2)

obj1=Cal(2)
pi_val=obj1.pi
print(pi_val)
radius=obj1.area()

print(radius)
class SuperClass(object):
    superpowers = []

    def __init__(self, name):
        self.name = name

    def add_superpower(self, power):
        self.superpowers.append(power)

foo = SuperClass('foo')
bar = SuperClass('bar')
foo.name
# Output: 'foo'

bar.name
# Output: 'bar'

foo.add_superpower('fly')
bar.add_superpower('walk')
print(bar.superpowers)
print(foo.superpowers)
# Output: ['fly']

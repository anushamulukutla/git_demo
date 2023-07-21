

#importing threading module
# time
from time import sleep
from threading import *
#create a thread class
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(2)
class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(2)

obj1=Hello()
obj=Hello()
obj2=hi()
obj1.start()
obj.start()
print(Hello.is_alive(obj1))
sleep(0.2)#it gives a gap between two threads to avoid collision
obj2.start()
obj1.join()
obj2.join()
print("I am done ")#this is called bymain thread(pyhton main thread)
#to avoid such ccollision weneed to wait till the thread completes its execution
obj1.setName("Anusha")
print(Hello.is_alive(obj1))
print(hi.is_alive(obj2))
print(Hello.getName(obj1))
print("__________________________________________________")



#class Humon:
    #height =175
    #progress = 20
    #def info(self):
        #print('I am Human')
#class Student(Humon):
    #progress = 15
    #def info(self):
        #print('I am Student')

#class Worker(Humon):
    #salary = 1000

#stud = Student()
#worker = Worker()

#print(stud.height)
#print(worker.height)

#print(stud.progress)
#print(worker.progress)
#print(worker.salary)

#stud.info()

#class Grandparent:
    #height = 170
    #age = 60
    #home = "Будинок в селі"
#class Parent(Grandparent):
    #age = 40

#class Child(Parent):
    #height = 100

    #def __init__(self):
        #print(self.height)
        #print(self.age)
        #print(self.home)

#child = Child()

#class SuperTest:

    #def _test1(self):
        #print("Test1")

    #def test2(self):
        #self._test1()
        #self.__test3()

    #def __test3(self):
        #print("Test3")

#class Test(SuperTest):
    #def print(self):
        #self.test2()
        #self._test1()
        #self.__test3()

#class Student:

# def __init__(self, age):
# self.__age = age

    #def getAge(self):
        #return self.__age

    #def setAge(self, age):
        #if age < 0 or age > 100:
            #return
        #self.__age = age

#st = Student(15)
#print(st.getAge())
#st.setAge(20)
#print(st.getAge())

class Animals:
   age = 3
   height = 40

class Sawci(Animals):
    def run(self):
        print("Я вмію бігати")



class Ptaky(Animals):
    def flight(self):
        print("Я вмію літати")

    def sing(self):
        print("Я вмію співати")

class gorobci(Ptaky):
    pass


class Synicy(Ptaky):
    pass


class Kit(Sawci):
    def info(self, name):
        self.name = "dog"

class Dog(Sawci):
    def info(self, name):
        self.name = "kit"
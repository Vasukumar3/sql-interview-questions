#Syntax
#class classname():
    #attr
    #methods


# class person_details():# class definition
#     user_name = "kiran" # attributes
#     emp_id = 1234 #attributes
#     def details(self): #methods
#         print(f"working at MNC company",self.user_name)
#     def details_2(self): #methods
#         print(f"he runs ABC company",self.emp_id)
#         self.details()
#Syntax
# objname = classname()
# raj_kumar = person_details()
# raj_kumar.details()
# print(raj_kumar.emp_id)
# raj_kumar.details_2()



# class mobile_phone():#class definition
#     brand_name = "samsung" #attribute
#     color = "white" #attribue
#     storage = "128GB"
#     def calling(self,bn): #method
#         print(f"you are calling from .......... {bn}")
#     def message(self,pn):
#         print(f"message sent successfully to {pn}")
#     def camera(self):
#         print(f"photo captured... internal storage {self.storage}")
#     def browsing(self):
#         print(f"network issuee... {self.brand_name}")
#syntax
# samsung = mobile_phone()
# samsung.calling("samsung")
# samsung.message(123456879)
# samsung.browsing()
# samsung.camera()
# samsung.message()
# apple = mobile_phone()
# apple.calling("apple")
# apple.message(123456789000)
# oppo = mobile_phone()
# oppo.calling("oppo")
# oppo.message(7889489)



# class laptop():
#     def __init__(self,bn,color,storage,model):
#         self.bn = bn
#         self.color = color
#         self.storage = storage
#         self.model = model
#     def gaming(self):
#         print(f"you are gaming biohazard4 on {self.bn}")
#     def browsing(self,browser):
#         print(f"you are browsing from laptop  {self.bn} {browser}")
#     def movies(self):
#         print(f"you are watching movies... {self.storage}")
# lenova = laptop("lenova","white","500gb",2025)
# lenova.gaming()
# lenova.browsing("moziila")
# # lenova.movies()
# msi = laptop("msi","black","1TB",2025)
# msi.gaming()
# msi.browsing("chrome")


#TASK
# class ATM():
#     def __init__(self,branchname,location,model):
#         pass
#     def credit(self):
#         pass
#     def withdraw(self):
#         pass
#     def blance(self):
#         pass
# sbin = ATM()
# while True:




########################  august 22 2025 ####################

# class mobilephone():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def make_call(self,number):
#         print(f"calling {number} from {self.brand} {self.model}")
#     def send_message(self,message,number=1234567890):
#         print(f"sending {message} from {number}")
#objname = classname()
# nokia = mobilephone("nokia",2012)
# nokia.make_call(1234567890)
# nokia.send_message("good morning")


# class mobilephone():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def make_call(self,number):
#         print(f"calling {number} from {self.brand} {self.model}")
#     def send_message(self,message,number=1234567890):
#         print(f"sending {message} from {number}")
# class smartphone(mobilephone):
#     def browsing(self):
#         print(f"you are browsing from {self.brand}")
#     def app(self,appname):
#         print(f"using {appname} app on {self.brand}")
# nokia = smartphone("nokia",2014)
# nokia.browsing()
# nokia.app("spotify")
# nokia.make_call(1234568790)
# nokia.send_message("hii")






#one baseclass multiple derived class (sibilings)
# class a():
#     def parent(self):
#         print("this is parent class")
# class b(a):
#     def child1(self):
#         print("this is child 1 class")
# class c(a):
#     def child2(self):
#         print("this is child 2 class")
# obj1 = b()
# obj1.parent()
# obj1.child1()
# obj2 = c()
# obj2.parent()
# obj2.child2()







# class parent1():
#     def father(self):
#         print("this is father class")
# class parent2():
#     def mother(self):
#         print("this is mother class")
# class child(parent1,parent2,):
#     def child(self):
#         print("this is child class")

# obj = child()
# obj.father()
# obj.mother()
# obj.child()




# class gfather():
#     def output(self):
#         print(f"earned 100cr properties")
# class father(gfather):
#     def output1(self):
#         print(f"this is father class")
# class child(father):
#     def output2(self):
#         print(f"this is child class")
# obj = child()
# obj.output2()
# obj.output1()
# obj.output()





# polymorphism ---> implementing same thing in different forms
#two types
#1. overloading --> 1. operator overloading 2.method overloading
#2. method overriding






#operator overloading
# '+'
# ( + )
# a = 10
# b = 20
# print(a+b)


# a = "kiran"
# b = "raju"
# print(a+b)




# method overloading ---> 
# method name should be same
# arguments must be different ---> in the terms of length or type of arguments


# class calculator():
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# obj = calculator()
# obj.add(10,20,30)
# obj.add(10,20)


# class calculator():
#     def add(self,a=45698,b=123,c=20):
#         print(a,b,c)
# obj = calculator()
# obj.add(10,20,30)
# obj.add(10,20)
# obj.add(10)
# obj.add()



# method overloading ---> 
# method name should be same
# arguments must be different ---> in the terms of length or type of arguments

# class calculator():
#     def add(self,a=5,b=55,c=555):
#         print(a+b+c)
# obj = calculator()
# obj.add(10,20,30)
# obj.add("vasu","kumar","palani")
# obj.add("vasu","kumar","rajesh")
# obj.add()
# obj.add()



#2. method overriding
# # 2.method overriding--> method name should be same, arguments should be also same length
# class gfather():
#     def details(self,a):
#         print("this is gfather class",a)

# class father(gfather):
#     def details(self,a):
#         print("this is father class",a)
#         super().details("100cr")
# obj = father()
# obj.details("100cr")

# class gfather():
#     def output(self):
#         print(f"earned 100cr properties")
# class father(gfather):
#     def output(self):
#         print(f"this is father class")
#         super().output()
# class child(father):
#     def output(self):
#         print(f"this is child class")
#         super().output()
# obj = child()
# obj.output()





############## oops august 26 2025  #################

# class gfather():
#     def __init__(self,a):
#         self.a = a
#         print("this is base class",a)
# obj = gfather("100Cr")

#public
#protect _
#private __



# class gfather():
#     def __init__(self,a):
#         self._a = a
#         print("this is base class ",a)
# class father(gfather):
#     def display(self,):
#         print(f"this is dervied class",self._a)
# obj = father("100cr")
# obj.display()



# class gfather():
#     def __init__(self,a):
#         self.__a = a
#         print("this is base class ",a)
# class father(gfather):
#     def display(self,):
#         print(f"this is dervied class",self._a)
# obj = father("100cr")
# obj.display()







#abstraction --> hiding the implementation and showing only essential part

# 1.abstract class --> class which contain abstract methods is called abstract class
# 2.abstract method --> the method which is having only declaration but not the definition is called abstract method (hiding the implementation)
# class which does not have abstract method is called concrete class
# concrete class  --> class without abstract methods
# object cannot create for abstract class
# object can create only concrete classes
# To create abstract classes in Python, you can use the abc (Abstract Base Classes) module

# from abc import ABC,abstractmethod
# class abstract_demo(ABC):
#     @abstractmethod
#     def display(self):
#         pass
#     @abstractmethod
#     def display2(self):
#         pass
# class demo(abstract_demo):
#     def display(self):
#         print(f"implementation done in derived class")
#     def display2(self):
#         print(f"implementation 2 done")
# obj = demo()
# obj.display()
# obj.display2()



# from abc import ABC,abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
# class gpay(payment):
#     def pay(self):
#         print("payment successfull through gpay")
# class phonepe(payment):
#     def pay(self):
#         print("payment successful through phone")
# class cred(payment):
#     def pay(self):
#         print("payment successful through cred")
# gpayment = gpay()
# gpayment.pay()
# phonepepayment = phonepe()
# phonepepayment.pay()
# credpay = cred()
# credpay.pay()




# class mother():
#     def output(self):
#         print(f"this is mother class")
# class father():
#     def output(self):
#         print(f"this is father class")
# class child(father,mother):
#     def output(self):
#         print(f"this is child class")
#         super().output()
#         mother.output(self)
# obj = child()
# obj.output()
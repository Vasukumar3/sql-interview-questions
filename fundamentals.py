# print(exp)--> it used to display the information on the screen

#syntax
# print(exp)
# print(10+10) #20
# print("welcome to pythonlife") #welcome to pythonlife


#below code is used to perform addition operation
# num_1 = 10 #num_1 is variable and i assinged 10 value to that variable
# num_2 = 10
# result = num_1 + num_2
# print(result)
'''
i have taken two variables
and i assigned values to those variables
and i perform addition operation by using + operator
later, i display the information by using print statement
num_1 = 10
num_2 = 10
result = num_1 + num_2
print(result)

'''


"""
i have taken two variables
and i assigned values to those variables
and i perform addition operation by using + operator
later, i display the information by using print statement



"""


#syntax
# variable = value

# age = 35
# print(id(age))
# height = 5.7
# print(id(height))
# employe_id = 1234
# print(id(employe_id))


# _voter_id = 548958
# print(_voter_id)


# 1stperson_name = "kiran kumar"
# print(1stperson_name)


# dept_1 = "front_end"
# print(dept_1)


# age = 35
# print(id(age))
# Age = 45
# print(id(Age))
# AGE = 25
# print(id(AGE))


# IF = 45
# print(IF)

# Variable Cases:
# There are 3 types of variable cases :
# 1.camelCase
# 2.snake_case
# 3.PascalCase



# schoolName = "aditya"


# #snake_case
# school_name = "mahati"


# SchoolName = "chaitanya"
# print(SchoolName)


# roll_number = -1316549849
# print(type(roll_number))

# height = -5498456.8987
# print(type(height))
# print(height)


# strings --> it is used to store textual information , it is used to represent sequence of characters
# sentence = 'welcome to pythonlife '
# print(sentence)
# print(type(sentence))
# sentence_2 = "welcome to pythonlife at 7 O'clock  "
# print(sentence_2)
# print(type(sentence_2))
# sentence_3 = """ 
# 1. this is textual information
# 2. triple quotes used for textual infor

# "he said , "he will atten 7 O'clock" "



# welcome to pythonlife """
# print(sentence_3)
# print(type(sentence_3))




#type conversion --> 1. implicit type conversion(automatic)
#2.explicit type conversion (manual)


#int---> float
# age = 35
# print(type(age))
# float_conversion = float(age)
# print(float_conversion)
# print(type(float_conversion))

# #float --> int
# product_cost = 449.50
# print(product_cost)
# int_coversion = int(product_cost)
# print(int_coversion)
# print(type(int_coversion))


# string --> int
# roll_number = "vasu@124"
# print(roll_number)
# print(type(roll_number))
# int_conversion = int(roll_number)
# print(int_conversion)
# print(type(int_conversion))


# string --> float  task

# input()--> input function allows us to give user inputs(dynamic values)
# num_1 = input("enter something: ")
# print(type(num_1))
# num_2 = input("enter something: ")
# print(type(num_2))
# result = num_1 + num_2
# print(result)


# first_name = "Vasu kumar"
# last_name = "palani"
# print(first_name + last_name)


# print("12345"+"45789")


# num_1 = float(input("enter the first number: "))
# num_2 = float(input("enter  the second number: "))
# print(num_1+num_2)


# num_1 = int(input("enter the number: "))
# num_2 = float(input("enter the number"))
# print(type(num_1+num_2))


# height ="5.7"
# print(type(height))

# product_cost = int(input("enter the product cost: "))
# print(product_cost)
# print(product_cost-50)



# first_person_school_name = "aditya"
# print(first_person_school_name)


##############  august 07 2025 ########
#list

# - A list is a mutable, ordered sequence of elements.
# - Elements can be of different data types.
# - Lists are defined using square brackets `[]`.
# - elements are separated by comma ,

# voter_list = [25,5.7,("pythonlife","vasu"),"kiran",1,2,3,4,1,11,1,1,1]
# print(voter_list)
# print(type(voter_list))
# print(id(voter_list))
# voter_list.append("pythonlife")
# print(voter_list)
# print(id(voter_list))
# sample_list = [1,5.7,"pythonlife",(1,5.7,"kiran"),["sample","oranges",1,1]]
# print(sample_list)

# **Tuples:**

# - A tuple is an immutable, ordered sequence of elements.
# - Similar to lists but cannot be modified once created.
# - Tuples are defined using parentheses `()`.


# sample_tuple = (25,5.7,"pythonlife",["apple","kiran","srinivas",1,5.7,],1,1,)
# print(sample_tuple)
# print(type(sample_tuple))
# sample_tuple.append("pythonlife")
# print(sample_tuple)

# sample = (1,5.7,"kiran",[1,1,1,],(5.7,"kiran"))
# print(sample)


# sample_set = {25,5.7,"rajesh",25,5.7,"rajesh",(25,5.7,"vasu kumar","rajesh","rajesh"),}
# print(sample_set)
# print(type(sample_set))


# user_data = {"user1":"user1@123","user2":"user2@123","user3":"user3@123",}
# print(user_data)
# print(type(user_data))

# sample_dict = {
#     1:"vasu kumar",
#     2:"rajesh",
#     3:"siva varma",
#     # 1:"vasu kumar palani",
#     (1,2):"immutable data type",
#     "user_id":123,
#     4:[1,23],
#     5:(1,23),
#     6:{1:"vasu kumar"},
#     7:{1,2,3},
#     8:"vasu kumar",
#     (1,2):[1,2]
# }
# print(sample_dict)



#boolean
# sample = True
# print(sample)
# print(type(sample))


# sample = False
# print(sample)
# print(type(sample))


# print(bool(1))
# print(bool(0))


# complex data type
# In Python, a complex data type is used to represent complex numbers. A complex number consists of a real part and an imaginary part, and it’s written in the form a + bj
# a+ij  a = realpart + ij imaginary part

# sample = 5+10j
# print(sample)
# print(type(sample))

# sample = 5+10j
# sample_2 = 5+10j
# print(type(sample+sample_2))







#int
#float
#complex
#list
#tuple
#sets
#dictionary
#bool
#strings

# user_data = {
#     1245:"vasukumar",
#     4568:"sharat",
#     7890:"rajesh",
# }

# products ={
#     "rice":99,
#     "oil":145,
#     "sugar":25,
# }



# tuple_1 = ("cxcpp533gh","hgsue789uh",)






# sample = 1,2,3,5.7,"vasu kumar"
# print(type(sample))


# a=b=c=d=1
# print(a)
# print(b)
# print(c)
# print(d)


# a,b,c,d = 1,2,3,4
# print(a)
# print(b)
# print(c)
# print(d)


# a = 10
# b = 20
# print(a)
# print(b)
# a,b = b,a
# print(a)
# print(b)




# voter_list = ["sravani","vasu","rajesh","sharath","srinu","srinu","srinu","vasu"]
# sample = set(voter_list)
# print(sample)
# sample_2 = list(sample)
# print(sample_2)


# voter_id = (123,456,789,125,789,123,456,789,)
# sample = list(voter_id)
# print(sample)
# sample_2 = set(sample)
# print(sample_2)
# sample_3 = tuple(sample_2)
# print(sample_3)

#task ---> 
# tuple --> dict
# dict ---> tuple

# set_1 = {"lekhana","pythonlife",1,2,3,3,4,5,5,6}
# print(set_1)
# sample = tuple(set_1)
# print(sample)



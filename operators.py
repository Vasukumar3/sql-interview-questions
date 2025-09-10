#operators

#operator ---> symbol or keyword that performs an operation on one or more operands
#operand --->  Value or variable acted  upon by an operator to produce a result

# + operator
# num_1 = 10
# num_2 = 20
# result = num_1 + num_2
# print(result)


# - subtraction
# - (Subtraction): Subtracts the right operand from the left operand.

# num_1 = 10
# num_2 = 5
# result = num_1 - num_2
# print(result)

# / (Division): Divides the left operand by the right operand.
# num_1 = 10
# num_2 = 3
# result = num_1 / num_2
# print(result)

# // (Floor Division): Returns the quotient of the division, discarding the fractional part.


# num_1 = 10
# num_2 = 3
# result = num_1 // num_2
# print(result)


# num_1 = 10
# num_2 = 3
# result = num_1 * num_2
# print(result)

# ** (Exponentiation): Raises the base (left operand) to the power of the exponent (right operand).
# num_1 = int(input("enter the value"))
# num_2 = int(input("enter the second value : "))
# # result = num_1 ** num_2
# print(f"base value {num_1} and expo value {num_2} and result is {num_1 ** num_2}")


# % (Modulus): Returns the remainder of the division of the left operand by the right operand.
# num_1 = 1041949
# num_2 = 354547
# result = num_1 % num_2
# print(result)

# a = 10
# b = 3

# addition = a + b
# subtraction = a - b
# multiplication = a * b
# division = a / b
# remainder = a % b
# floor_division = a // b
# exponentiation = a ** b

# print(addition, subtraction, multiplication, division, remainder, floor_division, exponentiation)




# product_cost = 99
# product_cost += 1 #eq --> product_cost = product_cost + 1
# print(product_cost)


# num_1 = 5*3
# num_1 *= 3 #eq --> num_1 = num_1 * 3
# print(num_1)


# person_1_age = 100
# person_2_age = 100
# print(person_1_age == person_2_age) #False
# print(person_1_age != person_2_age) #True
# print(person_1_age < person_2_age) #False
# print(person_1_age <= person_2_age) #True
# print(person_1_age > person_2_age) # False
# print(person_1_age >= person_2_age) # True

# user_name = input("enter the username: ")
# password = input("enter the password: ")
# otp = 12345
# print(user_name == "sharath" and password == "sharath@123" and otp == 12345)
# print(user_name == "sharath" or password == "sharath@123" or otp == 12345)



# sample = True
# print(not sample)

# sample = False
# print(not sample)



# num_1 = 10**101
# print(id(num_1))
# num_2 = 10**101
# print(id(num_2))
# print(num_1 is num_2)


# num_1 = "vasu kumar"
# print(id(num_1))
# num_2 = "vasu kumar2"
# print(num_1 is num_2)
# print(id(num_2))
# print(num_1 is not num_2)



# voter_list=["siva","rajesh","sharath"]
# voter_list_2=["siva","rajesh","sharath"]
# print(voter_list is voter_list_2)


# fruits_list =  ["apples","bananas","oranges"]
# print("grapes" in fruits_list)
# print("grapes" not in fruits_list)

# employee_id = (123,456,789,225,)
# print(456 in employee_id)
# print(456 not in employee_id)

# sample_sentence = "welcome to pythonlife"
# print("w" in sample_sentence)




# product_cost = int(input("enter the product cost: "))
# discount = int(input("enter the discount: "))
# result = product_cost * (discount/100)
# product_cost -= result
# print(f"discount given {discount}%  and final discount {result} and total cost after discount given {product_cost} ")
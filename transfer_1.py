# for i in range(6):
#     print(i)


# for i in range(6):
#     if i == 3:
#         break
#     print(i)

# print(f"last iteration of temporary variable stored {i}")


# employee_id = [12,34,55,66,99,88,45,89,55,56,57,58,59,60,66,61,62,63,64,66,75,78,88]
# for i in employee_id:
#     if i == 66:
#         print(i)
#         break
# print(f"last iteration value {i}")

# Syntax:
# for item in iterable:
#     if condition:

# for i in range(6):
#     if i == 3:
#         continue
#     print(i)
# print("last iteration",i)



# employee_id = [12,34,55,66,99,88,45,89,55,56,57,58,59,60,66,61,62,63,64,66,75,78,88]
# for i in employee_id:
#     if i == 66:
#         print(i)
#         continue
# print(f"last iteration value {i}")


# products = ["ok","ok","ok","defect","ok","ok","defect","ok"]
# for i in products:
#     if i == "defect":
#         continue
#     print(i)



# for i in "pythonlife":
#     print(i)


# for i in ["rajesh","arvind","hruthika","Vasu"]:
#     pass
# print(i)

# **Problem 1: Using `break` in a For Loop**

# Write a Python program that takes a list of numbers as input `numbers = [25, 30, 20, 40, 15, 25]` and prints the sum of the numbers. However, if the sum exceeds 100, stop adding numbers and print "Sum exceeded 100".

# sum = 0
# numbers = [25, 30, 20, 40, 15, 25]
# for i in numbers:
#     sum+=i
#     if sum >=100:
#         break
# print("sum exceeds 100")
# print("sum value is ",sum)
# print(i)



# **Problem 2: Using `continue` in a For Loop**

# Write a Python script that uses a for loop to iterate through numbers from 1 to 600. Print only the odd numbers, skipping the even ones using the `continue` statement.
# stop_value = int(input("enter the number:"))#include
# for i in range(1,stop_value+1):
#     if i%2==0:
#         continue
#     print(i)

# list_1 = []
# print(list_1)
# print(type(list_1))


# list_2 = [1,2,3,"pythonlife",5.7,[1,2,3],1,2,2,2,2]
# print(list_2)
# print(type(list_2))


# list_3 = list()
# print(list_3)
# print(type(list_3))

#Syntax
# var[index]
# my_list = [10, 20, 30, 40, 50]
# print(my_list[3])


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[7])
# print(my_list[3])
# print(my_list[5])
# print(my_list[0])


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[1])#20
# print(my_list[-7])#20
# print(my_list[7])#80
# print(my_list[-1])#80
# print(my_list[-8])#10





# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
#Syntax
# seq[s:s:s]
# print(my_list[1:4])#20 30 40
# print(my_list[4:6])#50 60
# print(my_list[0:8])
# print(my_list[0:8:1])
# print(my_list[0:8:3])
# print(my_list[0:8:4])


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[1:6:1])
# print(my_list[1:6:2])
# print(my_list[1:6:3])


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[0:8:1])
# print(my_list[::])
# print(my_list[4:8])
# print(my_list[4:])
# print(my_list[:3])


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[4:7])#50 60 70
# print(my_list[-4:-1])


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[1:4])
# print(my_list[-7:-4])


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[::-1])
# print(my_list[::-1])
# print(my_list[5:2:-1])#60 50 40
# print(my_list[-3:-6:-1])#60 50 40


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[6:0:-1])#70 60 50 40 30 20
# print(my_list[-2:-8:-1])#70 60 50 40 30 20

# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(len(my_list))
# print(my_list[-1])


# sum=0
# n = int(input("enter a numer:  "))
# for i in range (1, n + 1):
#     cube = i ** 3
#     print(f"Cube of {i} is {cube}")
#     sum += cube
# print(f"Final sum of cube of numbers from 1 to {n}: {sum}")



#####################     AUGUST 14 2025  #########

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
#METHOD SYNTAX
# .methodname()
# .methodname(arguments)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(numbers)
# numbers.append([25,5.7,"pythonlife",True])
# print(numbers)



# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(numbers)
# numbers.extend([25,5.7,"pythonlife",True])
# print(numbers)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(numbers)
# sample = numbers.copy()
# print(sample)
# sample.append("pythonlife")
# print(sample)
# print("og",numbers)

# numbers.clear()            # Removes all elements from the list

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.clear()
# print(numbers)

# numbers.count(2)           # Returns the number of occurrences of a specified item in the list.
# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5,"srinivas","srinivas","vasu"]
# print(numbers.count("srinivas"))


# Returns the index of the first occurrence of a  specified item in the list.
# numbers = [3, 4, 1, 5, 9, 2, 6, 5,1,1,]
# print(numbers.index(1))


# numbers.remove(1)          # Removing the first occurrence of 1
# numbers = [3, 4, 1, 5, 9, 2, 6, 5,1,1,]
# numbers.remove(1)
# print(numbers)

# list_1 = [25,35,8,18,5]
# print(list_1[2])
# list_1.remove(8)
# print(list_1)
# print(list_1[2])


# numbers.pop(4)             # Removing element at index 4
# numbers = [3, 4, 1, 5, 9, 2, 6, 5,1,1,]
# obj = numbers.pop(3)
# print(obj*3)
# print(numbers)

# numbers.insert(2, 10)      # Inserting 10 at index 2
# numbers = [3, 4, 1, 5, 9, 2, 6, 5,1,1,]
# numbers.insert(1,"pythonlife")
# print(numbers)


# numbers = [3, 4, 1, 5, 9, 2, 6, 5,1,1,]
# numbers.reverse()
# print(numbers)

# numbers = [3, 4, 1, 5, 9, 2, 6, 5,1,1,]
# print(numbers[::-1])

# numbers = [3, 4, 1, 5, 9, 2, 6, 5,1,1,]
# numbers.sort(reverse=True)
# print(numbers)




# numbers = [3, 4, 1, 5, 9, 2, 6, 5,1,1,]
# print(len(numbers))
# print(numbers[3])

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[1][1])
# print(matrix[2][2])
# print(matrix[0][2])


# Syntax
# [expression for item in iterable]

# empty_list = []
# for i in range(6):
#     result = i*i
#     empty_list.append(result)
# print(empty_list)

# # [expression for item in iterable]
# result = [i*i for i in range(6)]
# print(result)

# print([i*i for i in range(6)])




# empty_list = []
# for i in [25,48,68,44,24,78,35,1,2,3,4,7,77,8,9,4]:
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)


# # [exp for item in iter if cond]
# result = [i for i in [25,48,68,44,24,78,35,1,2,3,4,7,77,8,9,4] if i%2==0]
# print(result)


# print([i for i in [25,48,68,44,24,78,35,1,2,3,4,7,77,8,9,4] if i%2==0])

#remove
# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5,3,3,3,3,3,3,4,4,4,]
# numbers.remove(3)
# print(numbers)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5,3,3,3,3,3,3,4,4,4,]
# for i in numbers:
#     if i == 3:
#         numbers.remove(i)
# print(numbers)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5,3,3,3,3,3,3,4,4,4,]
# empty_list = []
# for i in numbers:
#     if i!=3:
#         empty_list.append(i)
# print(empty_list)

#index ---> task

# age = 3
# if age!=3:
#     print(age)
# set_1 = {1,2,"sets",5.7,(1,2,3),25,25,25,25,35,}
# print(set_1)


# set_2 = set()
# print(type(set_2))


# voter_id = {258,35,45,78,99,"string",7894,5.7}
# voter_id.add("pythonlife")
# print(voter_id)

# voter_id = {258,35,45,78,99,"string",7894,5.7}
# voter_id.clear()
# print(voter_id)

# voter_id = {258,35,45,78,99,"string",7894,5.7}
# sample = voter_id.copy()
# print("sample",sample)
# sample.add("ajay")
# print("sample",sample)
# print(f"orginal set {voter_id}")

# voter_id = {"Raju","ravi","ajay","srikant","siva"}
# voter_id.pop()
# print(voter_id)

# voter_id = {"Raju","ravi","ajay","srikant","siva"}
# voter_id.remove("ravi")
# print(voter_id)

# voter_id = {"Raju","ravi","ajay","srikant","siva"}
# new_set = {"kiran","vasu","ajay",}
# voter_id.update(new_set)
# print(voter_id)

# set_1 = {1,2,3,4,5}
# set_2 = {1,4,5,6,7,8,9}
# set_3 = set_1.union(set_2)
# print(set_3)


# set_1 = {1,2,3,4,5}
# set_2 = {1,4,5,6,7,8,9}
# set_3 = set_1.intersection(set_2)
# print(set_3)


# set_1 = {1,2,3,4,5}
# set_2 = {1,4,5,6,7,8,9}
# set_3 = set_1.symmetric_difference(set_2)
# print(set_3)


# set_1 = {1,2,3,4,5}
# set_2 = {1,4,5,6,7,8,9}
# set_3 = set_2.difference(set_1)
# print(set_3)

# voter_id = {25,45,89,85}
# voter_id_2 = {11,22,33,44}
# print(voter_id.isdisjoint(voter_id_2))

# set_1 = {1,2,3,4,5}
# set_2 = {1,2,}
# print(set_1.issuperset(set_2))
# print(set_2.issubset(set_1))


# voter_name = {"raju","ravi","kiran"}
# voter_name_2 = {"raju","ravi","kiran","pythonlife"}
# print(voter_name_2.issuperset(voter_name))
# print(voter_name_2.issubset(voter_name))
# print(voter_name.issubset(voter_name_2))


# set_1 = {1,2,3,4,5}
# print(set_1)
# set_1.add("pyhonlife")
# print(set_1)

# set_2 = frozenset(set_1)
# print(set_2)
# set_2.add("raj kumar")
# print(set_2)

#TASK
# union
# intersection
# difference
# symmdi


######################  TUPLE ################
# tuple_1 = ()
# print(tuple_1)
# print(type(tuple_1))



# tuple_2 = (1,2,3,5.7,"pythonlife",True,(1,2,3),11,1,11,1,1,1)
# print(tuple_2)


# tuple_3 = tuple()
# print(tuple_3)



tuple_4 = 25,45,"raju",5.7
print(tuple_4)
print(type(tuple_4))





# product_cost = (99,101)
# print(len(product_cost))
# print(product_cost.count(499))
# print(product_cost.index(499))
# product_cost_2 = (99,101,999,9999,499,4999,499,499,499,498,1000,9999)
# print(product_cost + product_cost_2)
# product_cost = (99,101)
# print(product_cost*10)


# fruits = ('apple', 'banana', 'orange')
# print("apple" in fruits)
# print("apple" not in fruits)


# tuple_1 = ()
# print(all(tuple_1))


# Item		Price
# --------------------
# Apple		99.00
# Banana	99.00
# Milk		49.00
# --------------------
# Total		247.00


# items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
# print(f"Item\tPrice")
# print("-"*25)
# total = 0
# for i,j in items:
#     print(f"{i}\t{j}")
#     total+=j
# print("-"*25)
# print(f"Total\t{total}")


# items = {"apple":99,"banana":99,"milk":49}
# for i,j in items.items():
#     print(i,j)
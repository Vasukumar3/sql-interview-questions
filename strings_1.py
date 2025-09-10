# single_quoted_string = 'Hello, World!'
# print(single_quoted_string)
# double_quoted_string = "Python String's"
# print(double_quoted_string)
# triple_quoted_string = '''Triple quotes allow he said, "welcome to pythonlife"
# strings to span multiple lines.'''
# print(triple_quoted_string)


# sample = ""
# print(sample)
# print(type(sample))


# sample_2 = str()
# print(sample_2)
# print(type(sample_2))




# sample = "pythonlife"
# # print(len(sample))
# print(sample[2])
# print(sample[-8])
# print(sample[9])
# print(sample[-1])


# sample = "pythonlife august"
# print(sample[11])


# sample_3 = "pythonlife"
# print(sample_3[2:5])
# print(sample_3[-8:-5])
# print(sample_3[4:1:-1])
# print(sample_3[-6:-9:-1])


# message = "welcome to pythonlife join by 7:00 O'clock "
# sample = message.upper()
# print(sample)
# print(message)

# message = "welcome to PYTHONLIFE join BY 7:00 O'clock "
# lower = message.lower()
# print(lower)

# sentence = "This is a sample sentence."
# count_i = sentence.count('e')
# print(count_i)


# whitespace_string = "   This is a string with leading and trailing whitespace.   "
# print(len(whitespace_string))
# stripped_string = whitespace_string.strip()
# print(len(stripped_string))
# print(stripped_string)


# split(separator): Splits the string into a list of substrings based on the specified   separator.
data = "Pythonlife,Kiran,123456,Pythonlife,Kiran,123456,Pythonlife,Kiran,123456,Pythonlife,Kiran,123456"
data1 = data.split(',')
print(data1)


# original_string = "Python is fun!"
# modified_string = original_string.replace('Python', 'pythonlife')
# print(modified_string)


# filename = "example.txt"
# starts_with = filename.startswith("ex")
# ends_with = filename.endswith(".txt")
# print(starts_with) 
# print(ends_with) 


# email_list = ["example1@gmail.com", "example2@yahoo.com", "example3@gmail.com", "example4@hotmail.com","example5@outlook.com"]
# empty_list = []
# for i in email_list:
#     if i.endswith("@gmail.com"):
#         empty_list.append(i)
# print(empty_list)


# # [exp for item in iterable if cond]
# result = [i for i in email_list if i.endswith("@gmail.com")]
# print(result)





# sentence = "This is a sentence."
# position_a = sentence.find('z')
# position_i = sentence.index('z')
# print(position_a)  
# print(position_i)

# text = "python programming pythonlife"
# capitalized_text = text.capitalize()
# print(capitalized_text)

# numeric_string = "12345"
# alpha_string = "Python"
# is_numeric = numeric_string.isdigit()
# is_alpha = alpha_string.isalpha()
# print(is_numeric)  
# print(is_alpha)  


# word_list = ['Hello', 'World']
# joined_string = ' '.join(word_list)

# print(joined_string)



# text = input("enter the something: ")
# punctuations = """ !\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~ """
# empty = []
# for i in text:
#     if i in punctuations:
#         empty.append(i)
# print(empty)
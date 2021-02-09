# 1. Write an expression that initializes the dictionary my_dict
# my_dict to be the empty dictionary
my_dict = dict()

# 2. Write an expression that initializes the dictionary my_dict
# my_dict to contain two key/value pairs: "Joe" : 1 and "Scott" : 2
my_dict = {'Joe': 1,
            'Scott':2}

# 3. Given the dictionary my_dict from the previous question, 
# write a Python statement that adds the key/value pair "John" : 3
my_dict['John'] = 3

# 4. Given the dictionary my_dict from the previous question,
# write three expressions that return True if the dictionary 
# my_dict whether the keys "Joe" , "Scott" , and "John", respectively, and False otherwise

print('Joe' in my_dict)
print('Scott' in my_dict)
print('John' in my_dict)
print('Steven' in my_dict)

# 5. Write a function is_empty(my_dict) that takes a dictionary my_dict and returns 
# True if my_dict is empty and False otherwise

def is_empty(my_dict):
    if my_dict == dict():
        return True
    else:
        return False

test_dict = dict()
print(is_empty(my_dict))
print(is_empty(test_dict))


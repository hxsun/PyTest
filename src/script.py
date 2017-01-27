# numbers = [1, 2, 3]
# strings = ["test1", "test2"]
# names = ["John", "Eric", "Jessica"]
# 
# # write your code here
# second_name = names[1]
# 
# 
# # this code should write out the filled arrays and the second name in the names list (Eric).
# print(numbers)
# print(strings)
# print("The second name on the names list is %s" % second_name)
# 
# def my_function_with_args(myname, greetings):
#     print("Hi %s, I wish %s"%(myname, greetings))
#     
# my_function_with_args("Kenneth", "all my best")


import random
def lottery():
    for i in range(6):
        yield random.randint(1, 40)
        
    yield random.randint(1, 15)
    
for random_number in lottery():
    print("And the next number is ... %d" % (random_number))
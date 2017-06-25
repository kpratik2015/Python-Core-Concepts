def variable_change_test( some_var, some_list ):
	some_var = 21; #NOTE: We are creating a new local variable using assignment operator
	some_list.append(4)
	print("some_var inside function: ", some_var) 
	print("some_list inside function: ", some_list)
	return

some_var = 11
some_list = [1,2,3]
variable_change_test(some_var, some_list)
print("-------------------------")
print("some_var outside function: ", some_var)
print("some_list outside function: ", some_list) 

'''
OUTPUT SO FAR:
some_var inside function:  21
some_list inside function:  [1, 2, 3, 4]
-------------------------
some_var outside function:  11
some_list outside function:  [1, 2, 3, 4]
-------------------------
'''


print("-------------------------")

def arguements_test( a, b="default argument"):
	print("a: ", a)
	print("b: ", b)
	return	
arguements_test( a="keyword argument" )

'''
OUTPUT SO FAR:
a:  keyword argument
b:  default argument
-------------------------
'''


print("-------------------------")

def variable_length( must_arg, *zero_or_more_arguments ):
	print(must_arg)
	list_collect = []
	for var in zero_or_more_arguments:
		list_collect.append(var)
	print(list_collect)
	return

variable_length(1,2,3,4,5)

'''
OUTPUT SO FAR:
1
[2, 3, 4, 5]
'''

print("--------- EXTRA -----------")

items = ["String 1", "String 2", 6754.23, 574.34, "String 3", 999]

def parse_lists(abc):
    str_list_items = []
    num_list_items = []
    for i in abc:
        if isinstance(i, float) or isinstance(i, int):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items.append(i)
        else:
            pass
    return str_list_items, num_list_items


print(parse_lists(items))

'''
OUTPUT SO FAR:
--------- EXTRA -----------
(['String 1', 'String 2', 'String 3'], [6754.23, 574.34, 999])

'''
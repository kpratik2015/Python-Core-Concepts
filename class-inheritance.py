class Base:
	some_list = [] 				# common to every instance
	def __init__(self, name):
		self.name = name 		# particular to each instance

class DerivedClass(Base):
	def update_list(self, something):
		self.some_list.append(something)

baseObj = Base("First Base")

'''
derived class object has to fulfill __init__
argument requirement since it does not implement 
its own __init__
'''

deriveObj = DerivedClass("First Derive") # name is particular to each instance

print(deriveObj.some_list) # derived object has inherited properties & behaviors of base

deriveObj.update_list("item1")

print(deriveObj.name) 

print(baseObj.name)

print(baseObj.some_list)

print(deriveObj.some_list)

'''
MULTIPLE INHERITANCE:

class DeriveMultiple( Base1, Base2, ..., Basen ):
	.
	.
	.


'''
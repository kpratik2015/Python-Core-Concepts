class ClassExample:
	"""Documentation part """
	attribute = "Class Variable"  # class varirable which is shared by all its instances
	
	def function(self): # self == object/instance
		return "Function called"
	
	def __init__(self, instance_var): # Constructor like. No return statement. Only initialization
		self.inst_var = instance_var  # unique to each instance

obj = ClassExample("Instance Variable")

print(
		obj.attribute,
		"\n"+obj.inst_var,
		"\n"+obj.function(),
		"\n"+obj.__doc__
	)

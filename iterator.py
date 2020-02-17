# Built-in iterators 

# Iterating over a list 
print("List Iteration") 
l = ["Python", "Excels", "Python"] 
for i in l: 
	print(i) 
	
# Iterating over a tuple (immutable) 
print("\nTuple Iteration") 
t = ("Python", "Excels", "Python") 
for i in t: 
	print(i) 
	
# Iterating over a String 
print("\nString Iteration")	 
s = "Python"
for i in s : 
	print(i) 
	
# Iterating over dictionary 
print("\nDictionary Iteration") 
d = dict() 
d['pincode'] = '560036'
d['city'] = 'Bangalore'
for i in d : 
	print("%s %d" % (i, d[i]) )

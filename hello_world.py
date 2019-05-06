print("Hello World!")
x = "Hello Python"
print(x)
y = 42
print(y)

# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variablecopy
name = "Noelle"
print(name, ", ", name, ", the first ", name )	# with a comma
print(name + ", " + name + ", the first " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("my number ", 42 )	# with a comma
print("my number" + str(42) )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love {} and {}".format(fave_food1, fave_food2) ) # with .format()
print(f"I love {fave_food1} and {fave_food2}") # with an f string

"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("X : %d, Y : %2f, Z: %s" % (x, y, z)) # NOTE: The output on y is showing 2.245520 instead of 2.25

print("X : %d, Y : %.2f, Z: %s" % (x, y, z)) # NOTE: Missed the decimal before 2 in the above, working now

# Use the 'format' string method to print the same thing
print("{} {} {}".format(x, y, z))

# Finally, print the same thing using an f-string
print(F"{x} {y} {z}")
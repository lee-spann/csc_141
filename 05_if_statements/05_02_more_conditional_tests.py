

#Test for equality and inequality with strings
print("red" == "red") #True
print ("red" != "red") #False

#Tests using the lower() method
print("HELLO".lower() == "hello")  # True
print("HELLO".lower() == "HELLO")  # False

# Numerical tests involving equality and inequality, 
# greater than and less than, greater than or equal to, 
# and less than or equal to
print(5 > 3)  # True
print(5 == 10)  # False

# Tests using the and keyword and the or keyword
print((5 > 3) and (10 > 7))  # True
print((5 > 3) and (10 < 7))  # False

print((5 > 3) or (10 < 7))  # True
print((5 < 3) or (10 < 7))  # False

#Tests whether an item is in a list
print(3 in [1, 2, 3, 4, 5])  # True
print(6 in [1, 2, 3, 4, 5])  # False

#Tests whether an item is not in a list
print(6 not in [1, 2, 3, 4, 5])  # True
print(3 not in [1, 2, 3, 4, 5])  # False



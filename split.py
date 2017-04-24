# create an empty list to be used for passing data into
int_array = list()

# user input for elements required - i.e enter number for sets of integers you require
num = raw_input("Enter how many integers in the list you want:")

# user input for integers to be added 
print 'Enter the numbers for the array: '

# Loop to go through how many elements user has defined for integers to be added
# This is passed into the int_array variable and assigned to the array
for numbers in range(0, int(num)):
    n = raw_input("numbers:")
    int_array.append(int(n))

# prints the number of integers in the array 
print 'ARRAY contains', numbers, 'integers' 	

# Divide the array into equal sizes of 2
size = 2

# prints the result for the loop which goes through the int_array values
# and gets the length of the array then splits by the size defined
print [int_array[i:i+size] for i  in range(0, len(int_array), size)]


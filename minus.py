import random
"""
Designed for Daniel Guo's Grade 1 subtraction practice.
Subtracting two numbers in which the numbers are in this range: 0 <= number <= 10
No negative answers
"""
file_name = "minus"
my_file = open(file_name, "w")
array=[]

#while the length of the array is less than 48 (in order to make 3 column of 16 on Excel)
while len(array) < 48:
    first = random.randrange(0, 20)
    second = random.randrange(0, 20)
    #only if the first number is greater than the second number
    if first >= second:
        my_file.write(str(first))
        my_file.write("-")
        my_file.write(str(second))
        my_file.write("=")
        #increase the length of the array by 1
        array.append(1)
        my_file.write("\n")
        my_file.write("\n")
    #make 16 set
    if len(array) == 16 or len(array) == 32 or len(array) == 48:
        my_file.write("\n")

my_file.close()

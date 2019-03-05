import random
"""
Designed for Daniel Guo's Grade 1 addition practice
Adding two numbers in which the numbers are in this range: 0 <= number <= 10
"""
file_name = "add"
my_file = open(file_name, "w")

#repeat 48 times (in order to make 3 columns of 16 in Excel)
for i in range(48):
    first = random.randrange(0, 11)
    second = random.randrange(0, 11)
    my_file.write(str(first))
    my_file.write("+")
    my_file.write(str(second))
    my_file.write("=")
    my_file.write("\n")
    my_file.write("\n")
    #separting it into sets of 16
    if i == 15 or i == 31 or i == 47:
        my_file.write("\n")

my_file.close()
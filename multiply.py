import random

"""
Daniel Guo's introduction to multiplcation
"""
file_name = "mulitply"
my_file = open(file_name, "w")

for i in range(48):
    first = random.randrange(0, 5)
    second = random.randrange(0, 5)
    my_file.write(str(first))
    my_file.write("x")
    my_file.write(str(second))
    my_file.write("=")
    my_file.write("\n")
    my_file.write("\n")
    #separting it into sets of 16
    if i == 15 or i == 31 or i == 47:
        my_file.write("\n")

my_file.close()
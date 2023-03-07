# numbers = int(input("Please enter the number till you want to print "))
# steps = int(input("Please enter the steps in range "))
# reference - https://www.programiz.com/python-programming/examples/index-for-loop
# range = range(0, numbers, steps)
for i, item in enumerate(range(5)):
    print(i, item)

print("Break")
# without enumerate
my_list = [21, 44, 35, 11]

for index in range(len(my_list)):
    value = my_list[index]
    print(index, value)

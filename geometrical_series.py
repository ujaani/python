starting_number = input("please type a starting number")
multiply_number = input("please type a number to multiply")
number_print = input("please type the total number of numbers you want to print")

starting_number = int(starting_number)
multiply_number = int(multiply_number)
number_print = int(number_print)

integer = starting_number

for number in range(0,number_print):
    print(integer)
    integer = integer * multiply_number

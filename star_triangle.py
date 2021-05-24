def print_stars_in_a_row(number_of_stars, number_of_spaces):
    for i in range(0, number_of_spaces):
        print(" ", end =" ")
    for x in range(0,number_of_stars):
        print("*", end =" ")

    print("")  # to break the line


starting_number = 1
numbers_to_print = 4
adding_number = 2

stars_to_print = starting_number
spaces_to_print = 3

for number in range(0,numbers_to_print):
    print_stars_in_a_row(stars_to_print, spaces_to_print)
    stars_to_print = stars_to_print + adding_number
    spaces_to_print = spaces_to_print - 1



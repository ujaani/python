starting_number = input(" give starting number ")
ending_number = input("give ending number")
starting_number = int(starting_number)
ending_number = int(ending_number)

if ending_number < starting_number:
    print("ERROR...THE STARTING NUMBER SHOULD ALWAYS BE LESS THAN THE ENDING NUMBER!")
for integers in range(starting_number,ending_number+1):
    if (integers % 2) == 0:
        print(integers)
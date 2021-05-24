first = input("give me a number")
second = input("give me another number")

first_int = int(first)
second_int = int(second)

if first_int > second_int:
    max = first_int
elif first_int == second_int:
    print("both no. are equal. the equal no. is " + first)
    exit(0)
else:
    max = second_int

max_str = str(max)
print("the greater no. is " + max_str)
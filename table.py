number = raw_input("tell me a number ")
value = int(number)
skip = int(number)

for i in range(1, 10):
  print(str(value))
  value += skip
print (str(value))

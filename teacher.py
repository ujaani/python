first = raw_input('give me a number: ')
second = raw_input('give me another number: ')

print '{0:>5}'.format(first)
print '{0:>5}'.format(second)
print '-----------'
students_answer = raw_input()
students_answer = int(students_answer)

first = int(first)
second = int(second)
correct_answer = first + second

if students_answer == correct_answer:
  print 'correct'
  print 'you are a good student'
else:
  print 'wrong'
  print 'try again. please study we
ll'


from random import randrange, seed

seed(11)

randrange(0,11)

math_grades = []

for math_grade in range(8):
  math_grades.append(randrange(0,11))

print('math grades: ', math_grades)
print('length: ', len(math_grades))

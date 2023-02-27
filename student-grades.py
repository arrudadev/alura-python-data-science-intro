import matplotlib.pyplot as plt
from random import randrange, seed

seed(11)

randrange(0, 11)

math_grades = []

for math_grade in range(8):
  math_grades.append(randrange(0, 11))

x = list(range(1, 9))
y = math_grades

print(x)
print(y)

plt.plot(x, y, marker='o')
plt.title('Notas de matemática')
plt.xlabel('Provas')
plt.ylabel('Notas')

# plt.show()
plt.savefig("mygraph.png")

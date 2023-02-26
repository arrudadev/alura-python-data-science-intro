my_age = int(input('Qual é sua idade? '))

def check_can_drive(age):
  if age >= 18:
    print('Tem permissão para dirigir!')
  else:
    years = 18 - age

    print(f'Calma... espere {years} ano(s) para tirar a habilitação!')

check_can_drive(my_age)

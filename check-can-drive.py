my_age = int(input('Qual é sua idade? '))

def check_can_drive(age):
  if age >= 18:
    print('Tem permissão para dirigir!')
  else:
    print('Não tem permissão para dirigir!')

check_can_drive(my_age)

permissions = []
ages = [18, 20, 15, 17, 10, 30]

def check_can_drive(ages_list):
  for age in ages_list:
    if age >= 18:
      permissions.append(True)
    else:
      permissions.append(False)

check_can_drive(ages)

for permission in permissions:
  if permission == True:
    print('Tem permissão para dirigir')
  else:
    print('Não tem permissão para dirigir')

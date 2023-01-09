person = {
  'name':'Moises', 
  'last_name':'Caez Rodriguez',
  'langs':['Python, Javascript'], 
  'age': 99
}

print(person)

person['name'] = 'santi'
person['age'] -= 50
person['langs'].append('rust')
print(person)

del person['last_name']  
person.pop('age')

print(person)

print('item')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())

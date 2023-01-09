#CRUD  Create, Read, Update, Delete

numbers = [1, 2, 3, 4, 5, 6]  
print(numbers[1])
numbers[-1] = 10
print(numbers)
numbers.append(700)  
print(numbers)

numbers.insert(0, 'Hola mundo')
print(numbers)  

numbers.insert(3, 'change')
print(numbers)

tasks = ['todo 1', 'todo 2', "todo 3 ", "todo 4"  ]

new_list = numbers + tasks
print(new_list)

index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

new_list.remove('todo 1')
print(new_list)

new_list.pop()  
print(new_list)

new_list.pop(0)  
print(new_list)

new_list.reverse()
print(new_list)

numbers_a =[1,6,3,5,2,4]
numbers_a.sort()
print(numbers_a)
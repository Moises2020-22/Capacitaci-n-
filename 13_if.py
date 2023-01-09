if True:
  print('deberia ejecutarse')

if False:
  print('nunca se ejecuta')

pet = input(' ¿Cual es tu mascota favorita ' )
if pet == 'perro':
  print('Genial tienes un buen gusto ')

elif pet == 'gato':
  print('espero tengas suerte')
elif pet == 'pez':
  print('eres lo maximo')
else :
  print("no tienes ninguna mascota interesante ")


...


  
  
stock = (input('Digita el stock=>'))
stock = int(stock)

if stock >= 100 and stock <= 1000:
  print("El stock es correcto")
else:
 print("El stock es incorrecto")

number = int(input("Ingrese un numero =>"))
result = number % 2
if (result == 0):
  print("Es par")
else: 
  print("Es impar")


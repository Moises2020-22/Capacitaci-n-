lives = 3
print(type(lives))
buget = 100
age = 21
temperature = 12.12
print(type(temperature))
lives = 2
print(lives)
lives = 1
print(lives)
lives = 12 + 15
print(lives)
lives = lives - 1
print(lives)

number = 45000000000000000000000000.1
print(number)

number_b = 0.000000000000001
print(number_b)

budget_january = input("¿Cual es el presupuesto de enero?")
budget_february = input("¿Cual es el presupuesto de febrero?")
budget_march = input("¿Cual es el presupuesto de marzo? ")

budget_january = int(budget_january)
budget_february = int(budget_february)
budget_march = int(budget_march)

budget_total = budget_january + budget_february + budget_march
print("La suma de los presupuestos es: ", budget_total)

budget_total = int(budget_total)

avg_budget = budget_total / 3
print("El promedio es: ", avg_budget)

name = "Moises"
last_name = "Caez Rodriguez"
my_age = "21"
print(name)
print(last_name)
print(my_age)
full_name = name + " " + last_name
print(full_name)


quote = "I´m Moises"
print (quote)

quote2 = "She said *Hello* "
print(quote2)
# format
template = "Hola, mi nombre es " + name + " y mis apellidos son " + last_name + "y mi edad es" + my_age
print("v1",template)

template = "Hola, mi nombre es {} y mis apellidos son {} y mi edad es {}".format(name,last_name,my_age)
print("v2",template)

template = f"Hola, mi nombre es {name} y mis apellidos son {last_name}  y mi edad es {my_age}"
print("v3",template)
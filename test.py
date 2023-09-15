
lista_numeros = []
for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        lista_numeros.append("FizzBuzz")
    elif numero % 3 == 0:
        lista_numeros.append("Fizz")
    elif numero % 5 == 0:
        lista_numeros.append("Buzz")
    else:
        lista_numeros.append(numero)

print(lista_numeros)







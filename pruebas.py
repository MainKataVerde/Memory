def fibonacci(n):
#Imprimir la serie de Fibonacci hasta un número dado
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()

#fibonacci(2000)

lista = ["A", "B", "C"]
for indice, l in enumerate(lista):
    print(indice, l)
    

mi_lista = [1, 0, 2, 6, 3, 2]

print(mi_lista[1:3])
    


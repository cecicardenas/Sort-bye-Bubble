lista = [23, 78, 45, 8, 32, 56, 1]

for num in lista:
    for num in range(1,len(lista)):
        valor=lista[num]
        j=num-1
        while j>=0 and lista[j]>valor:
            lista[j+1]=lista[j]
            j=j-1
        lista[j+1]=valor
print(lista)
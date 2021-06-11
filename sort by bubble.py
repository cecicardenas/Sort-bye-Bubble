lista = [23,78,45,8,32,56,1,-2000,400,50]

for num in range(len(lista)):
    i=0
    for num in lista:
        if num>lista[i+1]:
            valor = lista[i+1]
            lista[i+1]=num
            lista[i]=valor
        i=1+i 
        if i==(len(lista)-1):
            break
print(lista)
        


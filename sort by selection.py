lista = [5,3,6,4,1,2,200,1000,890321,-20]

menor = min(lista)

pos=lista.index(min(lista))
#print(pos)
i=0
for num in lista:
    lista[pos]=lista[i]
    lista[i]=menor
    #print(lista)
    i=i+1
    if i==(len(lista)):
        break
    menor=min(lista[i:len(lista)])
    pos=lista.index(menor)
print(lista)     

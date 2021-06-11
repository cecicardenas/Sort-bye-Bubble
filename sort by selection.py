'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

lista = [23,78,45,8,32,56]

menor = min(lista)

pos=lista.index(min(lista))
print(pos)
i=0
for num in lista:
    lista[pos]=lista[i]
    lista[i]=menor
    print(lista)
    i=i+1
    if i==(len(lista)):
        break
    menor=min(lista[i:len(lista)])
    pos=lista.index(menor)
print(lista)
        

        
    
        

lista = []
N = int(input())
    
for _ in range(N):
        comando = input().split()
        
        if not comando:  
            continue
            
        if comando[0] == 'insert':
            posicion = int(comando[1])
            numero = int(comando[2])
            lista.insert(posicion, numero)
            
        elif comando[0] == 'print':
            print(lista)
            
        elif comando[0] == 'remove':
            numero = int(comando[1])
            lista.remove(numero)
            
        elif comando[0] == 'append':
            numero = int(comando[1])
            lista.append(numero)
            
        elif comando[0] == 'sort':
            lista.sort()
            
        elif comando[0] == 'pop':
            lista.pop()
            
        elif comando[0] == 'reverse':
            lista.reverse()
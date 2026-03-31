def verificarPrimo(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

valor = int(input('N: '))
if verificarPrimo(valor):
    print('é primo')
else:
    print('não é primo')
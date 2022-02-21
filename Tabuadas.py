print('TABUADA DE MULTIPLICAÇÃO')
num = int(input('Digite o numero: '))
for c in range(1, 11):
    print(' {:2}  x  {:2} =  {:2}'.format(num, c, num * c))

print('TABUADA DE DIVISÃO:')
num = int(input('Digite o numero: '))
for c in range(1, 11):
    print(' {:2}  /  {:2} =  {:2}'.format(num * c, num, c))

print('TABUADA DE ADIÇÃO:')
num = int(input('Digite o numero: '))
for c in range(1, 11):
    print(' {:2}  +  {}  =  {:2}'.format(c, num, num + c))

print('TABUADA DE SUBTRAÇÃO')
num = int(input('Digite o numero: '))
for c in range(0, 11):
    print('{:2}  -  {:2}  =  {:2}'.format(num + c, num, c))
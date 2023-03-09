def fibo(num):
    if num > 1:
        return fibo(num-1) + fibo(num-2)
    return num


num = int(input('Inserisci il numero: ' ))
print('La tua sequenza è: ')
for i in range(1, num+1):
    print(fibo(i))
precoMercadoria = float(input())
qtdMercadoria = int(input())

precoReal = precoMercadoria*qtdMercadoria
precoDesconto = precoReal*(0.9 - (qtdMercadoria*0.01))

print(f'{precoReal:.2f}')
print(f'{precoDesconto:.2f}')

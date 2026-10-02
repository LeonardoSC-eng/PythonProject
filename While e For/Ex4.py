total_economizado = 0
mes = 1

while mes<=3:
    valor = float(input(f"Valor a ser economizado no mês {mes}, R$: "))
    total_economizado = valor + total_economizado #Acumulador
    mes +=1 #Contador

print(f"Parabéns! Você economizou {total_economizado}")
#Contador normalmente é utilizado na condição do loop
#Contador incrementa valores por padrão +1. ou +2

#Acumulador pode ser utilizado na condição do loop
#Não soma valores padronizados
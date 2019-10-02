print ('='*60)
# imprimindo salario
salario = float(input('{}Digite o salario liquido: '.format(' '*5)))

print ('{}O salário liquido é:{} R$:{:8.2f}'.format (' '*5,' '*16, salario))
print ('{}Gastos E:{} R$:{:8.2f}'.format(' '*5,' '*27, salario * 0.5))
print ('{}Investimentos Longo prazo:{} R$: {:8.2f}'.format(' '*5,' '*10, salario * 0.2))
print ('{}Investimentos Curto prazo:{} R$:{:8.2f}'.format(' '*5, ' '*10,salario * 0.1))
print ('{}Livre:{} R$: {:8.2f}'.format(' '*5,' '*30, salario * 0.2))
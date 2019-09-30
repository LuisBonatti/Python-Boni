print ('-='*50)
frase = str(input('{0}Digite uma frase: '.format(' '*5 )))
letra = str(input('{0}Digite uma letra: '.format(' '*5 )))


print ('{0}A letra foi encontrada {1} vezes'.format (' '*5, frase.count(letra)))
print ('{0}A letra foi encontrada pela primeira vez {1}'.format(' '*5, frase.find(letra)+1))
print ('{0}A letra foi encontrada pela ultima vez {1}'.format(' '*5, frase.rfind(letra)+1))

print ('-='*50)
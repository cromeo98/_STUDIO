# 1 cosa vuol dire castare
# 2 quando eseguire un casting
# 3 funzioni int(), float(), str()

#1 castare significa cambiare il tipo di dato di una variabile o di un risultato

#2 viene fatto nel momento in cui dobbiamo eseguire operazioni o funzioni che coinvolgono variabili con tipo di dato diverso
# per i seguenti esempi, la variabile x è una stringa (lo vediamo perchè il valore è tra virgolette "") e la variabile y è un numero
# es. non posso concatenare un tipo stringa e un tipo int
# l'errore riportato sarà:
# TypeError: can only concatenate str (not "int") to str
x = "5"
y = 5
#print(x + y)
# es. non posso sommare un tipo int a un tipo stringa
# l'errore riportato sarà:
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
x = "5"
y = 5
#print(y + x)

# per ovviare a questi errori posso usare le funzioni str() (trasforma il tipo dato della variabile in stringa) 
# o
# int() (trasforma la variabile in int)
# es: trasformo y in string
# il risultato sarà 55 (difatti il "+" con le stringhe concatena i valori, quindi "5" e "5" = "55")
x = "5"
y = str(5)
print (x + y)
# es: trasformo x in int 
# il risultato sarà 10 (difatti il "+" con i tipi int va a sommare i valori quindi 5 + 5 = 10)
x = int("5")
y = 5
print (x + y)

# int(), str() e float() possono essere usate anche per convertire il valore di una variabile all'interno di un'altra varibile, oppure all'interno del print()
# es: uso la variabile z per trasformare in numero il valore contenuto all'interno di x
x = "5"
y = 5
z = int(x)
type(x)
type(z)
print(y + z)
# es: uso le funzioni direttamente all'interno del print()
print(int(x) + y)
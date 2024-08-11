# operatori aritmetici
# operatori di assegnamento
# precedenza operatori
# metodi: min, max, abs, pow

# gli operatori sono:
# +     #somma
# -     #sottrazione
# *     #moltiplicazione
# /     #divisione
# %     #modulo - mi da il resto di una divisione
# **    #elevamento a potenza
# //    #floor division - divisione arrotondata per difetto

# +     #somma
x = 10
y = 5
print(x + y)

# -     #sottrazione
x = 10
y = 5
print(x - y)

# *     #moltiplicazione
x = 10
y = 5
print(x * y)

# /     #divisione
x = 10
y = 7
print(x / y)

# %     #modulo - mi da il resto di una divisione
x = 10
y = 7
print(x % y)

# **    #elevamento a potenza
x = 10
y = 2
print(x ** y)

# //    #floor division - divisione arrotondata per difetto
x = 10
y = 7
print(x // y)


# operatori di assegnamento
# gli operatori di assegnamento mi servono nel momento in cui per ottenere il nuovo valore di una variabile devo eseguire un'operazione tra la variabile stessa e altro
#ad esempio, dichiarata la variabile x con valore 15, devo sommare il valore 2 al suo valore originale, di base il codice potrebbe essere:
x = 15
x = x + 2

# possiamo invece utilizzare gli operatori di assegnamento, che ci permettono di svolgere la medesima funzione
# sono (pongo semplicemente l'uguale a seguito dell'operatore aritmetico):
# +=     
# -=     
# *=     
# /=     
# %=     
# **=    
# //=    
x = 15
x += 2

#metodi min, max, abs (absolute), pow (potenza)
# min sta per minimo
x = min(5, 100, 1)
print(x)
# max sta per massimo
x = min(5, 100, 1)
print(x)
# abs sta per absolute (estraggo il valore assoluto di un numero)
x = abs(-5)
print(x)
# pow sta per potenza (elevamento a potenza)
x = pow(2, 2)
print(x)

# per svolgere operazioni matematiche più complesse, possiamo importare il moduli math
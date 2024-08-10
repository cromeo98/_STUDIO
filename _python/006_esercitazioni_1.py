# 1 creare variabile numero e assegnare il valore 5
# 2 creare una variabile nome ed assegnare il valore "Mario"
# 3 creare una varibile pi ed assegnare il valore 3.14
# 4 creare una variabile vero_falso ed assegnare il valore True
# 5 convertire il valore della variabile numero in una stringa ed assegnarlo alla varibile numero_stringa
# 6 convertire il valore della variabile pi in un intero ed assegnarla alla variabile pi_intero
# 7 convertire il valore della variabile vero_falso in una stringa e assegnarlo alla variabile vero_falso_stringa
# 8 dichiarare la variabile x con valore 10 e y con valore 20 e stamparne la somma
# 9 dichiarare la variabile z con valore "30" (stringa), convertirne il tipo dato in intero e stampre la somma di x, y e z
# 10 dichiarare la variabile stringa_1 con valore "hello"  e stringa_2 con valore "world"; concatenare i valori delle due variabili e assegnare il risultato alla variabile strings_concatenata e stamparne il valore
# 11 dichiarare la variabile variabile_bool con valore true e controllarne il tipo dato stampandolo a schermo
# 12 dichiarare la variabile lista con valori [1,2,3] e controllarne il tipo dato stampandolo a schermo

# 1 creare variabile numero e assegnare il valore 5
numero = 5
print(numero)
print(type(numero))

# 2 creare una variabile nome ed assegnare il valore "Mario"
nome = "Mario"
print(nome)
print(type(nome))

# 3 creare una varibile pi ed assegnare il valore 3.14
pi = 3.14
print(pi)
print(type(pi))

# 4 creare una variabile vero_falso ed assegnare il valore True
vero_falso = True
print(vero_falso)
print(type(vero_falso))

# 5 convertire il valore della variabile numero in una stringa ed assegnarlo alla varibile numero_stringa
numero_stringa = str(numero)
print(numero_stringa)
print(type(numero_stringa))

# 6 convertire il valore della variabile pi in un intero ed assegnarla alla variabile pi_intero
pi_intero = int(pi)
print(pi_intero)
print(type(pi_intero))

# 7 convertire il valore della variabile vero_falso in una stringa e assegnarlo alla variabile vero_falso_stringa
vero_falso_stringa = str(vero_falso)
print(vero_falso_stringa)
print(type(vero_falso_stringa))

# 8 dichiarare la variabile x con valore 10 e y con valore 20 e stamparne la somma
x = 10
y = 20
print(x + y)

# 9 dichiarare la variabile z con valore "30" (stringa), convertirne il tipo dato in intero e stampre la somma di x, y e z
z = int("30")
print(x + y + z)

# 10 dichiarare la variabile stringa_1 con valore "hello"  e stringa_2 con valore "world"; concatenare i valori delle due variabili e assegnare il risultato alla variabile strings_concatenata e stamparne il valore
stringa_1 = "hello"
stringa_2 = "world"
stringa_concatenata = stringa_1 + " " + stringa_2
print(stringa_concatenata)

# 11 dichiarare la variabile variabile_bool con valore true e controllarne il tipo dato stampandolo a schermo
# Posso confrontare il tipo di dato usando lo strumento di comparazione "==" per verificare che il tipo sia "bool"
variabile_bool = True
print(type(variabile_bool) == bool) #risultato è True (è vero che la variabile è di tipo bool)
print(type(variabile_bool) == int)  #risultato è False (è falso che la variabile è di tipo int)

# 12 dichiarare la variabile lista con valori [1,2,3] e controllarne il tipo dato stampandolo a schermo
lista = [1, 2, 3]
print(type(lista))
# Esercizio 1
# Stampare i numeri interi da 1 a 10 usando un loop while.
# n = 1
# while n <= 10:
#     print(n)
#     n += 1
# else:
#     print("Abbiamo stampato " + str(n - 1) + " numeri!")

# Esercizio 2
# Calcolare la somma dei primi n numeri interi positivi usando un loop while. L'utente deve inserire il valore di n.
# n = int(input("Inserisci un numero: "))
# sum = 0
# i = 0
# while i <= n:
#     sum += i
#     i += 1
#     if i > n:
#         string = "La somma dei primi {} numeri interi positivi è: {}"
#         print(string.format(n, sum))
#         #### oppure
#         print("La somma dei primi ", n, " numeri interi positivi è: ", sum)

# Esercizio 3
# Stampare i numeri pari da 2 a 10 usando un loop while.
# i = 0
# while i <= 10:
#     i += 1
#     if i % 2 != 0:
#         continue
#     print(i)

# Esercizio 4
# Chiedere all'utente di indovinare un numero intero casuale compreso tra 1 e 10. Continuare a chiedere all'utente di indovinare finché non indovina il numero corretto. Usare un loop while.
# import random
# rand_num = random.randint(1, 10)
# user_num = int(input("Scegli un numero tra 1 e 10: "))

# while user_num != rand_num:
#     print(rand_num, " ", user_num)
#     rand_num = random.randint(1, 10)
#     user_num = int(input("Sbagliato! Scegli un numero tra 1 e 10: "))
# else:
#     print("Hai indovinato!")

# Esercizio 5
# Chiedere all'utente di inserire una stringa. Stampare la stringa al contrario usando un loop while.
# user_string = input("Ciao! Inserisci una stringa di testo: ")
# i = len(user_string) - 1

# while i >= 0:
#     print(user_string[i], end="") #nel print, end ci permette di specificare come deve "terminare il print", così facendo il sistema stampa tutte le "i" contenute nel while, una di fianco all'altra
#     i -= 1

# Esercizio 6
# Stampare i numeri da 10 a 1 usando un loop while.
# i = 10
# while i > 0:
#     print(i, end=" ")
#     i -= 1

# Esercizio 7
# Calcolare il fattoriale di un numero intero positivo n usando un loop while.
# n = 5
# i = 1
# fact = 1

# while i <= n:
#     fact *= i
#     i += 1
#     if i > n:
#         print("Il fattoriale di ", n, " è: ", fact)

# Esercizio 8
# Chiedere all'utente di inserire una lista di numeri interi. Stampare la somma di tutti i numeri usando un loop while.
# list = []
# sum = 0
# num_request = int(input("Quanti numeri vuoi inserire? "))
# i = 1
# s = "Inserisci il {} numero: "
# while i <= num_request:
#     n = int(input(s.format(i)))
#     list.append(n)
#     i += 1
#     if i > num_request:
#         i = 0
#         break

# while i < len(list):
#     sum += list[i]
#     i += 1
#     if i == (len(list)):
#         print(sum)
#         break

# Esercizio 9
# Chiedere all'utente di inserire una stringa. Stampare solo le consonanti della stringa usando un loop while.
s = input("Inserisci una stringa di testo: ").lower()
cons = "bcdfghjklmnpqrstvwxyz" ### or vocals!!! e a quel punto anzichè usare in uso not in
i = 0

while i < len(s):
    l = s[i]
    i += 1
    if l in cons:
        print(l, end=" ")
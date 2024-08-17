# Esercizio 1
# Scrivere un programma che utilizzi un loop for per stampare ogni elemento di una lista.
# lst = ["ciao", "buongiorno", "buonasera", "buonanotte"]

# for greeting in lst:
#     print(greeting.capitalize())    #.capitalize() mi permette di rendere la prima lettera maiuscola

# Esercizio 2
# Scrivere un programma che utilizzi un loop for per stampare tutti i numeri da 1 a 10.
# for n in range(1,11):
#     print(n)
# else:
#     print("Fatto!")

# Esercizio 3
# Scrivere un programma che utilizzi un loop for per sommare tutti i numeri in una lista.
# lst_of_n = [1, 4, 6, 7, 2, 27]
# sum = 0
# for n in lst_of_n:
#     sum += n
# else:
#     print("Total sum is: ", sum)

# Esercizio 4
# Scrivere un programma che utilizzi un loop for per stampare tutti i numeri pari da 1 a 20.
# for n in range(1, 21):
#     if n % 2 == 0:
#         print(n)
# else:
#     print("Done!")

# Esercizio 5
# Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di una stringa.
# user_string = input("Welcome! Please, enter a string: ")

# for l in user_string:
#     print(l, end="")

# Esercizio 6
# Scrivere un programma che utilizzi un loop for per stampare tutte le chiavi di un dizionario.
# dict = {"name": "Christian", "surname": "Romeo", "age": "26"}
# for k in dict:
#     print(k)    #il for estrae solo le chiavi come elemento

# Esercizio 7
# Scrivere un programma che utilizzi un loop for per stampare tutte le coppie chiave-valore di un dizionario.
# dict = {"name": "Christian", "surname": "Romeo", "age": "26"}
# i = 1
# for k in dict:
#     print("Coppia chiave-valore n. " + str(i) + "= " + str(k) + ": " + dict[k])    #per estarre il valore devo inserire l'indice all'interno del dict
#     i += 1

# Esercizio 8
# Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di ogni stringa in una lista.
# s_lst = ["Armando", "Arianna", "Adele", "Azzurra"]
# for name in s_lst:
#     for l in name:
#         print(l)

# Esercizio 9
# Scrivere un programma che utilizzi un loop for per contare quante volte una lettera compare in una stringa.
# s = "Anche io sarei alto"
# c = 0
# for l in s:
#     if l.lower() == "a":
#         c +=1
# else:
#     print(c)

# Esercizio 10
# Scrivere un programma che utilizzi un loop for per calcolare la media di una lista di numeri.
# n_lst = [1, 50, 76, 39]
# count = 0
# sum = 0
# avg = 0
# for n in n_lst:
#     count += 1
#     sum += n
# else:
#     avg = sum / count
#     print("La media  è: " + str(avg))

#### Or
# for n in n_lst:
#         sum += n

# avg = sum / len(n_lst)
# print("La media è: ", avg)

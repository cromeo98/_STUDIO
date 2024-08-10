# 1 creare una stringa
# 2 mandare a schermo una stringa
# 3 stringhe multi riga - tripli apici
# 4 trattare stringhe come array (carattere, lunghezza, loop)

# 5 prendere parti di una stringa: str[:5]
# 6 modificare stringa con i metodi upper(), lower(), strip(), split(), replace()
# 7 concatenare stringhe
# 8 usare format per combinare stringhe e numeri
# 9 escape dei caratteri


# 1 creare una stringa
# posso usare sia gli apici singoli o i doppi apici
x = 'ciao'
y = "ciao tra doppi apici"
# 2 mandare a schermo una stringa
# usiamo sempre il print()
print(x)
# 3 stringhe multi riga - tripli apici
poesia = """
lorem 
ipsum
dolor
sit
"""
poesia_singoli_apici = '''
lorem 
ipsum
dolor
sit
'''
print(poesia)
print(poesia_singoli_apici)
# 4 trattare stringhe come array (carattere, lunghezza, loop)
# gli array di base non esistono in python, esistono con una libreria specifica
# gli array sono collezioni di valori (potremmo dire che assomigliano alle liste)
# le stringhe possono essere trattate come collezioni di caratteri, secondo le seguenti logiche
# - la stringa "ciao" contiene 4 caratteri, ognuno dei quali ha una posizione alla quale corrisponde un valore che parte da 0
# - esempio: il carattere "i", nella strinta "ciao" ha posizione 1
# posso estrarre un carattere da una stringa in base alla sua posizione (indice) con il seguente comando:
# - nome_variabile[posizione_da_estarre_come numero]
# es:
stringa = "ciao"
pos_0 = stringa[0]
pos_1 = stringa[1]
pos_2 = stringa[2]
pos_3 = stringa[3]
print(pos_1)
# ho la possibilità di contare quanto è "lunga la stringa" tramite la funzione len()
# es:
stringa = "ciao"
print(len(stringa))
# ho anche la possibilità di usare i loop sulle stringhe
# un loop può essere ad esempio il for
for i in stringa:
    print(i)

# 5 prendere parti di una stringa: str[:5]
# posso estrarre parti di una stringa
# per farlo posso eseguire il comando: nome_variabile[:posizione_da_estarre_come numero]
# i due punti vengono utilizzati per separare l'indice dal quale estrarre, all'indice fino al quale si desidera arrivare
# in questo esempio estrarremo "ciao" perchè estrarremo stringa[0:4]
stringa = "ciao sono python"
print(stringa[:4])
# in questo esempio estrarremo "sono" perchè estrarremo stringa[5:9], il che significa che partiremo dall'indice 5 e finiremo all'indice 9
stringa = "ciao sono python"
print(stringa[5:9])
print(stringa[:4])
# in questo esempio estrarremo "sono python" perchè estrarremo stringa[5:], il che significa che partiremo dall'indice 5 e finiremo alla fine della stringa
stringa = "ciao sono python"
print(stringa[5:])
# possiamo anche usare gli indici negativi, sia su singolo carattere (partiremo dal fondo) stringa[-1]
# che con un range stringa[-5:]
# esempio 1: parto dal fondo, e vado indietro di 6 indici (estraggo "python")
stringa = "ciao sono python"
print(stringa[-6:])
# esempio 2: parto dall'inizio, e rispetto al fondo sottraggo all'estrazione 6 indici (estraggo "ciao sono")
stringa = "ciao sono python"
print(stringa[:-6])

# 6 modificare stringa con i metodi upper(), lower(), strip(), split(), replace()
# .upper() rende tutta la stringa MAIUSCOLA
stringa = "ciao"
stringa_maiusc = stringa.upper()
print(stringa_maiusc)
# .lower() rende tutta la stringa minuscola
stringa = "CIAO"
stringa_minus = stringa.lower()
print(stringa_minus)
# .strip() rimuove gli spazi a inizio e fine stringa
stringa = "   ciao   "
stringa_stripped = stringa.strip()
print(stringa_stripped)
# .replace("stringa da sostituire", "stringa con cui sostituirla") sostituisce un carattere o un pezzo di stringa con un altro valore all'interno della stringa stessa
stringa = "ciao sono python"
stringa_replaced = stringa.replace("sono", "sei")
print(stringa_replaced)

# 7 concatenare stringhe
# significa unire due stringhe
stringa_1 = "ciao"
stringa_2 = " "
stringa_3 = "sono python"
stringa_concatenata = stringa_1 + stringa_2 + stringa_3
print(stringa_concatenata)
# ricordiamoci che per concatenare un numero ad una stringa devo necessariamente usare la funzione str()
stringa_1 = "Ho "
eta = 12
stringa_3 = " anni"
stringa_concatenata = stringa_1 + str(eta) + stringa_3
print(stringa_concatenata)
# 8 usare format per combinare stringhe e numeri
# oppure abbiamo il metodo .format()
# il format permette di concatenare numeri alle stringhe
# si utilizza con le parentesi graffe {} in una variabile per specificare dove dovrà essere aggiunto il numero
# in fase di printing o all'interno di un'altra variabile uso il metodo stringa.format(altra_variabile/valore, altra_variabile/valore)
stringa = "Ho {} anni, peso {} e sono alto {}"
eta = 12
stringa_concatenata = stringa.format(eta, 65, 1.72)
print(stringa_concatenata)
# all'interno delle graffe posso specificare quale dev'essere l'indice all'interno del metodo a cui fare riferimento
# nel seguente esempio, nel metodo inserisco i valori 65 (peso), eta (età), 1.72 (altezza)
# anche in questo caso gli indici partono da 0, quindi secondo l'ordine stabilito, il peso avrà indice 0, l'età 1 e l'altezza 2
stringa = "Ho {1} anni, peso {0} e sono alto {2}"
eta = 12
stringa_concatenata = stringa.format(65, eta, 1.72)
print(stringa_concatenata)

# 9 escape dei caratteri
# l'escape è lo strumento che ci permette di inserire le virgolette o gli apostrofi all'interno delle stringhe
# nella documentazione di python esistono altri escape
# bisogna usare il carattere speciale backslash "\"
stringa = "ciao sono \"bello e ho 26 anni, inoltre cerco l\'amore"
print(stringa)

# bonus metodo .split()
# il metodo split permette di creare una lista di stringhe da una singola stringa
# se all'interno delle parentesi non viene inserito nulla, la stringa verrà splittata in base agli " "
stringa = "ciao sono christian"
lista_stringa_splitted = stringa.split()
print(lista_stringa_splitted)
# in alternativa possiamo inserire un carattere per il quale eseguire lo split (vengono estratti i valori dalla posizione successiva al carattere trovato fino alla posizione successiva in cui viene ritrovato)
stringa = "Aciao Asono Achristian"
lista_stringa_splitted = stringa.split("A")
print(lista_stringa_splitted)
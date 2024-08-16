# cosa sono i cicli (loop)
# sintassi del while
# break, continue ed esle

# i cicli servono per eseguire gli script contenuti al loro interno fintanto che una condizione è considerata vera
# possono essere utilizzati con un contatore che aumenta ad ogni "giro" del ciclo

i = 0   #è il nostro contatore
while i <= 5:
    print(i)
    i += 1 #aumento di 1 il contatore ad ogni giro

# break, serve ad interrompere il ciclo
# può essere utilizzato con un if per definire qual è la condizione per la quale interrompere il ciclo
i = 0
while i <= 5:
    print(i)
    if i == 3:
        print(str(i) + " è il numero corrispondente alla condizione in un cui eseguire il break, quindi sarà l\'ultimo numero che stampiamo")
        break
    i += 1

# continue permette di tornare alla prima riga contenuta all'interno del ciclo while, ignorando tutto ciò che è stato scritto dopo il continue
i = 0
while i <= 5:
    i += 1
    if i == 3:
        print(str(i) + " viene stampato con questo altro messaggio e non con quello precedente perchè è all'interno del continue!")
        continue
    print(str(i) + " viene stampato con questo messaggio perchè al di fuori del continue")

# else invece ci permette di inserire l'alternativa da eseguire nel caso in cui il ciclo è terminato o la condizione non è rispettata
i = 1
while i == 0:
    print("qui")
else:
    print("fine")
# cosa sono i moduli?
# come si creano?
# funzioni e variabili nei moduli
# alias
# moduli built in
# funzione dir
# importare le parti di moduli

# sostanzialmente un modulo è una libreria, un file esterno contenente funzioni e/o variabili che possiamo importare nel nostro script per sfruttarne le funzioni

# nel file modulo_saluti creo una funzione saluta che ha un requisito "nome" ed esegue il print della parola "ciao" + nome. in questo file 027a_ andiamo ad importare il modulo e ad eseguire la funzione saluta, nonostante questa non sia definita all'interno dello script del file 027a_

# in questo file andremo ad importare ed eseguire la funzione creata nel modulo modulo_saluti; per farlo,dobbiamo fare come segue:
import modulo_saluti
modulo_saluti.saluta("Christian")
 
# possiamo anche creare delle variabili all'interno dei moduli (esempio: creiamo un dict persona) e assegnarle alle variabili presenti in questo script
x = modulo_saluti.persona

# e concatenare funzioni e variabili
modulo_saluti.saluta(x["nome"])

# alias: tendenzialmente per i moduli il nome ha 2, massimo 3 lettere, in quanto un ampio utilizzo di un modulo ci costringerebbe a ripetere ogni volta che il modulo viene richiamato tutto il nome
# l'alias ci viene in soccorso perchè ci permette di rinominare all'interno del nostro script il modulo, così da poterlo richiamare più rapidamente
# in questo esempio andremo a dare al modulo_saluti l'alias "ms"
import modulo_saluti as ms

# da ora in avanti, per sfruttare le funzioni e variabili del modulo, ci basterà richiamarlo usando la dicitura ms
ms.saluta("Paolo")

# conseguentemente, "modulo_saluti" non sarà più utilizzabile

# in python esistono già tanti moduli molto utili, chiamati moduli built in, ad esempio math, che ci permette di eseguire operazioni matematiche particolari
# la modalità di import non cambia
import math as ma

print(ma.floor(1.6549465465))

# la funzione dir() ci permette di visualizzare tutte le funzioni costruite all'interno di un modulo
print(dir(ms))
# risultato: 
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'persona', 'saluta']
print(dir(ma))

# possiamo importare solamente alcune parti del modulo, in sostanza dicendo: dal modulo importa la funzione/variabile/classe
from modulo_saluti import saluta

# per eseguire la funzione, non c'è bisogno di richiamare il modulo
saluta("jhonny")
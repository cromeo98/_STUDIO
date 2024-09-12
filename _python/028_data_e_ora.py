# modulo datetime
# creazione di un oggetto con data .now() e data predefinita
# metodo strftime - utile per la formattazione
# parametri formattazione date
    # %a	|   Giorno della settimana abbreviato			            |   Mon
    # %A	|   Giorno della settimana completo				            |   Monday
    # %w	|   Giorno della settimana come numero 			            |   (0=Dom, 6=Sab)	0 (per Domenica)
    # %d	|   Giorno del mese (2 cifre, con zero iniziale)	        |   01
    # %b	|   Nome abbreviato del mese				                |   Jan
    # %B	|   Nome completo del mese					                |   January
    # %m	|   Mese come numero (01-12)				                |   01 (per Gennaio)
    # %y	|   Anno senza secolo (2 cifre)				                |   23 (per 2023)
    # %Y	|   Anno completo (4 cifre)					                |   2023
    # %H	|   Ora in formato 24h (00-23)				                |   14
    # %I	|   Ora in formato 12h (01-12)				                |   02
    # %p	|   AM/PM							                        |   PM
    # %M	|   Minuti (00-59)						                    |   45
    # %S	|   Secondi (00-59)						                    |   30
    # %f	|   Microsecondi (000000-999999)				            |   123456
    # %j	|   Giorno dell'anno (001-366)				                |   001
    # %U	|   Numero della settimana (domenica come primo giorno)     |   52
    # %W	|   Numero della settimana (lunedì come primo giorno)       |   01
    # %c	|   Rappresentazione locale di data e ora			        |   Mon Jan 1 14:30:00 2023
    # %x	|   Rappresentazione locale della data			            |   01/01/23
    # %X	|   Rappresentazione locale dell'ora			            |   14:30:00
    # %Z	|   Fuso orario						                        |   CST
    # %z	|   Offset dal fuso orario UTC				                |   +0100
    # %T	|   Ora in formato 24h 					                    |   (HH:MM)	14:30:00
    # %D	|   Data in formato MM/DD/YY				                |   01/01/23
    # %F	|   Data in formato completo (YYYY-MM-DD)			        |   2023-01-01
    # %R	|   Ora in formato 24h senza secondi 			            |   (HH) 14:30
    # %r	|   Ora in formato 12h con secondi e AM/PM			        |   02:30:00 PM

# in python non esiste il tipo di dato "data" o "ora"
# pertanto per poter lavorare su questa tipologia di dato, possiamo sfruttare il modulo datetime, che andiamo ad importare
import datetime as dt
print(dir(dt.datetime))

# datetime è un modulo che contiene classi(e di conseguenza metodi) e funzioni
# ad esempio vogliamo attribuire alla nostra variabile x il datetime attuale
# dichiariamo x, che corrisponderà al metodo .now() della classe datetime appartenete al modulo datetime (dt nel nostro caso in quanto gli abbiamo dato un alias)
x = dt.datetime.now()

print(x)

# con il metodo strftime, possiamo formattare con i parametri sopra indicati le nostre date
print(x.strftime("%D"))

# possiamo anche concatenare diversi parametri (esempio, giorno della settimana, giorno, mese, anno)
print(x.strftime("%A - %F"))
# cosa sono i valori booleani
# comparazioni ed if
# valutare i valori delle variabili

# cosa sono?
# in breve sono i valori che esprimono la condizione Vero o Falso
# posso sfruttarli nelle condizioni
# anche in un print posso ottenere come output un valore booleano, ad esempio:
print(5 < 10) # è vera o falsa questa condizione?
# il risultato sarà True

# i valori possono anche essere assegnati alle varibili, ad esempio:
t = True
f = False

# È fondamentale comprendere i valori booleani, in quanto sono ciò che in programmazione ci permette di usare gli if e i cicli
# ad esempio, mettiamo caso che nel caso in cui una variabile fosse maggiore di un determinato valore volessimo stampare una determinata stringa
# grazie ai valori booleani possiamo farlo
x = 100

if x > 99: #condizione che riporterà il valore True oppure False
    print(str(x) + ' è maggiore di 99') #questa sezione viene eseguita se la condizione è vera
else:
    print(str(x) + ' non è maggiore di 99') #questa sezione viene eseguita se la condizione è falsa

# possiamo sfruttare i valori booleani anche per valutare i valori delle variabili
# N.B. esistono valori delle variabili che restituiranno sempre la condizione False, e sono
# bool(False)   - booleano
# bool(None)    - vuota
# bool(0)       - numero
# bool("")      - str
# bool(())      - tupla
# bool([])      - lista
# bool({})      - set
# viene da sè che possiamo sfruttare la funzione bool() per comprendere se una determinata variabile è vuota oppure no, indipendentemente dalla tipologia di dato

# esempio pratico
# abbiamo una variabile "warehouse" che contiene la quantità di prodotti stoccati nel magazzino, se i prodotti scendono a 0 (False), bisogna contattare l'ufficio vendite
warehouse = 0
if warehouse: #se 0 sarà False, se > 0 True
    print("Magazzino pieno")
else:
    print("Contattare l'ufficio acquisti")

# esempio pratico 2
# ho una lista della spesa, se è vuota non devo andare al supermercato, altrimenti sì
lista_della_spesa = ["pane", "uova", "pasta"]
if lista_della_spesa: #se la lista non contiene valori sarà False, se al contrario li conterrà sarà True
    print("Andare a fare la spesa")
else:
    print("Non serve andare al supermercato")
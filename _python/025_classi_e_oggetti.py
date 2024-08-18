# cos'è la programmazione ad oggetti
# la programmazione ad oggetti consiste nel gestire delle classi, che sono una specie di insieme di informazioni e/o azioni che possono essere svolte da tutti gli oggetti che fanno parte di quella determinata classe.
# è fondamentale il concetto di ereditarietà: ogni classe può avere una classe padre, dalla quale erediterà tutte le proprietà e le funzioni in essa contenuta
# la differenza tra classe e oggetto deriva dal fatto che un oggetto viene costruito in base ad una classe richiamandola

# in questo esempio, creiamo una classe Videogame, che come propietà ha il nome e il produttore
# il metodo self, significa che le due proprietà fanno riferimento alla classe stessa, e verranno utuilizzate quindi esclusivamente per l'oggetto creato dalla classe
class Videogame:
    def __init__(self, name, producer): #questo si chiama costruttore, permetterà di costruire gli oggetti
        self.name = name                #self specifica il riferimento a sè stesso, permette agli oggetti di avere sempre il proprio riferimento
        self.producer = producer
# creiamo ora all'interno della classe la funzione "stampa_proprieta"
    def stampa_proprieta(self):
        print("Le proprietà del gioco sono: " + self.name + " e " + self.producer)

# creiamo ora l'oggetto gioco_1
# un oggetto è un'istanza della classe (nel senso che deriva dalla classe Videogame)
gioco_1 = Videogame("the last of us", "naughty dog")
# per eseguire la funzione dichiarata all'interno del videogame basta eseguirla come metodo
gioco_1.stampa_proprieta()

# parlando di ereditarietà, creiamo una nuova classe, figlia di videogame, ad esempio Videogame_pc, che ha sia le proprietà di classe, che le proprietà di un gioco pc, ovvero possiamo avere la proprietà "requisiti_grafici" e "requisiti_ram"
class Videogame_pc(Videogame):
    def __init__(self, name, producer, requisiti_grafici, requisiti_ram):
        super().__init__(name, producer)    # super() mi permette di ereditare dalla classe padre le proprietà e le modalità con cui sono definite
        self.requisiti_grafici = requisiti_grafici
        self.requisiti_ram = requisiti_ram
    def stampa_proprieta(self):
        print("Le proprietà del gioco sono: ", self.name, self.producer, self.requisiti_grafici, self.requisiti_ram)

gioco_2 = Videogame_pc("Minecraft", "ND", "Alti", "16gb")
gioco_2.stampa_proprieta()

# in una classe figlia posso eseguire l'overriding delle proprietà, riscrivendo l'init
class Videogame_pc(Videogame):
    def __init__(self, name, producer, requisiti_grafici, requisiti_ram):
        self.name = "Overridden name"
        self.producer = "Overridden producer"
        self.requisiti_grafici = requisiti_grafici
        self.requisiti_ram = requisiti_ram
    def stampa_proprieta(self):
        print("Le proprietà del gioco sono: ", self.name, self.producer, self.requisiti_grafici, self.requisiti_ram)

gioco_3 = Videogame_pc("Minecraft", "ND", "Alti", "16gb")
gioco_3.stampa_proprieta()
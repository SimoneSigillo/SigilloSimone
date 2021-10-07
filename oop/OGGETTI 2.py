class Studente:
    #attributi della Classe
    studenti= 0
    ragazzi= 0
    ragazze= 0

    #metodo costruttore
    def __init__(self, nome, cognome, genere, eta, classe):

        #attributi di istanza
        
        self.nome = nome
        self.cognome = cognome
        self.genere = genere
        self.eta = eta
        self.classe = classe
        Studente.studenti += 1
        if self.genere == "ragazzo":
            Studente.ragazzi += 1
        else:
            Classe.ragazze +=1

        
                
                
            


                #metodo get
        def scheda(self):
            return f"Scheda:\nNome: " + {self.nome} + "\nCognome: " + {self.cognome} + "\nGenere: " + {self.genere} + "\nEta: " + {self.eta} + "\nClasse: " + {self.classe}
        

        def studenti_totali():
            return str("\nNumero totale di studenti: " + str(Studente.studenti) + "\nNumero ragazzi: " + str(Studente.ragazzi) + "\nNumero ragazze: " + str(Studente.ragazze))
        
            
                   
                
            

            #metodo set
            def set_eta(self, eta):
                self.eta = eta
            
                
                    
                    

                #costruzione oggetti
                
                Simone = Studente ("Simone","Sigillo","ragazzo",17,"quartaE")
                Luca = Studente("Luca","Petrazzuolo","ragazzo",18,"quintaE")
               

                print("il tipo di variabile costruita è: ")
                print(Simone)
                print(Luca)

               #utilizzo metodo get

                print("la singola scheda è: ")
                print (Simone.scheda())
                print (Luca.scheda())

                print(Studente.studenti_totali())
             
             

                #utilizzo metodo set
                Simone.set_eta(17)
                print(Simone.scheda())

                #altro metodo per visualizzare le informazioni, (__dict__)
                #print()
                #print(Simone.__dict__)
                #print(Luca.__dict__)
                
                

                
               

                

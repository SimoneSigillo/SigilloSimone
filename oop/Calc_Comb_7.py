from itertools import permutations

class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)
        self.__anagrammi = anagrammi(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self, stringa):
        self.__stringa = stringa
        self.__N = len(stringa)
        self.__listStringa = list(stringa)
        self.__anagrammi = anagrammi(stringa)

    def charRipetuti(self): #caratteri ripetuti
        carattere = {}
        nCaratteri = 0
        count = 0
        for i in self.__listStringa:
            if (i in carattere):  
                carattere[str(i)] += 1
            else:
                carattere[str(i)] = 1 
        for i in carattere:
            if carattere[i]>1: 
                count += 1 
                nCaratteri += carattere[i] 

        variabiliAnagrammi = [count, nCaratteri, carattere]

        return variabiliAnagrammi
    

    def cerca_parola(self):  #cerca la parola nel file di parole italiane
        f = open("word.italian.txt", 'r')
        riga = f.readline()
        stringapresente == False
        for riga in f:
            if self.__stringa == riga[:-1]:
                stringapresente == True
        f.close()

        return stringapresente


    def fattoriale(n):
        if n==0:
            return 1
        else:
            return n * fattoriale(n-1)
            
        
        
        
    

    def coeffBinom(n, k):
        if k == n:
            return 1
        elif k == 1:         
            return n
        elif k > n:          
            return 0
        else:
            return calcComb.fattoriale(n) // (calcComb.fattoriale(k) * calcComb.fattoriale(n-k))
            
    def anagrammi(self):  #generiamo tutte le possibili permutazioni inserendo quest'ultimi in una lista
        lettere = list(parola)

        permutazioni = list(permutations(lettere))

        temp = ''

        anagrammi = []

        for i in permutazioni:

            for carattere in i:
                temp += carattere

            anagrammi.append(temp)

            temp = ''
        

    def confUtil(self): # dopo aver cercato le parole nel file, mette in evidenza solo le parole che rispettano la lingua italiana
        anagrammiGiusti = []
        for i in self.__anagrammi:
            calcComb.cerca_parola(i)
            if stringapresente == True:
                anagrammiGiusti.append(i)

        return anagrammiGiusti
                
            

        


    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        PermutSenzaRip = calcComb.fattoriale(self.__N)

        return PermutSenzaRip

    def nPermutConRip(self):
        PermutConRip = calcComb.fattoriale(self.__N) / calcComb.charRipetuti(self)

        return PermutConRip

    def permutSenzaRip(self):
        
        return calcComb.anagrammi(self)

    def permutConRip(self):
       
        return 0

    # DISPOSIZIONI

    def nDispSemplSenzaRip(self, k):
        if self.__N >= k:
            DispSemplSenzaRip = calcComb.fattoriale(self.__N) / calcComb.fattoriale(self.__N-k)

        return DispSemplSenzaRip

    def nDispSemplConRip(self, k):
        DispSemplConRip = self.__N**k

        return DispSemplConRip

    def dispSemplSenzaRip(self, k):
        listaDisposizioni = list(itertools.permutations(self.__stringa, k))
        temp = ''
        disposizioni = []
        for i in listaDisposizioni:
            for carattere in i:
                temp += carattere
            disposizoni.append(temp)
            temp = ''
        
        return disposizioni

    def dispSemplConRip(self):
        
        return 0

    # COMBINAZIONI

    def nCombSemplSenzaRip(self, k):
        CombSemplSenzaRip = calcComb.fattoriale(self.__N) / (calcComb.fattoriale(k) * calcComb.fattoriale(self.__N-k))

        return CombSemplSenzaRip

    def nCombSemplConRip(self, k):
        CombSemplConRip = calcComb.coeffBinom(self.__N+k-1, k)

        return CombSemplConRip

    def combSenzaRip(self, k):
        listaCombinazioni = list(itertools.combinations(self.__stringa, k))
        temp = ''
        combinazioni = []
        for i in listaCombinazioni:
            for carattere in i:
                temp += carattere
            combinazioni.append(temp)
            temp = ''
        
        return combinazioni


    def combConRip(self):
        listaCombinazioni = list(itertools.combinations_with_replacement(self.__stringa, k))
        temp = ''
        combinazioni = []
        for i in listaCombinazioni:
            for carattere in i:
                temp += carattere
            combinazioni.append(temp)
            temp = ''
        
        return combinazioni

    # PROBABILITA'

    def probConfUtil(self):  #otteniamo il numero di casi favorevoli attraverso il metodo "confutil" dividendo in seguito per il numero totale di anagrammi, attraverso il len della tupla degli anagrammi.
        casiFavorevoli = 0
        for i in self.__anagrammi: 
            Vtemp = calcComb.confUtil(i)
            if Vtemp == False:
                None
            elif Vtemp == True:
                casiFavorevoli += 1
        
        probabilità = casifav/(len(self.__anagrammi))

        return probabilità

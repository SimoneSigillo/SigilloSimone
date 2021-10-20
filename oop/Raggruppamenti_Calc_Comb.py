from itertools import permutations, combinations, combinations_with_replacement


#PERMUTAZIONI
permutazioni=permutations(["A","B","C"])
#print(list(permutazioni))

#DISPOSIZIONI CON RIPETIZIONE ?



#DISPOSIZIONI
disposizioni=permutations(["A","B","C","D","E"],2)   #numeri dentro le quadre indicano il nostro n, il numero fuori le quadre indica il k
#print(list(disposizioni))

#COMBINAZIONI

combinazioni=combinations(["U","R","Y","I"],2)
print(list(combinazioni))

#COMBINAZIONI CON RIPETIZIONI

combinazioniconripetizione =(combinations_with_replacement("ABCD", 2))
#print(list(combinazioniconripetizione))



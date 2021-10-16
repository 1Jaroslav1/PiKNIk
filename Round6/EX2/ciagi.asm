SIZE DC INTEGER(10)
TAB DC 10*INTEGER()
MEM_STEP DC INTEGER(4)
# Zerujemy registry 1 i 6
 SR 1,1
 SR 10,10
# Do registru 2 przypisujemy rozmiar tablicy w bitach
 L 2,SIZE
 M 2,MEM_STEP
# Pomniejszamy rozmiar tablicy, ponieważ numeracja elementow
# w tablicy zaczyna sie od zera
 S 2,MEM_STEP
#Do registru 4 musimy zapisac pierwszy element tablicy,
#gdyz wymaga tego logika petli
 L 4,TAB(1)
 J LOOP_END
#poprzedni element zapisujemy do registru 3, biezacy do registru 4
LOOP_START LR 3,4
 A 1,MEM_STEP
 L 4,TAB(1)
#Jezeli biezacy element jest mniejszy od poprzedniego - zerujemy je w tablicy,
#Ale zostaja one w registrach
 CR 3,4
 JZ LOOP_END
 JN LOOP_END
 ST 10,TAB(1)
 S 1, MEM_STEP
 ST 10,TAB(1)
 A 1,MEM_STEP
LOOP_END CR 1,2
 JN LOOP_START
#Ostatnie polecenie potrzebne zeby wyjsc z petli
#(Inaczej interpretator traktuje petle jako nieskonczona)
 A 1,MEM_STEP
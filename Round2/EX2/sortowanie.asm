TAB DC 5*INTEGER
SIZE DC INTEGER(5)
STEP DC INTEGER(1)
VAR_SIZE DC INTEGER(4)
ZERO DC INTEGER(0)
ONE DC INTEGER(1)
#Zakres wewnetrznej petli
 L 1, SIZE
 S 1, ONE
#Zerowanie iteratora
LOOP_START L 2, ZERO
#Obliczanie potocznego adresu
IN LR 10, 2
 M 10, VAR_SIZE
#Comparing current element with next
 L 3, 0(10)
 C 3, 4(10)
 JP SWAP
 J NEXT_STEP_IN
#Zamiana elementow
SWAP L 4, 4(10)
 ST 4, 0(10)
 ST 3, 4(10)
#Zwiekszeniei teratora o zdefiniowany krok
NEXT_STEP_IN A 2, STEP
 CR 2, 1
 JN IN
#Zmniejszenie iteratora petli zewnetrznej
NEXT_STEP_OUT S 1, STEP
 C 1, ZERO
 JP LOOP_START
#Koniec (Jezeli iterator jest zerem)
END S 1,TAB(1)
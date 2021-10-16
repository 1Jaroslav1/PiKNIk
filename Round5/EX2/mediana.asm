LENGTH DC INTEGER(7)
INT DC 7*INTEGER()
TWO DC INTEGER(2)
ONE DC INTEGER(1)
MEM_STEP DC INTEGER(4)
WYNIK DC INTEGER(0)
TAB DS INTEGER
#Przypisujemy zmiennej TAB adres tablicy (jej pierwszego elementu)
 LA 1,INT
 ST 1,TAB
#Ładujemy długgosc tablicy do registrow 2 i 3
 L 2,LENGTH
 L 3,LENGTH
#Sprawdzamy czy liczba elementow jest wieksza od zera
 SR 1,1
 CR 2,1
 JZ WYNIK_ZERO
 JN WYNIK_ZERO
#Jezeli tablica zawiera mniej niz 2 elementy
#Pomijamy operacje modulo
 C 2,TWO
 JN NIEPARZYSTA
#Liczymy LENGTH mod 2
START_MOD S 2,TWO
 C 2,TWO
 JZ START_MOD
 JP START_MOD
#Sprawdzamy czy liczba elementow jest parzysta
END_MOD C 2,ONE
 JZ NIEPARZYSTA
#Liczymy mediane dla parzystej liczby elementow
 D 3,TWO
 M 3,MEM_STEP
 S 3,MEM_STEP
 J END_LOOP_P
START_LOOP_P A 1,MEM_STEP
END_LOOP_P CR 1,3
 JN START_LOOP_P
 L 2,INT(1)
 A 1,MEM_STEP
 A 2,INT(1)
 D 2,TWO
 ST 2,WYNIK
 J WYNIK_ZERO
NIEPARZYSTA D 3,TWO
 M 3,MEM_STEP
 S 3,MEM_STEP
 J END_LOOP_N
START_LOOP_N A 1,MEM_STEP
END_LOOP_N CR 1,3
 JN START_LOOP_N
 L 2,INT(1)
 ST 2,WYNIK
WYNIK_ZERO L 15,WYNIK
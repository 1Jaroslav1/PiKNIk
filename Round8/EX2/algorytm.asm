X1 DC INTEGER(1)
Y1 DC INTEGER(1)
X2 DC INTEGER(5)
Y2 DC INTEGER(4)
ONE DC INTEGER(1)
TWO DC INTEGER(2)
# Zapisujemy wartości do registrow
 L 1,X1
 L 2,Y1
 L 3,X2
 L 4,Y2
# Register 5 - dx
# Register 6 - dy
# Register 7 - e
# Register 8 - 1
# Register 9 - 2
# Regiser 10 - zero
# Register 11 - dx/2
# Register 14 - wspolrzedna x piksela docelowego
# Register 15 - wspolrzedna y piksela docelowego
 LR 5,3
 SR 5,1
 LR 6,4
 SR 6,2
 LR 7,5
 D 7,TWO
 L 8,ONE
 SR 10,10
 LR 11,5
 D 11,TWO
 AR 11,1
 LR 14,1
 LR 15,2
START_LOOP AR 14,8
 SR 7,6
 CR 7,10
 JZ END_ITER
 JP END_ITER
 AR 15,8
 AR 7,5
END_ITER CR 14,11
 JN START_LOOP
 CR 14,15
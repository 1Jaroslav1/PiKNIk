ODC_1 DC INTEGER(16)
ODC_2 DC INTEGER(14)
ODC_3 DC INTEGER(2)
#Finding max
 L 1,ODC_1
 L 2,ODC_2
START_IF_MAX CR 1,2
 JZ LESS_IN
 JN LESS_IN
 JP MORE_IN
LESS_IN L 3,ODC_3
 CR 2,3
 JZ SWITCH
 JN SWITCH
 JP END_IF_MAX
MORE_IN LR 3,1
 LR 1,2
 LR 2,3
 L 3,ODC_3
 CR 2,3
 JZ END_IF_MAX
 JN END_IF_MAX
 JP SWITCH
SWITCH LR 4,2
 LR 2,3
 LR 3,4
 J END_IF_MAX
#Compute sum
END_IF_MAX AR 1,2
#Compare the sum to Maximum
START_IF CR 1,3
#Jumping to label
 JZ ZERO
 JN ZERO
 JP JEDEN
#Labels
ZERO SR 1,1
WYNIK DC INTEGER(0)
 J END_IF
JEDEN SR 1,1
WYNIK DC INTEGER(1)
 J END_IF
END_IF L 1,WYNIK
#Zeby wyjsc z instrukcji warunkowej w ostatniej linijce program przypisuje wartosc zmiennej WYNIK do registru 1
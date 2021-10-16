DNI = ('poniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota', 'niedziela')

data = input('Podal dzien i liczbe: ').split(' ')

shift = (DNI.index(data[0]) + int(data[1])) % 7

print(DNI[shift])
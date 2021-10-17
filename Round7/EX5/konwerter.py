def to_si(value, code):
    if code == 1:
        return value * 1000
    elif code == 2:
        return value * 10
    elif code == 3:
        return value
    elif code == 4:
        return value / 1000
    elif code == 5:
        return value * 10 ** 5
    elif code == 6:
        return value * 10 ** 6
    elif code == 7:
        return value * 0.06479891
    elif code == 8:
        return value * 28.34952981
    elif code == 9:
        return value * 453.59237

def from_si(value, code):
    if code == 1:
        return value / 1000
    elif code == 2:
        return value / 10
    elif code == 3:
        return value
    elif code == 4:
        return value * 1000
    elif code == 5:
        return value / 10 ** 5
    elif code == 6:
        return value / 10 ** 6
    elif code == 7:
        return value / 0.06479891
    elif code == 8:
        return value / 28.34952981
    elif code == 9:
        return value / 453.59237

def main():
    MENU = """------JEDNOSTKI-------
1. Kilogram [kg]
2. Dekagram [deg]
3. Gram [g]
4. Miligram [mg]
5. Kwitnal [q]
6. Tona [t]
7. Gran [gr]
8. Uncja [oz]
9. Funt[lb]"""
    print(MENU)
    code = int(input('Podaj numer jednostki z ktorej konwertujemy: '))
    value = float(input('Podaj ilosc: '))
    value = to_si(value, code)
    code = int(input('Podaj numer jednostki na ktora konwertujemy: '))
    print(from_si(value, code))

if __name__ == '__main__':
    main()


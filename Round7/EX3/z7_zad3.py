def pal_check(str):
    length = len(str)

    for i in range(int(length / 2)):
        if str[i] != str[length - i - 1]: return False

    return True

if __name__ =='__main__':
    print(pal_check(input()))

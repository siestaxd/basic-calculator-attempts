import os

def screen_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def topla(x,y):
    return x + y
def cikar(x,y):
    return x - y
def carp(x,y):
    return x * y
def bol(x,y):
    return x / y

while True:
    islem = input('[1] - Toplama\n[2] - Çıkarma\n[3] - Çarpma\n[4] - Bölme\n[0] - İptal\nİşlem seçiniz: ')
    if islem == '1':
        screen_clear()
        x = float(input('1.sayı: '))
        y = float(input('2.sayı: '))
        screen_clear()
        print(f'{x} + {y} = {topla(x,y)}')
        print('\n'*3)
    elif islem == '2':
        screen_clear()
        x = float(input('1.sayı: '))
        y = float(input('2.sayı: '))
        screen_clear()
        print(f'{x} - {y} = {cikar(x,y)}')
        print('\n'*3)
    elif islem == '3':
        screen_clear()
        x = float(input('1.sayı: '))
        y = float(input('2.sayı: '))
        screen_clear()
        print(f'{x} * {y} = {carp(x,y)}')
        print('\n'*3)
    elif islem == '4':
        screen_clear()
        x = float(input('1.sayı: '))
        y = float(input('2.sayı: '))
        if y == 0:
            screen_clear()
            print("bir sayı 0'a bölünemez")
            print('\n'*3)
        else:
            screen_clear()
            print(f'{x} / {y} = {bol(x,y)}')
            print('\n'*3)
    elif islem == '0':
        break
    else:
        print('Geçersiz işlem seçtiniz')
        print('\n'*3)
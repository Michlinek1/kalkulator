import time
import math
def Dodawanie(x,y):
    return x+y

def Odejmowanie(x,y):
    return x-y

def Mnożenie(x,y):
    return x*y

def Dzielenie(x,y):
    return x/y

def Potęga(x,y):
    return x**y

def Modulo(x,y):
    return x%y

def Logatytmy(x,y):
    return math.log(x,y)

def Main():
    Pytanie = str(input(
'''Jakie chcesz zrobić działanie?
Dodawanie
Odejmowanie
Mnożenie
Dzielenie
Potęga
Modulo
Logatytmy
''' + "\n"))


    match Pytanie:
        case "Dodawanie" | "dodawanie":
            liczb1 = float(input(colored("Wpisz pierwszą liczbę", 'red') + "\n"))
            liczb2 = float(input(colored("Wpisz drugą liczbę", 'red') + "\n"))
            wynik = Dodawanie(liczb1, liczb2)
            zaaokraglenie = round(wynik)
            print(f"Wynik to:{wynik} co w zaaokragleniu daje {zaaokraglenie}")
            time.sleep(2)
            Main()
        case "Odejmowanie" | "odejmowanie":
            liczb1 = float(input("Wpisz pierwszą liczbę") + "\n"))
            liczb2 = float(input("Wpisz drugą liczbę"') + "\n"))
            wynik = Odejmowanie( liczb1, liczb2)
            zaaokraglenie = round(wynik)
            print(f"Wynik to:{wynik} co w zaaokragleniu daje {zaaokraglenie}")
            time.sleep(2)
            Main()
    
        case "Mnożenie" | "mnożenie":
            liczb1 = float(input("Wpisz pierwszą liczbę"') + "\n"))
            liczb2 = float(input("Wpisz drugą liczbę") + "\n"))
            wynik = Mnożenie(liczb1, liczb2)
            zaaokraglenie = round(wynik)
            print(f"Wynik to:{wynik} co w zaaokragleniu daje {zaaokraglenie}")
            time.sleep(2)
            Main()
            
        case "Dzielenie" | "dzielenie":
            liczb1 = float(input("Wpisz pierwszą liczbę") + "\n"))
            liczb2 = float(input("Wpisz drugą liczbę") + "\n"))
            wynik = Dzielenie(liczb1, liczb2)
            zaaokraglenie = round(wynik)
            print(f"Wynik to:{wynik} co w zaaokragleniu daje {zaaokraglenie}")
            time.sleep(2)
            Main()
        case "Potęga" | "potęga":
            liczb1 = float(input("Wpisz podstawę potęgi" + "\n"))
            liczb2 = float(input("Wpisz wykładnik potęgi") + "\n"))
            wynik = Potęga(liczb1,liczb2)
            zaaokraglenie = round(wynik)
            print(f"Wynik to:{wynik} co w zaaokragleniu daje {zaaokraglenie}")
            time.sleep(2)
            Main()
            
        case "Modulo" | "modulo":
            liczb1 = float(input("Wpisz pierwszą liczbę") + "\n"))
            liczb2 = float(input("Wpisz drugą liczbę") + "\n"))
            wynik = Modulo(liczb1,liczb2)
            zaaokraglenie = round(wynik)
            if wynik == 0:
                    print(f"Wynik to:{wynik}, ponieważ {liczb1} / {liczb2} nie ma żadnej reszty")
            else:
                    print(f"Wynik to:{wynik}, ponieważ {liczb1} / {liczb2} ma resztę")
            time.sleep(2)
            Main()
        case "Logatytm" | "logatytm":
            liczb1 = int((input("Wpisz podstawę logatytmu") + "\n")))
            liczb2 = int((input("Wpisz liczbę logatytmowaną) + "\n")))
            wynik = Logatytmy(liczb2, liczb1)
            print(f"Wynik to:{wynik}")
            time.sleep(2)
            Main()
        


Main()

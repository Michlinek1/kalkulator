import time
from termcolor import colored
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
            liczb1 = float(input(colored("Wpisz pierwszą liczbę", 'cyan') + "\n"))
            liczb2 = float(input(colored("Wpisz drugą liczbę", 'cyan') + "\n"))
            wynik = Odejmowanie( liczb1, liczb2)
            zaaokraglenie = round(wynik)
            print(f"Wynik to:{wynik} co w zaaokragleniu daje {zaaokraglenie}")
            time.sleep(2)
            Main()
    
        case "Mnożenie" | "mnożenie":
            liczb1 = float(input(colored("Wpisz pierwszą liczbę", 'blue') + "\n"))
            liczb2 = float(input(colored("Wpisz drugą liczbę", 'blue') + "\n"))
            wynik = Mnożenie(liczb1, liczb2)
            zaaokraglenie = round(wynik)
            print(f"Wynik to:{wynik} co w zaaokragleniu daje {zaaokraglenie}")
            time.sleep(2)
            Main()
            
        case "Dzielenie" | "dzielenie":
            liczb1 = float(input(colored("Wpisz pierwszą liczbę", 'green') + "\n"))
            liczb2 = float(input(colored("Wpisz drugą liczbę", 'green') + "\n"))
            wynik = Dzielenie(liczb1, liczb2)
            zaaokraglenie = round(wynik)
            print(f"Wynik to:{wynik} co w zaaokragleniu daje {zaaokraglenie}")
            time.sleep(2)
            Main()
        case "Potęga" | "potęga":
            liczb1 = float(input(colored("Wpisz podstawę potęgi", 'magenta') + "\n"))
            liczb2 = float(input(colored("Wpisz wykładnik potęgi", 'magenta') + "\n"))
            wynik = Potęga(liczb1,liczb2)
            zaaokraglenie = round(wynik)
            print(f"Wynik to:{wynik} co w zaaokragleniu daje {zaaokraglenie}")
            time.sleep(2)
            Main()
            
        case "Modulo" | "modulo":
            liczb1 = float(input(colored("Wpisz pierwszą liczbę", 'magenta') + "\n"))
            liczb2 = float(input(colored("Wpisz drugą liczbę", 'magenta') + "\n"))
            wynik = Modulo(liczb1,liczb2)
            zaaokraglenie = round(wynik)
            if wynik == 0:
                    print(f"Wynik to:{wynik}, ponieważ {liczb1} / {liczb2} nie ma żadnej reszty")
            else:
                    print(f"Wynik to:{wynik}, ponieważ {liczb1} / {liczb2} nie ma żadnej reszty")
            time.sleep(2)
            Main()
        case "Logatytm" | "logatytm":
            liczb1 = int((input(colored("Wpisz podstawę logatytmu", 'white') + "\n")))
            liczb2 = int((input(colored("Wpisz liczbę logatytmowaną", 'white') + "\n")))
            wynik = Logatytmy(liczb2, liczb1)
            print(f"Wynik to:{wynik}")
            time.sleep(2)
            Main()
        


Main()

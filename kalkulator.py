import time
from termcolor import colored
def Dodawanie(x,y):
    return x+y

def Odejmowanie(x,y):
    return x-y

def Mnożenie(x,y):
    return x*y

def Dzielenie(x,y):
    return x/y



def Main():
    Pytanie = str(input(
'''Jakie chcesz zrobić działanie?
Dodawanie
Odejmowanie
Mnożenie
Dzielenie
''' + "\n"))


    match Pytanie:
        case "Dodawanie" | "dodawanie":
            liczb1 = float(input(colored("Wpisz pierwszą liczbę", 'red') + "\n"))
            liczb2 = float(input(colored("Wpisz pierwszą liczbę", 'red') + "\n"))
            wynik = Dodawanie(liczb1, liczb2)
            zaaokraglenie = round(wynik)
            print(f"Wynik to:{wynik} co w zaaokragleniu daje {zaaokraglenie}")
            time.sleep(2)
            Main()
        case "Odejmowanie" | "odejmowanie":
            liczb1 = float(input(colored("Wpisz pierwszą liczbę", 'cyan') + "\n"))
            liczb2 = float(input(colored("Wpisz pierwszą liczbę", 'cyan') + "\n"))
            wynik = Odejmowanie( liczb1, liczb2)
            zaaokraglenie = round(wynik)
            print(f"Wynik to:{wynik} co w zaaokragleniu daje {zaaokraglenie}")
            time.sleep(2)
            Main()
    
        case "Mnożenie" | "mnożenie":
            liczb1 = float(input(colored("Wpisz pierwszą liczbę", 'blue') + "\n"))
            liczb2 = float(input(colored("Wpisz pierwszą liczbę", 'blue') + "\n"))
            wynik = Mnożenie(liczb1, liczb2)
            zaaokraglenie = round(wynik)
            print(f"Wynik to:{wynik} co w zaaokragleniu daje {zaaokraglenie}")
            time.sleep(2)
            Main()
            
        case "Dzielenie" | "dzielenie":
            liczb1 = float(input(colored("Wpisz pierwszą liczbę", 'green') + "\n"))
            liczb2 = float(input(colored("Wpisz pierwszą liczbę", 'green') + "\n"))
            wynik = Dzielenie(liczb1, liczb2)
            zaaokraglenie = round(wynik)
            print(f"Wynik to:{wynik} co w zaaokragleniu daje {zaaokraglenie}")
            time.sleep(2)
            Main()
            
        


Main()

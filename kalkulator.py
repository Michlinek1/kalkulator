def Kalkulator():
    liczbznakow = 0
    Pytanie1 = int(input("Ile liczb chcesz dodać/pomnożyć/podzielić/odjąć" + "\n"))
    if Pytanie1 <= 0:
        print("Liczba ta nie może być mniejsza lub równa 0!")
        Kalkulator()
    liczbznakow += Pytanie1
    #print(liczbznakow)
    Pytanie2 = str(input("Jakie działanie chcesz zrobić?(Dodawanie, odejmowanie, dzielenie, mnożenie)" + "\n"))
    if Pytanie2 == "Dodawanie" or Pytanie2 == "dodawanie":
        for x in range(liczbznakow):
            PytanieDodawanie = input("Jakie liczby chcesz dodać?")
            if PytanieDodawanie.isdigit() == False:
                print("Słowo to nie liczba!")
        return 
    
    
    if Pytanie2 == "Odejmowanie" or Pytanie2 == "odejmowanie":
         for x in range(liczbznakow):
             PytanieOdejmowanie = input("Jakie liczby chcesz odjac?")
             if PytanieOdejmowanie.isdigit() == False:
                 print("Słowo to nie liczba!")
    
    
    if Pytanie2 == "Mnożenie" or Pytanie2 == "mnożenie":
         for x in range(liczbznakow):
             PytanieMnozenie = input("Jakie liczby chcesz pomnozyc?")
             if PytanieMnozenie.isdigit() == False:
                 print("Słowo to nie liczba!")
                 
                 
    if Pytanie2 == "Dzielenie" or Pytanie2 == "dzielenie":
          for x in range(liczbznakow):
              PytanieDzielenie = input("Jakie liczby chcesz podzielic?")
              if PytanieDzielenie.isdigit() == False:
                  print("Słowo to nie liczba!")
        
        
        
        
        
        
        
        
Kalkulator()

import sys
import string

def main():
  oceny = otworz_plik("marks.csv")
  print(oceny)

def otworz_plik(nazwa_pliku):
  dane = [] 
  f = open(nazwa_pliku, "r")
  for linia in f:
    wynik = dict()
    rekord = linia.rstrip()
    lista = rekord.split(',')
    i = 2
    suma = 0
    ilosc = 0
    while i < len(lista):
      suma = suma + int(lista[i])
      ilosc = ilosc + 1
      i = i + 1
    
    srednia = 0
    srednia = suma / ilosc

    wynik['imie'] = lista[0]
    wynik['nazwisko'] = lista[1]
    wynik['srednia'] = srednia
  
    dane.append(wynik)

  return dane

if __name__ == "__main__":
    main()

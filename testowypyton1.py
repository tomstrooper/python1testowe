import os

try:
    liczba1 = input("podaj pierwsza liczbe: ")
    liczba2 = input("podaj druga liczbe: ")
    suma = float(liczba1) + float(liczba2)
    print(suma)
    sumadonapisania = str(suma)
    plikdozapisu = open("pliktestowy.txt","w")
    plikdozapisu.write("to jest probny plik \njego celem jest wyswietlic wynik dodawania\nwynik dodawania to:\n"+sumadonapisania+"\nkolejna linia testowa")
    plikdozapisu.close()
    
except:
    print("podane znaki nie sa liczbami")

plikdoodczytu = open("pliktestowy.txt","r")
print("wypisz wynik poprzedniego dodawania:")
print(plikdoodczytu.readlines()[3])
tekstdoprzepisania = plikdoodczytu.read()
plikdoodczytu.close()
print(tekstdoprzepisania)
plik2 = open("teksttest2.txt","w")
plik2.write("wynik poprzedniego dodawania to: ")
plik2.close()
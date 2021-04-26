import numpy as np

# Zad1
# Utworz dwie macierze 1x3 roznych wartosci a nastepnie wykonaj operacje mnozenia

m1 = np.array([2, 4, 9])
m2 = np.array([4, 6, 1])
print("Zad1")
print(np.multiply(m1, m2))

# Zad2
# Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.

m3 = np.array([[1, 4, 5], [2, 3, 9], [5, 5, 8]])
m4 = np.array([[2, 4, 7, 7], [1, 3, 6, 9], [5, 5, 0, 1], [2, 8, 8, 8]])

print("\nZad2")
print(m3.min(axis=1))
print(m3.min(axis=0))
print(m4.min(axis=1))
print(m4.min(axis=0))

# Zad3
# Wykorzystaj macierze z zadania pierwszego i wykonaj iloraz macierzy.

print("\nZad3")
print(np.dot(m1.T, m2))
# trasponowane ze wzgledu na brak mozliwosci mnozenia macierzy 1x3 przez 1x3


# Zad4
# Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite,
# a druga liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia.

m5 = np.array([2, 5, 9])
m6 = np.array([3., 6., 1.])

print("\nZad4")
print(np.multiply(m5, m6))

# Zad5
# Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla
# każdej z jej wartości i zapisz do zmiennej “a”.

m7 = np.array([[2, 5, 6], [1, 3, 9]])

print("\nZad5")
a = np.sin(m7)
print(a)

# Zad6
# Utwórz nową macierz 2x3 różnych wartości a następnie wylicz
# cosinus dla każdej z jej wartości i zapisz do zmiennej “b”.

m8 = np.array([[1, 3, 8], [5, 9, 0]])

print("\nZad6")
b = np.cos(m8)
print(b)

# Zad7
# Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.

print("\nZad7")
print(np.add(a, b))

# Zad8
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.

m9 = np.arange(9).reshape(3, 3)
print("\nZad8")
for a in m9:
    print(a)

# Zad9
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy element
# korzystając z opcji “spłaszczenia” macierzy. (użyj funkcji flat())

m10 = np.arange(1, 19, 2).reshape(3, 3)
print("\nZad9")
for b in m10.flat:
    print(b)

# Zad10
# Wygeneruj macierz 9x9 a następnie zmień jej kształt.
# Jakie mamy możliwości i dlaczego?

m11 = np.arange(9 * 9).reshape(9, 9)
print("\nZad10")
print(m11)
print(m11.reshape(3, 27))
print(m11.reshape(27, 3))
print(m11.reshape(81, 1))
print(m11.reshape(1, 81))
# mamy mozliwosc zmienic ksztalt tylko w taki sposob by dalej ilosc
# wszystkich elementow macierzy ze zmienionym ksztaltem
# rownala sie ilosci wszystkich elementow w pierwotnej macierzy

# Zad11
# Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4.
# Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6.
# Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?

m12 = np.arange(12).reshape(3, 4)
m13 = np.arange(12).reshape(4, 3)
m14 = np.arange(12).reshape(2, 6)
print("\nZad11")
for a in m12, m13, m14:
    for b in m12.flat:
        print(b)
    print("")

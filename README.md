# Projekt 1: Transformacje
Program służy do transformacji współrzędnych. 

##### Dostępne transformacje:
- XYZ (geocentryczne) --> BLH (elipsoidalne)
- BLH --> XYZ
- XYZ --> NEUp (topocentryczne)
- BL --> PL2000
- BL --> PL1992

##### Dostępne elipsoidy:
- GRS80
- WGS84
- Krasowski

## Wymagania
- Windows 11
- python 3.10
- biblioteka numpy
- biblioteka argparse

## Opis użycia programu
Program umożliwia podawanie argumentów przy wywołaniu za pomocą odpowiednich flag.
```sh
-p
```
Przyjmuje ścieżkę do pliku z danymi wejściowymi, jeśli plik jest w tym samym folderze co skrypt, to wystarczy nazwa pliku z rozszerzeniem.
```sh
-el
```
Przyjmuje nazwę elipsoidy. Dostępne: WGS84, GRS80 lub KRASOWSKI. Wielkość wpisywanych liter nie ma znaczenia.
```sh
-t
```
Przyjmuje nazwę wybranej transformacji. Dostępne: XYZ2BLH, BLH2XYZ, PL2000, PL1992, XYZ2NEUP. Wielkość wpisywanych liter nie ma znaczenia.
Przykładowe wywołanie:
```sh
skrypt.py -p plik_dane_XYZ2BLH.txt -el grs80 -t xyz2blh
```
Następnie wyświetli się poniższy komunikat o utworzeniu pliku z wynikami transformacji w folderze, w którym znajduje się skrypt.py.
```sh
Plik wynikowy zostal utworzony.
Jezeli chcesz wykonac kolejna transformacje wpisz TAK jesli chcesz zakonczyc NIE:
```
 Ukaże się również informacja o tym czy użytkownik chce wykonać kolejną transformacje. Jeśli użytkownik wpisze **NIE** program zakończy działanie.
```sh
Jezeli chcesz wykonac kolejna transformacje wpisz TAK jesli chcesz zakonczyc NIE: nie
Koniec programu
```
W przypadku kiedy użytkownik będzie chciał wykonać kolejną transformację, wpisująć **TAK**, program wyświetli informację o ponownym podaniu elipsoidy, pliku z danymi i transformacji do wykonania. Po podaniu tych wartości całość będzie wyglądać przykładowo w następujący sposób:
```sh
Jezeli chcesz wykonac kolejna transformacje wpisz TAK jesli chcesz zakonczyc NIE: tak
Podaj nazwe elipsoidy: wgs84
Wklej sciezke do pliku txt z danymi: plik_dane_XYZ2NEUP.txt
Jaka transformacje wykonac?: xyz2neup
Plik wynikowy zostal utworzony.
Jezeli chcesz wykonac kolejna transformacje wpisz TAK jesli chcesz zakonczyc NIE: nie
Koniec programu
```
Takie same komunikaty pojawią się także w momencie kiedy użytkownik nie poda, którejś z tych wartości przy wywoływaniu za pomocą flag.

```sh
skrypt.py -p plik_dane_XYZ2BLH.txt -t xyz2blh
Podaj nazwe elipsoidy:
```

## Opis przykładowych danych do transformacji
Wszystkie dane w plikach wejściowych i wyjściowych są oddzielone od siebie spacją.
#### BL --> PL2000/PL1992
- plik_dane_2000_92.txt

>52.2297 21.0122
50.0647 19.9450
54.3722 18.6386
51.1079 17.0385
51.7592 19.4550

Pierwsza wartość to szerokość geodezyjna, a druga to długość geodezyjna.

- plik_wynikowy_PL2000_grs80.txt

> 5788456.487 7500833.512
5548149.630 7424469.100
6027068.915 6541498.772
5664093.136 6432667.451
5737111.071 6600451.534

Pierwsza wartość to współrzędna X, a druga to współrzędna Y.

#### BLH --> XYZ
- plik_dane_BLH2XYZ.txt

>52.2297 21.0122 78.000
50.0647 19.9450 219.000
54.3722 18.6386 5.000
51.1079 17.0385 118.000
51.7592 19.4550 182.000

Pierwsza wartość to szerokość geodezyjna, druga to długość geodezyjna, a trzecia to wysokość punktu.

- plik_wynikowy_BLH2XYZ_grs80.txt

> 3654515.722 1403730.043 5018560.041
3856423.941 1399432.680 4867579.707
3528330.697 1190061.310 5160990.221
3836640.805 1175798.397 4941181.911
3730268.374 1317661.092 4986406.785

Pierwsza wartość to współrzędna X, druga to współrzędna Y, a trzecia to współrzędna Z.
#### XYZ --> BLH
- plik_dane_XYZ2BLH.txt

>3654515.7218380477 1403730.0433548905 5018560.040857761
3856423.941196924 1399432.680121372 4867579.706638583
3528330.6974752024 1190061.3100085442 5160990.220680703
3836640.8048792393 1175798.397398429 4941181.911009777
3730268.373914433 1317661.09184508 4986406.785425414

Pierwsza wartość to współrzędna X, druga to współrzędna Y, a trzecia to współrzędna Z.

- plik_wynikowy_XYZ2BLH_grs80.txt

> 52.2297000000 21.0122000000 78.000
50.0647000000 19.9450000000 219.000
54.3722000000 18.6386000000 5.000
51.1079000000 17.0385000000 118.000
51.7592000000 19.4550000000 182.000

Pierwsza wartość to szerokość geodezyjna, druga to długość geodezyjna, a trzecia to wysokość punktu.

#### XYZ --> NEUp
- plik_dane_XYZ2NEUP.txt

>3673602.0707659787 1410163.7139986877 5002803.345368741
2.234878304399999976e+07 1.470313728000000119e+07 3.847713999999999942e+04
-2.391130946000000089e+07 -1.089180339500000142e+07 -2.229962486000000034e+06
1.256775858699999936e+07 1.288512925399999879e+07 1.944924987600000203e+07
1.982159728800000250e+07 3.882086669999999925e+06 1.731373310199999809e+07
-5.921297010999999940e+06 -2.445428761199999973e+07 -8.484889633000001311e+06

W pierwszym wierszu znajdują się kolejno współrzędne X, Y, Z odbiornika na Ziemi. Natomiast w pozostałych wierszach pierwsza wartość to współrzędna X satelity, druga to współrzędna Y satelity, a trzecia to współrzędna Z satelity.

- plik_wynikowy_XYz2NEUP_wgs84.txt

> -20549047.679 5717473.618 9754855.210
19314544.051 -1599327.517 -24268687.235
-889561.130 7525422.589 19027805.115
-4998318.921 -3479185.048 19527908.835
6058904.131 -20708041.190 -21849862.779

W wierszach znajdują się kolejno współrzędne X, Y, Z w układzie topocentrycznym.

## Błędy
- Program nie wykona transformacji dla plików z danymi z tylko jednym wierszem. Zostanie to uznane jako błąd, nawet jeśli dane wprowadzone są poprawnie.
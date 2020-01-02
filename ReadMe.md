**Parcel Profile**

Prosta aplikacja badająca możliwość użycia API Usługi Lokalizacji Działek Katastralnych ([dokumentacja](https://uldk.gugik.gov.pl/opis.html)) oraz usługi Numerycznego Modelu terenu ([dokumentacja](https://services.gugik.gov.pl/nmt/)) udostępnianych przez Główny Urząd Geodazji i Kartografii do uzyskania podstawowych informacji przestrzennych o działce katastralnej jeśli posiadamy tylko jej numer lub lokalizację.

Aplikację napisałem jako spike dla własnych potrzeb i udostępniam as-is - może się komuś przyda. Jak będzie zainteresowanie czy zapotrzebowanie mogę rozszerzyć

Ta wersja wykonuje jedynie podstawowe operacje - pobiera geometrię działki na podstawie jej numeru lub współrzędnych z ULDK, po czym przesyła ją do NMT i pobiera maksymalną i minimalną wysokość oraz obliczony obszar.

**Przykładowe wywołania**

Dla wyszukania działki numer 519 w Bielsku-Białej:

`python3 main.py -t '246101_1.0005.519'`

Ta sama działka po współrzędnych w układzie "Polska 1992" (EPSG:2180)

`python3 main.py -y 217163 -x 503635`

Modułów można również użyć importując je do swojego kodu - przykłady użycia można znaleźć w plikach z testami jednostkowymi (test_*.py)

Have fun

![licencja](https://s23527.pcdn.co/wp-content/uploads/2015/12/DWTFPL.jpg.optimal.jpg "Logo Title Text 1")
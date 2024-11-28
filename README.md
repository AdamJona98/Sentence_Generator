Mondatgenerátor

Fejlesztő: Jóna Ádám

Ez az alkalmazás egy egyszerű interaktív felületen véletlenszerű mondatokat generál a leggyakoribb angol szavak listájából. 
A felhasználók testreszabhatják a mondat megjelenését, beleértve a betűtípust, betűméretet, színt, valamint a mondat hosszát. 

Funkciók:

1. Mondatgenerálás
- Véletlenszerű angol mondatok generálása a `words.txt` szöveges fájl szavaiból.
- A mondathossz a felhasználó által állítható 2 és 8 szó között.
- A generált mondat mindig nagybetűvel kezdődik és ponttal végződik.

2. Testreszabható Megjelenés
- Betűtípus kiválasztása:
  - Négy jól megkülönböztethető betűtípus közül választhat: Helvetica, Courier, Comic Sans MS, Impact.
- Betűméret módosítása:
  - A szöveg mérete 16 és 32 pont között állítható.
- Betűszín kiválasztása:
  - A felhasználó szabadon választhat színt egy grafikus színválasztó segítségével.

Rendszerkövetelmények
- Python 3.x telepítve a gépre.
- A `tkinter` modul elérhetősége (alapértelmezett a Python telepítésekor).

Felépítés:
- `main.py`: Az alkalmazás indítómodulja.
- `sentence_properties.py`: A mondat tulajdonságait kezelő osztály.
- `app_window.py`: Az alkalmazás grafikus interfészének kezelőmodulja.
- `sentence_generator.py`: A véletlenszerű mondat generálásért felelős modul.
- `words.txt`: A leggyakoribb angol szavak listája, amelyből a mondatokat generáljuk.

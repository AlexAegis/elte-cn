# [Lesson 4](./lesson4.pdf)

## Feladat 1

Készítsünk egy TCP alkalmazást, amelyen több kliens képes egyszerre üzenetet küldeni a szervernek, amely minden üzenetre csak annyit ír vissza, hogy „OK”. (Használjuk a select függvényt!)

## Feladat 2

Készíts egy olyan több kliens-szerver alkalmazást, ahol a szerver gondol egy n egész számra 1 és 100 között, és a kliensek megpróbálják kitalálni!
Használd a select függvényt!

–A csatlakozott kliens-oldalon lévő felhasználó kérdéseket tesz fel: kisebb-e mint n(<n), nagyobb-e mint n(>n) vagy rákérdez egy konkrét értékre (=n)

–Ezt egy "cH" formátumú struktúrával kell elküldeni–A szerver válaszol: "no", "yes", "win" és "end" üzenetekkel

–Ha jó rákérdezés történik, akkor a rákérdezőnek "win" üzenet jön, a többieknek pedig "end" üzenet, és vége a játéknak (megtörténik a kapcsolat bontás)

–Ha a szerver minden klienssel bontotta a kapcsolatot, akkor kilép

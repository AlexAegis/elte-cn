# [Lesson 2](./lesson2.pdf)

## Feladat

Adott a cs1.json, ami tartalmazza egy irányítatlan gráf leírását. A gráf végpont (end-points) és switch (switches) csomópontokat tartalmaz. Az élek (links) kapacitással rendelkeznek (valós szám). Tegyük fel, hogy egy áramkör kapcsolt hálózatban vagyunk és valamilyen RRP - szerű erőforrásfoglaló protokollt használunk. Feltesszük, hogy csak a linkek megosztandó és szűk erőforrások. A json tartalmazza a kialakítható lehetséges útvonalakat (possible-cicuits), továbbá a rendszerbe beérkező, két végpontot összekötő áramkör igényeket kezdő és végidőponttal. A szimuláció at=1 időpillanatban kezdődik és t=duration időpillanatban ér véget. Készíts programot, ami leszimulálja az erőforrások lefoglalását és felszabadítását a JSON fájlban megadott topológia, kapacitások és igények alapján! A program bemenete: cs1.jsonA program kimenete: Minden igény lefoglalását és felszabadítását írassuk ki a stdout-ra. Foglalás esetén jelezzük, hogy sikeres vagy sikertelen volt-e. Megj.: sikertelen esetben az igénnyel más teendőnk nincs, azt eldobhatjuk.

Pl.:
foglalas: A<->C st:1 –sikeres
foglalas: B<->C st:2 –sikeres
felszabaditas: A<->C st:5
foglalas: D<->C st:6 –sikeres
foglalas: A<->C st:7 –sikertelen

## Házi feladat I. (4 pont) Alexa-top-1M

Szept 30-ig

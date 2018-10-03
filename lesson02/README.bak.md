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

Az [Alexa-top-1M](http://s3.amazonaws.com/alexa-static/top-1m.csv.zip) adathalmaz tartalmazza a legnépszerűbb 1 millió website domain nevét népszerűségi sorrendben:
Válasszuk ki az első és utolsó 100 nevet a listából, írjunk egy python programot, ami végig megy a leszűkített 200 elemű listán és minden címre lefuttatja a traceroute és ping toolokat, majd az eredményeket rendezett formában két fájlba írja! Ld.subprocess! Lehetőség szerint ne az egyetemi hálózaton futassuk az adatbegyűjtést!
Traceroute paraméterek: max.30 hopot vizsgáljunk
Ping paraméterek: 10 próba legyen
Kimenetifájlok (ld.következődia):
traceroute.json
ping.json

traceroute.json:

```json
{
	"date": "20180916",
	"system": "windows",
	"traces": [
		{
			"target": "www.valami.com",
			"output": "Tracing route to www. . . "
		}
	]
}
```

ping.json:

```json
{
	"date": "20180916",
	"system": "linux",
	"pings": [
		{
			"target": "www.valami.com",
			"output": "Pingingwww. . . "
		}
	]
}
```

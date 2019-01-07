# Quiz

24. page:

    -   A megbízató adatátvitel 4 fő célja közül melyik szól az adat leszállítási idejének minimalizálásáról.

        -   Időbeliség/Timeliness

    -   Egy csúszóablak (sliding window) protokoll esetén a sorszámok tere 0,1,2,3,4,5,6,7, a négy hosszú küldési ablakban az 1,2,3,4 sorszámok vannak. Az 1-es sorszámú nyugta beérkezése után, milyen sorszámmal lehetnek elküldött de nem nyugtázott csomagok.

        -   2,3,4,5

    -   Melyik nyugtázási módszerre igaz az alábbi állítás? A nyugta a legnagyobb sorszámot tartalmazza, amelyre igaz, hogy az összes kisebb (vagy egyenlő) sorszámú csomag már sikeresen megérkezett a vevőhöz.

        -   Kumulatív nyugta - cummulative ACK

    -   Egy csúszóablak (sliding window) protokoll esetén a sorszámok tere 0,1,2,3,4,5,6,7. A fogadó 2 csomagot tud pufferelni, a vételi ablakában 2,3 sorszámok szerepelnek. Mit tesz a fogadó egy 1-es sorszámú csomag beérkezése esetén?

        -   Eldobja a csomagot és nyugtát küld.

    -   Kumulatív nyugta (cummulative ACK) esetén miként tudjuk detektálni a csomagvesztést?

        -   Az izolált csomagvesztéseket nyugta dupliokátumok jelzik. Emelett timerekkel is dolgozik a módszer.

    -   Melyik nyugtázási módszerre igaz az alábbi állítás?
        Teljes információt ad a forrásnak és jól kezeli a nyugták elvesztését is, azonban az a nagy hálózati overheadje miatt csökkenti a teljesítményt.

            -   Teljes információ visszacsatolás - Full Information Feedback

    -   Hogyan definiáltuk a helyességet!
        Egy szállítási mechanizmus helyes, akkor és csak akkor...

        -   Minden elvesztett vagy hibás csomagot újraküld.

    -   Adott egy hálózat:
        A------------1 Gbps---------B------------10 Gbps--------C

        és adott 3 folyam:

        1. folyam: A-ból B-be küld adatot
        2. folyam: B-ból C-be küld adatot
        3. folyam: A-ból C-be küld adatot

        Milyen rátát kap a 2. folyam Mbps-ben kifejezve, ha max-min fair allocation-t alkalmazunk a sávszélességek kiosztására (a fenti példában)?

        -   9500.0 (megközelítőleg : 0.0)
            9.5 (megközelítőleg: 0.0)

    -   Mi a folyam vezérlés (flow control) célja a megbízható adatátvitel során?

        -   A lassú vevő túlterhelésének megakadályozása.

    -   Mely állítások igazak a végpont-végpont megbízhatóságra?

        -   A végpont-végpont megbízhatóságot az L4 (Transport - Szállítói) réteg biztosítja.
        -   A hálózat legyen a lehető legegyszerűbb, azaz nem biztosít végpont-végpont megbízhatóságot.
        -   Az alkalmazásoknak nem kell a hálózati problémákkal foglalkozniuk, így a megbízhatóság biztosításával sem.

25. page:

    -   Mik történhetnek egy csomaggal átvitel során, melyet egy megbízható végpont-végpont adattranszport protokollnak kezelnie kell?

        -   csomagvesztés - loss
        -   meghibásodás - being corrupted
        -   duplikátumok - duplicates
        -   várakoztatás - being delayed
        -   csomagok sorrendjének megváltoztatása - reordering

    -   Melyik nyugtázási módszerre igaz az alábbi állítás?
        A nyugta a legnagyobb sorszámot tartalmazza, amelyre igaz, hogy az összes kisebb (vagy egyenlő) sorszámú csomag már sikeresen megérkezett a vevőhöz.
        -   Kumulatív nyugta - cummulative ACK

26. page:

    -   Kumulatív nyugta (cummulative ACK) esetén miként tudjuk detektálni a csomagvesztést?
        -   Az izolált csomagvesztéseket nyugta duplikátumok jelzik. Emellett timerekkel is dolgozik a módszer.

27. page:

    -   A megbízható adatátvitel 4 fő célja körül melyik szól arról, hogy:
        "az adat leszállítása biztosított, sorrend helyes és átvitel során nem módosul".
        -   Helyesség/Correctness

28. 32page:

    -   Jelölje be, hogy az állítások mely multiplexálási technikákra igazak!

        -   A teljes frekvencia tartományt szűkebb sávokra bontja
            > **Frekvencia multiplexálás**
        -   Vezetékes kommunikáció esetén minden egyes csatornához külön pont-pont fizikai kapcsolat tartozik
            > **Térbeli multiplexálás**
        -   Vezeték nélküli kommunikáció esetén minden egyes csatornához külön antenna rendelődik
            > **Térbeli multiplexálás**
        -   Minden állomás saját frekvencia tartományt kap
            > **Frekvencia multiplexálás**
        -   Diszkrét időszeletek használata
            > **Idő-osztásos multiplexálás (TDM)**
        -   Minden állomás saját időszeletet kap
            > **Idő-osztásos multiplexálás (TDM)**

    -   Mely állítások igazak az alapsávú átvitelre?

        -   a digitális jel direkt árammá vagy feszültséggé alakul
        -   a jel minden frekvencián átvitelre kerül

    -   Mit nevezünk elnyelődésnek?

        -   A küldési és vételi energiák hányadosát.

    -   Egy s(t) függvényt a sin(t) vivőhullámra a következőképp kódolunk: s(t)\*sin(t)
        Melyik modulációs technikát alkalmaztuk?

        -   Amplitúdó moduláció

    -   Egy s(t) függvényt a sin(t) vivőhullámra a következőképp kódolunk: sin(t\*s(t))
        Melyik modulációs technikát alkalmaztuk?

        -   Frekvencia moduláció

    -   Mely modulációs technika használja a vivőhullám több jellemzőjét is a szimbólumok kifejezésére?

        -   QAM-16 technika

    -   A 100 Mbps Ethernetnél alkalmazott 4/5 kódolással 20 %-ot veszítünk a hatékonyságból!

    -   Két szimbólum használata esetén a szimbólum ráta 4 Baud. Négy szombólum használata mellett mekkora lesz a szimbólum ráta, ha semmi mást nem változtatunk?

        -   4 Baud

    -   Egy s(t) függvényt a sin(t) vivőhullámra a következőképp kódolunk: sin(t + s(t))
        Melyik modulációs technikát alkalmaztuk?

        -   Fázis moduláció

    -   Mely állítások igazak az szélessávú átvitelre?
        -   egy széles frekcencia tartományban történik az átvitel, nem minden frekvencián kerül átvitelre a jel **NOT VERIFIED**
        -   a jelet modulálással ülteti egy vivóhullámra **NOT VERIFIED**

29. 33page:

    -   Négy szimbólum használata esetén hány bitet tudunk egy szombólumba kódolnu?

        -   2

    -   Mi az összefüggés a frekvencia (f), a hullámhossz (L (LAMBDA)) és a fénysebesség (c) között? - f\*L = c

    -   Mely állítások igazak a fizikai rétegre? - Szolgáltatása, hogy információt (biteket) visz át két fizikailag összegkötött eszköz között

30. 41page:

    -   Mekkora következő két bitsorozat Hamming-távolsága?

        -   d( 11111, 11000 ) = 3

    -   Mekkora következő két bitsorozat Hamming-távolsága?

        -   d( 1001, 1011 ) = 1

    -   Minek kell teljesülnie a chip vektorokra a CDMA módszer esetén?

        -   Páronként ortogonális vektoroknak kell lenniük.

    -   Alkosson párokat a keretezési technikák jellemzőiből és neveiből!

        -   A fogadó az adatban előforduló minden 11111 részsorozat után ellenőrzi a követező bitet, majd ez alapján lép tovább.
            > **Bit beszúrás**
        -   Nagyon érzékeny a bithibákra (pl. fejléc meghibásodása)
            > **Karakterszámlálás**
        -   Egy speciális ESC (Escape) bájtot szúr be az "adat" ESC bájtok elé
            > **Bájt beszórás**
        -   SONET hálózatoknál alkalmazzák
            > **Óra alapú keretezés**

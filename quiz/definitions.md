# Definitions

## 1. lecture

-   Mi a **hálózati hoszt**?

    > Olyan eszköz, amely egy számítógépes hálózattal áll összeköttetésben. Infót oszthat meg, szolgáltatásokat és alkalmazásokat biztosíthat a hálózat további csomópontjainak.

-   Mi a **átviteli csatorna**?

    > Az a közeg, amelyen a kommunikáció folyik a résztvevő hosztok között. Ez a közeg lehet egy koaxális kábel, a levegő, optikai kábel, stb.

-   Definiálja a **propagációs késés**t.

    > Az az időtartam, amely a jelnek szükséges ahhoz, hogy a küldőtől megérkezzen a címzetthez.

    > Jelölése: d<sub>prop</sub> vagy d

-   Definiálja az **átviteli késleltetés**.

    > Az az időtartam, amely egy csomag összes bitjének az átviteli csatornára tételéhez szükséges.

    > Jelölése: d<sub>T</sub>

-   Definiálja a **Jel sávszélesség**et.

    > Jel feldolgozás esetén az egymást követő frekvenciák legnagyobb és legkisebb eleme közötti különbséget nevezik jel sávszélességnek.

    > Tipikusan Hertz-ben mérik.

-   Definiálja a **Hálózati sávszélesség**et.

    > Az adat átviteléhez elérhető vagy felhasznált kommunikációs erőforrás mérésére szolgáló mennyiség, amelyet bit per másodpercben szoktak kifejezni.

-   Mi a fő különbség a **csomagkapcsolt** és az **áramkörkapcsolt** hálózatok között?

    > **Áramkörkapcsolt**: pl a telefon, egy hoszt dedikált erőforrást használ, az erőforrást le kell foglalni.

    > **Csomagkapcsolt**: csak rá kell tenni a csomagokat a hálózatra, és az állomások maguk döntik el, merre továbbítják (nem kell lefoglalni az erőforrást, megosztott használat)

-   Sorolja fel a **hálózati kiterjedések**et.

    > PAN: Personal Area Network (1 m<sup>2</sup>)

    > LAN: Personal Area Network (10-1000 m<sup>2</sup>)

    > MAN: Metropolitan Area Network (10 km<sup>2</sup>)

    > WAN: Wide Area Network (100-1000 km<sup>2</sup>, de az internet is)

-   Mit jelent a **legjobb szándék (best effort)** elv a hálózati kommunikációban?

    > Ha egy csomag nem éri el a célt, akkor törlődik, ilyenkor az alkalmazás újraküldi.

-   Mit jelent a "Black-box" megközelítés a kapcsolatokra?

    > Az eszközök (black box, később gateway, router) nem őrzik meg a csomaginformációkat, nincs folyam-felügyelet

-   Sorolja fel az **internet 5 (előadáson elhangzott) jellemzőjét**.

    > rendszerfüggetlenség

    > nincs központi felügyelet

    > LAN-okból áll

    > globális

    > szolgáltatásokat nyújt, pl WWW, e-mail, fájlátvitel

-   Hány réteget különböztet meg az **ISO/OSI referencia modell**? Sorolja fel őket.

    | #   |                 |              |
    | --- | --------------- | ------------ |
    | 7.  | Alkalmazási     | Application  |
    | 6.  | Megjelenítési   | Presentation |
    | 5.  | Munkamenet/Ülés | Session      |
    | 4.  | Szállítói       | Transport    |
    | 3.  | Hálózati        | Network      |
    | 2.  | Adatkapcsolati  | Data Link    |
    | 1.  | Fizikai         | Physical     |

-   Hány réteget különböztet meg a **Tannenbaum**-féle hibrid rétegmodell? sorolja fel őket.

    | #   |                |             |
    | --- | -------------- | ----------- |
    | 5.  | Alkalmazási    | Application |
    | 4.  | Szállítói      | Transport   |
    | 3.  | Hálózati       | Network     |
    | 2.  | Adatkapcsolati | Data Link   |
    | 1.  | Fizikai        | Physical    |

    > sima TCP/IP modellben a fizikai és adatkapcsolati réteg egy kapcsolati rétegként jelenik meg

-   Mi az "Open System Interconnection Reference Model" (**ISO/OSI**), hogyan specifikáljuk az egyes rétegeket?

    > Open System Interconnection Reference Model: 7 rétegű standard, koncepcionális modellt ad meg kommunikációs hálózatok belső funkcionalitásához.

    > Réteg: szolgáltatás (mit csinál), interfész (hogyan férhetünk hozzá), protokoll (hogyan implementáljuk)

-   Mi a feladata és mik a főbb funkcionalitásai az ISO/OSI modell **fizikai rétegének**?

    -   Szolgáltatás

        -   Információt visz át két fizikailag összekötött eszköz között
        -   Definiálja az eszköz és a fizikai átviteli közeg kapcsolatát

    -   Interfész

        -   Specifikálja egy bit átvitelét

    -   Protokoll

        -   Egy bit kódolásának sémája
        -   Feszültség szintek
        -   Jelek időzítése

    -   Példák

        -   koaxiális kábel
        -   optikai kábel
        -   rádió frekvenciás adó

-   Mi a feladata és mik a főbb funkcionalitásai az ISO/OSI modell **adatkapcsolati rétegének**?

    -   Szolgáltatás

        -   Adatok keretekre tördelésezés: határok a csomagok között
        -   Közeghozzáférés vezérlés (MAC)
        -   Per-hop megbízhatóság és folyamvezérlés

    -   Interfész

        -   Keret küldése két közös médiumra kötött eszköz között

    -   Protokoll

        -   Fizikai címzés (pl. MAC address, IB address)

    -   Példák

        -   Ethernet
        -   Wifi
        -   InfiniBand

-   Mi a feladata és mik a főbb funkcionalitásai az ISO/OSI modell **hálózati rétegének**?

    -   Szolgáltatás

        -   Csomagtovábbítás
        -   Útvonalválasztás
        -   Csomag fragmentálás kezelése
        -   Csomag ütemezés
        -   Puffer kezelés

    -   Interfész

        -   Csomag küldése egy adott végpontnak

    -   Protokoll

        -   Globálisan egyedi címeket definiálása
        -   Routing táblák karbantartása

    -   Példák

        -   Internet Protocol (IPv4)
        -   IPv6

-   Mi a feladata és mik a főbb funkcionalitásai az ISO/OSI modell **ülés/munkamenet rétegének**?

    -   Szolgáltatás

        -   kapcsolat menedzsment: felépítés, fenntarás és bontás
        -   munkamenet típusának meghatározása
        -   szinkronizációs pont menedzsment (checkpoint)

    -   Interfész

        -   Attól függ…

    -   Protokoll

        -   Token menedzsment
        -   Szinkronizációs checkpoints beszúrás

    -   Példák

        -   nincs

-   Mi a feladata és mik a főbb funkcionalitásai az ISO/OSI modell **megjelenítési rétegének**?

    -   Szolgáltatás

        -   Adatkonverzió különböző reprezentációk között
        -   Pl. big endian to little endian
        -   Pl. Ascii to Unicode

    -   Interfész

        -   Attól függ…

    -   Protokoll

        -   Adatformátumokat definiál
        -   Transzformációs szabályokat alkalmaz

    -   Példák

        -   nincs

-   Mi a feladata és mik a főbb funkcionalitásai az ISO/OSI modell **alkalmazási rétegének**?

    -   Szolgáltatás

        -   Bármi…

    -   Interfész

        -   Bármi…

    -   Protokoll

        -   Bármi…

    -   Példák

        -   kapcsold be a mobilod és nézd meg milyen appok vannak rajta…

## 2. lecture

-   Mit jelent a hálózatok esetén az **adatok burkolása**?

    > Mindegyik réteg hozzáteszi a saját fejlécét az üzenethez, amely réteg-specifikus infókat tartalmaz
    > interfészek definiálják a rétegek közti interakciókat, a rétegek csak az alattuk lévőkre épülnek
    > pl. a fizikai réteg nem tud az alkalmazásiról, az alkalmazásinak nem kell törődnie a fizikaival

-   Adjon egy valós példát **adatok beburkolására** (pl. az előadáson látott Internet példa)!

    | Ethernet Header | IP Header | TCP Header | HTTP Header | Web Page | Ethernet Trailer |
    | --------------- | --------- | ---------- | ----------- | -------- | ---------------- |
    |                 |           |            |             |          |                  |

-   Mit értünk **Internet homokóra** alatt? Miért nehéz az IPv6-ra való átállás?

    > **TODO**

-   A Hálózati réteg funkcióit milyen **síkok (planes)** mentén csoportosíthatjuk még?

    > **Control plane (vezérlési sík)**: hogyan határozzuk meg az útvonalat?

    > **Data plane (adat sík)**: hogyan továbbítjuk az adatot egy útvonal mentén?

-   Jellemezze egy mondatban a **tűzfalakat**, **proxy**kat és **NAT doboz**okat!

    > **Tűzfal**: védelmi rendszer, az alkalmazási réteg fejléceit is vizsgálnia kell

    > **Proxyk**: alkalmazási végpontot szimulál a hálózatban

    > **NAT doboz**: megtöri a végpont-végpont elérhetőséget a hálózatban

-   Mi a **szimbólumráta** és az **adatráta**? Mi a mértékegységük?

    > **Szimbólumráta**: elküldött szimbólumok száma másodpercenként (Baud)

    > **Adatráta**: elküldött bitek száma másodpercenként (bps)

    > Egy szimbólum állhat több bitből

-   Mit mond ki a **Nyquist tétel**?

    > _Zajmentes csatornán_\
    > Max adatsebesség = 2**H** \* log<sub>2</sub>(**V**) bps\
    > **H**: sávszél \
    > **V**: szimbólumok száma

-   Mit mond ki a **Shannon tétel**?

    > _Zajos csatornán_\
    > Max adatseb = **H** \* log<sub>2</sub>(1 + **S/N**) bps\
    > **H**: sávszél\
    > **S/N**: jel-zaj teljesítményének hányadosa

-   Ismertesse a fizikai rétegben a lehetséges **átviteli közegek** fajtáit!

    > **Mágneses adathordozó** _(merevlemez)_\
    > **Sodort érpár** _(távbeszélőrendszerek)_\
    > **Koaxális kábel** _(nagyobb sebesség és távolság)_\
    > **Fénykábel** _(fényforrás, közeg, detektor)_\
    > **Rádiófrekvenciás** _(egyszerű, nagy táv, frekvenciafüggő terjedés)_\
    > **Mikrohullámú** _(egyenes vonal mentén terjed, elhalkulás problémája, olcsó)_\
    > **Infra** _(kis táv, szilárd tárgyakon nem hatol át)_\
    > **Látható fény** _(lézerforrás + érzékelő, nagy sávszél, olcsó, nem > engedélyköteles, időjárásfüggő)_\
    > **Műholdas**

-   Mit nevezünk **frekvenciá**nak? Hogyan jelölik? Mi a mértékegysége?

    > Az elektromágneses hullám másodpercenkénti rezgésszáma.

    > Jelölése: **f**\
    > Mértékegysége: Hertz (**Hz**)

-   Mi a **hullámhossz**?

    > Két egymást követő hullámcsúcs (vagy hullámvölgy) közti távolság

-   **Fénysebesség**

    > Elektromágneses hullámok terjedési sebessége vákuumban

    > Jelölése: **c** = 3\*10<sup>8</sup> m/s\
    > _rézben és üvegszálban ennek csak 2/3-a_

-   Összefüggés **hullámhossz, frekvencia és fénysebesség** között

    > **hullámhossz × frekvencia = fénysebesség**

-   Soroljon fel 3 **elektromágneses tartományt a frekvenciáik növekvő sorrendjében**!

    1.  rádió
    2.  mikrohullám
    3.  infravörös
    4.  látható
    5.  ultraibolya
    6.  röntgensugár
    7.  gammasugár

-   Milyen frekvencia tartomány átvitelére alkalmas a **sodort érpár**, a **koax kábel** és az **optikai szál**?

    | Közeg            | Frekcenciatartomány                  |
    | ---------------- | ------------------------------------ |
    | **Sodort érpár** | 10<sup>4</sup> - 10<sup>6</sup> Hz   |
    | **Koax kábel**   | 10<sup>5</sup> - 10<sup>8</sup> Hz   |
    | **Optikai szál** | 10<sup>14</sup> - 10<sup>15</sup> Hz |

-   Soroljon fel **3 óraszinkronizációs módszer**t!

    > **Explicit órajel**: párhuzamos átviteli csatornák használata esetén explicit küldjük az órajeleket; rövid átvitele esetén alkalmas\
    >  **Kritikus időpontok**: adott időkor sync, pl szimbólum v blokk kezdetén ezen kívül az órák szabadon futnak, remélhetőleg szinkronban\
    >  **Önütemező jel**: külön órajel sync nélkül dekódolható jel, a szignál tartalmazza a szinkronizáláshoz szükséges infót

-   Ismertesse az **NRZ-L** (Non-Return to zero) kódolás szabályait!

    | Bit   | Jel      |
    | ----- | -------- |
    | **1** | Magas    |
    | **0** | Alacsony |

    > **Deszinkronizáció**ra hajlamos

-   Ismertesse a **Manchester** kódolás szabályait!

    | Bit   | Jel                 |
    | ----- | ------------------- |
    | **1** | Magasról alacsonyra |
    | **0** | Alacsonyról magasra |

    > **Nincs óraelcsúszás**, de az átvitel felét használja csak ki (két óraidő ciklus kell egy bithez)

    > Példa:

    ```bash
    Bit   │ 0 ┊ 0 ┊ 1 ┊ 1 ┊ 0 │
          │   ┊   ┊   ┊   ┊   │
    Man   │_/¯┊_/¯┊¯\_┊¯\_┊_/¯│
          │   ┊   ┊   ┊   ┊   │
    Clock │_¯_┊_¯_┊_¯_┊_¯_┊_¯_│
    ```

-   Ismertesse az **NRZI** (Non-return to zero inverted)? Mi a fő probléma ezzel a kódolással?

    | Bit   | Jel              |
    | ----- | ---------------- |
    | **1** | Vált             |
    | **0** | Tartja a szintet |

    > A csupa egyes sorozat problémáját megoldja ugyan, de a csupa nulla sorozatot ez sem kezeli

    > Példa:

    ```bash
    Bit   │0┊0┊1┊0┊1┊0┊1┊1┊0┊0│
          │ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ │
    NRZI  │_┊_┊/┊¯┊\┊_┊/┊\┊_┊_│
          │ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ │
    Clock │_┊_┊_┊_┊_┊_┊_┊_┊_┊_│
    ```

-   Ismertesse a **4-bit/5-bit módszer**t. Miért van erre szükség? Hol használjuk?

    > Minden 4 bitet 5 bitbe kódolunk úgy, hogy elején max 1, végén max 2 nulla lehet

    > elkerüli a csupa 0 sorozatokat, ahol az NRZI elcsúszhat.

    > Hátrányok: 20%-os hatékonyságvesztés

-   Mik a főbb tulajdonságai az **alapsávú** (baseband) átvitelnek?

    > a digitális jel direkt árammá vagy fesszé alakul

    > a jel minden frekvencián átvitelre kerül

    > átviteli korlátok

-   Ismertesse a digitális **alapsávú átvitel** struktúráját!

    1. Forrás
    2. Forrás kódolás (forrás bitek)
    3. Csatorna kódolás (csatorna szimbólumok)
    4. Fizikai átvitel
    5. Médium

    -   vissza 4->3->2->1, minden lépés dekódolása

-   Mik a főbb tulajdonságai a **szélessávú** (broadband) átvitelnek?

    > Széles frekitartományban történik az átvitel

    > Jelmodulációs lehetőségek:

    -   **Vivőhullámra ültetés** - amplitúdó moduláció
    -   **Vivőhullám megváltoztatása** - frekvencia vagy fázis moduláció
    -   **Különböző vivőhullámok felhasználása egyidejűleg**

-   Ismertesse a digitális **szélessávú átvitel** struktúráját!

    1. Forrás
    2. Forrás kódolás (forrás bitek)
    3. Csatorna kódolás (csatorna szimbólumok)
    4. Moduláció (Hullámformák véges halmaza)
    5. Fizikai átvitel
       6 . Médium

    -   vissza 5->4->3->2->1, minden lépés dekódolása

-   Mi az **amplitúdó moduláció**?

    > A küldendő **s(t)** szignált a szinuszgörbe amplitúdójaként kódoljuk:

    > **f<sub>A</sub>(t)** = **s(t)** \* sin(2π \* **f** \* **t** + **𝜑**)\
    > **t**: periódus idő\
    > **f**: frekvencia\
    > **A**: amplitúdó\
    > **𝜑**: eltolás

    > Digitális jelnél a szignál erőssége egy diszkrét halmaz értékeinek megfelelően változik (pl.: 0-1)

-   Mi a **frekvencia moduláció**?

    > A küldendő **s(t)** szignált a szinuszgörbe frekvenciájaként kódoljuk:

    > **f<sub>F</sub>(t)** = **a** \* sin(2π \* **s(t)** \* **t** + **𝜑**)\
    > **t**: periódus idő\
    > **f**: frekvencia\
    > **𝜑**: eltolás

-   Mi a **fázis moduláció**?

    > Az **s(t)** szignált a szinuszgörbe fázisában kódoljuk:

    > **f<sub>P</sub>(t)** = **a** \* sin(2π \* **f** \* **t** + **s(t)**)\
    > **t**: periódus idő\
    > **f**: frekvencia\
    > **𝜑**: eltolás

## 3. lecture

-   Ismertesse a **médium többszörös használatának 5 módszerét**!

    -   **Térbeli** multiplexálás (**S**pace-**D**ivision **M**ultiplexing)

        > Külön vezeték vagy antenna

    -   **Frekvencia** multiplexálás (**F**requency-**D**ivision **M**ultiplexing)

        > Több szignál kombinációja adja az átvitelt, minden szignálhoz más frekvencia tartozik

    -   **Hullámhossz** multiplexálás (**W**avelength-**D**ivision **M**ultiplexing)

        > Optikai kábeleknél használt

    -   **Időbeli** multiplexálás (**T**ime-**D**ivision **M**ultiplexing)

        > Jelsorozat időintervallumokra szegmentálása, minden állomás saját időszeletet kap

    -   Kód multiplexálás **CDMA** (**C**ode **D**ivison **M**ultiple **A**ccess)

        > Állomások egyfolytában sugározhatnak a teljes frekvenciasávon

        > Feltételezi, hogy a többszörös jelek lineárisan összeadódnak

        > **Kulcs**: a hasznos jel kiszűrése

-   Mi a **CDMA**? Ismertesse a működési algoritmusát.

    > Minden bitidőt _m_ darab intervallumra osztunk (chip)

    > Minden állomásnak van egy _m_ bites kódja (chip sequence - páronként ortogonálisak)

    > **1**-es bitet akar továbbítani egy állomás: saját töredéksorozatát küldi tovább\
    > **0**-ás bitet akar továbbítani egy állomás: saját töredéksorozatát 1-es komplemensét küldi tovább

-   Mi az a **Walsh mátrix**? Mire használható?

    > Oszlopai vagy sorai meghatároznak egy kölcsönösen ortogonális chipkód halmazt, CDMA multiplexálásra

-   Hogyan áll elő a **H(2<sup>k</sup>)**-nal jelölt Walsh mátrix?

    ```bash
    ┌                     ┐
    │ H(2^k-1),  H(2^k-1) │
    │ H(2^k-1), -H(2^k-1) │
    └                     ┘
    ```

    > Ahol **H(2<sup>1</sup>)** = [[1, 1], [1, -1]]

-   Melyek az **adatkapcsolati réteg** legfontosabb feladatai?

    -   Jól definiált szolgálati interfész a hálózati rétegnek
        -   Nyugtázatlan összeköttetés alapú
        -   Nyugtázott öszeköttetés nélküli
        -   Nyugtázott összeköttetés alapú
    -   Átviteli hibák kezelése
    -   Adatforgalom szabályozása (elárasztás elkerülése)

-   Milyen módszereket ismer a **keretezés**re az adatkapcsolati rétegben?

    > **Bájt alapú**: karakterszámlálás, bájtbeszúrás

    > **Bit alapú**: bitbeszúrás

    > **Óra alapú**: SONET - (**S**ynchronous **O**ptical **Net**work) kódolás

-   Hogyan működik a **karakterszámlálás**?

    > Keret fejlécében megadjuk a keretben lévő karakterek számát

    > Érzékeny a hibára

-   Hogyan működik a **karakterbeszúrás** (bájt beszúrás)?

    > Keret elején végén _FLAG_ byte, + _ESC_ byte

-   Hogyan működik a **bitbeszúrás**?

    > Minden keret speciális bitmintával kezdődik és végződik: _01111110_

    > A küldő az adatban előforduló minden _11111_ részsorozat után berak egy _0_-t, a fogadó majd eltávolítja

-   Hogyan működik az **óra alapú** keretezés (pl. SONET)?

    > STS-1 keretei fix méretűek, 9\*90 bájt, a fogadása után újabb keret kezdő mintázatot kezd keresni

-   Mit tud mondani a bájt beszúrás és a bit beszúrás hatékonyságáról legrosszabb esetben?

    > **Bájtbeszúrás**: 50%, ha minden bájt flagbájt

    > **Bitbeszúrás**: 20% csökk, ha csak 1-esek

-   Mi az egyszerű bithiba definiciója?

    > Az adat **1** bitje **1** helyett **0** lesz vagy fordítva

-   Definiálja a **csoportos bithibát** adott védelmi övezet (_m_) mellett!

    > A fogadott bitek egy olyan folytonos sorozata, amelynek az első és utolsó bitje hibás, és nem létezik ezek közt olyan _m_ hosszú részsorozat, amelyet helyesen fogadtunk volna (_m_ = védelmi övezet)

-   Definiálja egy tetszőleges _S_ kódkönyv **Hamming távolság**át?

    > _S_ kódkönyvben szerepeljenek egyenlő hosszú bitszavak, ekkor S Hamming-távolsága: \
    > d(S) = min { d(x,y) | x!=y eleme S }

-   Mi az a **Hamming korlát**?

    > **C**: kód (_n_ hosszú szavakból)\
    > |**C**| \* szum[i = 0 tól (d(**C**) - 1) / 2] (_n_ alatt i) <= 2<sup>n</sup>

-   Mi a **kódráta** és a **kód távolság**? Milyen a rátája és távolsága egy jó kódkönyvnek?

    > **kódráta**: log<sub>2</sub>|S| / n (hatékonyságot adja meg)
    > **kódtávolság**: d(S) / n (hibakezelési lehetőségeket adja meg)

-   Milyen összefüggés ismeretes egy tetszőleges kódkönyv, a Hamming távolsága és **hibajavitási** képessége között?

    > _d_ bithiba javításához a kódkönyv H-távolsága minimum _2d+1_ legyen

-   Milyen összefüggés ismeretes egy tetszőleges kódkönyv, a Hamming távolsága és **hibafelismerő** képessége között?

    > _d_ bithiba felismeréséhez a kódkönyv H-távolsága minimum _d+1_ legyen

-   Mikor érdemes hibajelző kódot és mikor hibajavító kódot használni?

    > **Hibajelző**: megbízható hálózat (ARQ) - olcsóbb

    > **Hibajavító**: megbízhatatlan hálózat, gyakori hibákkal (FEC) - sok ismétlés elkerülésére

-   Hogyan működik a **Hamming kód** (több paritásos módszer)?

    > **TODO** 3/45

-   Mi a **redundancia** szerepe a hibafelügyeletben?

    > **TODO**

## 4. lecture

-   Mi a **CRC**? Mire használható?

    > **C**yclic **R**edundancy **C**heck, hibajelző kód, bitsorozatokat **Z**<sub>2</sub> feletti polinomok reprezentációjának tekinti

-   Ismertesse a **CRC**-t használó algoritmus 4 lépését!

    1. Legyen G(x) foka r. r darab 0 hozzáfűzése M(x)-hez, így az x<sup>r \* M(x)</sup> lesz
    2. Az ehhez tartozó bitsorozatot elosztjuk a G(x) sorozatával mod 2
    3. x<sup>r \* M(x)</sup>-ből vonjuk ki a **maradékot**, ez lesz T(x), az ellenörző összeggel ellátott, továbbítandó keret.
    4. a vevő T(x) + E(x)-et kapja, ezt elosztja G(x)-szel. ha a maradék, R(x), nem 0, akkor hiba történt

-   Mikor **nem ismeri fel** a hibát a vevő oldal?

    > A G(x) többszöröseinek megfelelő bithibákat nem ismeri fel

-   **CRC** esetén mit lehet mondani **hibajelző képesség**éről, ha a generátor polinom x+1 többszöröse?

    > ezesetben minden páratlan számú hiba felismerhető

-   Mutassa be röviden a **korlátozás nélküli szimplex protokoll**t!

    -   Környezet:

        > Adó és vevő hálózati rétegei mindig készen állnak

        > Feldolgozási idő nincs

        > Végtelen puffer

        > A csatorna hibátlanul továbbít

    -   Protokoll:

        > Nincs sorszám, nyugta
        > Küldő végtelen ciklusban folyamatosan küld
        > Vevő a keret érkezésekor az adatrészt továbbítja a hálózati rétegnek

-   Mutassa be röviden a **szimplex megáll-és-vár protokoll**t!

    -   Környezet:

        > Adó-vevő mindig kész

        > van feldolgozási idő

        > Végtelen puffer

        > Hibátlan csatorna

    -   Protokoll:

        > Küldő egyesével küld, és addig nem küld újat, amíg nem kap nyugtát

        > A vevő várakozik a keretre, ha megjött, adatrészt továbbküldi a hálózati rétegnek, végül nyugtáz

    -   Következmény:

        > fél-duplex csatorna kell (nyugta miatt)

-   Mutassa be röviden a **szimplex protokollt zajos csatorna** esetén!

    -   Környezet:

        > Adó-vevő mindig kész

        > Van feldolgozási idő

        > Végtelen puffer

        > A csatorna hibázhat

    -   Protokoll:

        > A vevő egyesével küld, amíg nem kap nyugtát a határidőn belül; ha ez lejár, újraküld

        > A vevő várakozik, ha megjön, akkor csekkolja az ellenőrző összeget; ha ok, küldi fel, ha nem, eldobja és nem nyugtáz

        > Ha a nyugta elveszik, duplikátum! Megoldás: alternáló bit protokoll (keretek sorszámozása)

-   Mutassa be röviden a **csúszóablak protokoll**t!

    > Egyszerre több keret is küldési állapotban lehet.

    > A fogadó n keretnyi puffert foglal, a küldőnek max ennyi keretet küldhet ki nyugtázatlanul.

    > A keret sorozatbeli pozíciója adja a címkéjét.

    > A fogadó nyugtája tartalmazza a következő várt keret sorszámát (kumulatív nyugta...) A hibás és a nem jó számú kereteket eldobja

    > A küldő nyilvántartja a küldhető sorozatszámokat (adási ablak)
    > A fogadó a fogadható sorszámokat (vételi ablak)

    > Az adási ablak minden küldéssel szűkül, nyugtával nő

-   Mi a **visszalépés N-nel stratégia** lényege?

    > A hibás keret utáni kereteket a fogadó eldobja, és nem is nyugtázza. Az adó a timeout lejárta után újraküldi az összes nyugtázatlan keretet. (1 méretű ablakot tételez fel a fogadó részéről) - nagy sávszél pazarlás, ha sok a hiba

-   Mi a **szelektív ismétléses stratégia** lényege?

    > A hibás keretet a fogadó eldobja, de az utána érkező jókat puffereli. A küldő a timeout után a legrégebbi nyugtázatlan keretet küldi újra.
    > NAK javíthat a hatékonyságon, egynél nagyobb vételi ablak kell

-   Mely 3 dolgot biztosítja a **PPP protokoll**?

    -   Keretezési módszert egyértelmű határokkal
    -   Kapcsolatvezérlő protokollt a vonalak felélesztésére, tesztelésére, az opciók egyeztetésére, és a vonalak elengedésére.
    -   Olyan módot a háózati réteg opcióinak megbeszélésre, amely független az alkalmazott hálózati réteg protokolltól.

-   A **csatorna kiosztás**ra mik a legelterjedtebb módszerek?

    -   Statikus (FDM, TDM)
    -   Dinamikus
    -   Verseny vagy ütközés alapú (ALOHA, CSMA, CSMA/CD)
    -   Verseny-mentes (bittérkép alapú, bináris visszaszámlálás)
    -   Korlátozott verseny (adaptív fabejárás)

-   Röviden mutassa be a **frekvenciaosztásos nyalábolás** módszerét!

    -   N db userhez a sávszélt N egyenlő méretű sávra osztja
    -   Fix számú usernél, nagy forgalomigénynél jó
    -   Löketszerű forgalom esetén problémás

-   Röviden mutassa be az **időosztásos nyalábolás** módszerét!

    -   N db userhez az időegységet N egyenlő méretű időrésre osztja
    -   Löketszerűnél nem jó

-   A csatorna modellben mit nevezünk **ütközés**nek?

    > Ha két keret egyidőben kerül átvitelre, akkor átlapolódnak, és értelmezhetetlenné válnak

-   Írja le a folytonos és a diszkrét időmodell lényegét!

    > **Folytonos**: mindegyik állomás tetszőleges időpontban megkezdheti a kész keretének sugárzását

    > **Diszkrét**: az időt diszkrét résekre osztjuk, sugárzás csak az időrések elején lehetséges. Egy időrés lehet üres, sikeres vagy ütközéses.

-   Mit jelent a **vivőjel érzékelési (Carrier Sensing)** képesség?

    > Az állomások meg tudják vizsgálni a közös csatorna állapotát küldés előtt, hogy foglalt-e vagy szabad. Ha foglalt, addig nem próbálják meg használni. Ha nem rendelkeznek ezzel a képességgel, akkor küldenek, ahogy megvan rá a lehetőségük.

-   Hogyan működik az egyszerű **ALOHA** protokoll?

    > Ha van küldendő adat, akkor a hoszt elküldi.

-   Mit jelent a **keretidő az ALOHA** protokoll esetén?

    > Keretfeldolgozási idő + átviteli késés + propagációs késés (T<sub>f</sub>)

-   Mennyi az Aloha protokoll esetén az **áteresztőképesség** (átvitel) a terhelés függvényében?

    > S(G) = G<sub>a</sub> jó átvitel valószínűsége, azaz 2T<sub>f</sub> idő alatt 0 keretet küldenek = G<sub>P<sub>0</sub>(2T<sub>f</sub>)</sub> = G \* e<sup>-2G</sup>

-   Mit nevezünk **sebezhetőségi idő**nek?

    > Az az időtartam, amely alatt ha másik keret is elküldésre kerül, akkor az aktuális keret sérül.

## 5. lecture

-   Hogyan működik a **réselt ALOHA protokoll**?

    > A csatornát azonos időrésekre bontjuk, egy időrés = T<sub>f</sub>. Átvitel csak az időrések határán lehetséges

    > Algoritmus:\
    > Amikor egy keret küldésre kész, akkor kiküldi a következő időrés határon

-   Mennyi a réselt Aloha protokoll esetén az **áteresztőképesség** a terhelés függvényében?

    > S(G) = G<sub>a</sub> jó átvitel valószínűsége, azaz T<sub>f</sub> idő alatt 0 keretet küldenek \
    > G<sub>P<sub>0</sub>(T<sub>f</sub>)</sub> = G \* e<sup>-G</sup>

-   Hogyan működik az 1-perzisztens **CSMA** protokoll?

    > Folytonos időmodell

    > Küldés előtt belehallgat:

    > Ha foglalt, akkor vár, amíg fel nem szabadul.

    > Ha szabad, küld

    > Ütközéskor véletlen ideig vár, majd újrakezdi a procedúrát

-   Hogyan működik a **nem-perzisztens CSMA** protokoll?

    > Folytonos időmodell

    > Küldés előtt belehallgat:

    > Ha foglalt, akkor véletlen ideig vár, majd újrakezd

    > Ha szabad, küld

    > Ütközéskor véletlen ideig vár, majd újrakezdi a procedúrát

-   Hogyan működik a **p-perzisztens CSMA** protokoll?

    > Diszkrét időmodell

    > Küldés előtt belehallgat:

    > Ha foglalt, akkor a következő időrésig vár, majd újra

    > Ha szabad, akkor p valszegséggel küld. Ha mégse küld, akkor a következő időrésben megint p-vel küld. Ez addig megy, amíg el nem küldi, vagy más nem kezd el küldeni. Ekkor úgy viselkedik, mintha ütközés történt volna.

    > Ütközéskor véletlen ideig vár, majd újra

-   Hogyan működik a **CSMA/CD protokoll**? (CD -> Collision Detection: ütközés érzékelés)

    > Egy CSMA protokoll kiegészítése így:\
    > Minden állomás küldés közben is figyeli a csatornát, ha ütközést tapasztal azonnal
    > megszakítja az adást (nem adja le a teljes keretet), véletlen ideig vár, majd újraküld. Újraküldés során a **binary expontential backoff** módszer alkalmazása

    > Nincs szükség nyugtára, mert az állomások észlelik az ütközést.

-   Mi a **Binary exponential backoff** módszer?

    > Válasszunk [0, 2<sup>n-1</sup>] -ből egyet, ahol n az ütközések száma

    > Ennyi keretidőt várjunk az újraküldésig\
    > n felső határa 10, 16 sikertelen próba után eldobjuk

-   Hogyan működik az **alapvető bittérkép eljárás**?

    > Versengési periódus N időrés, az i-edik hoszt ha küldeni akar, akkor az i-edik időrésben szór egy 1-est
    > A versengési periódus végére mindenki ismeri a küldőket, így sorban küldenek

-   Hogyan működik a **bináris visszaszámlálás protokoll**?

    > Minden állomásnak van azonos hosszú bitsorozat azonosítója, a versengési időben elkezdik bitenként küldeni az azonosítót, ha valaki 0-t küld de 1-et hall vissza a vagyolódás miatt, akkor lemond a küldési szándékáról

    > Mok-Ward módosítása: sikeres átvitel után ciklikusan permutáljuk az állomások címét

-   Mi a **korlátozott versenyes protokollok** célja?

    > Ötvözni a versenyhelyzetes és a versenymentes protokollok jó tulajdonságait

    > Kis terhelés esetén versenyhelyzetes technikát használ a kis késleltetés érdekében, nagy terhelés esetén mellett ütközésmentes technika a csatorna jó kihasználása miatt

-   Hogyan működik az **adaptív fabejárási protokoll**?

    > Állomások bináris fában reprezentálva 0. időrésben mindenki küld

    > Ha ütközés, akkor mélységi bejárás, minden rés egy csomóponthoz van rendelve

    > Ütközés esetén megnézzük a bal és a jobb csomópontot

    > Ha nincs ütközés, akkor a csomópont keresése befejeződik

-   Mi a **repeater** (ismétlő), és mire használják?

    > Analóg eszköz, mely két kábelszegmenshez csatlakozik. Felerősíti a jelet és továbbítja. (fizikai réteg)

-   Mi az **hub** (elosztó) és mire használják?

    > Több bemenettel rendelkezik

    > A beérkező keretet minden vonalon továbbítja

    > Ha két keret egyszerre érkezik, ütközni fognak

    > Általában nem erősíti a jelet (fizikai réteg)

    > Olcsó, egyszerű, kevés tudással rendelkezik

-   Mi a **bridge** (híd), és mire használják?

    > Az adatkapcsolati rétegben működő eszköz, amely LAN-ok összekapcsolását végzi - lekorlátozzák az ütközési tartományok méretet

    > A bejövő keretet csak a megfelelő LAN-hoz továbbítja (forgalomirányítás az adatkapcsolati rétegben).

    > A portok külön ütközési tartományt képeznek és különböző sebességű hálózatokhoz csatlakozhatnak.

    > Pufferelést, csomagfeldolgozást végez, továbbító táblázatot (forwarding table) tart karban. Képest megtanulni a csatlakozó eszközök címét.

-   Mi a **backward learning** (Címek tanulása) lényege?

    > A hidak használják ezt a módszert a keretek továbbításához használt táblázatuk feltöltésére.

    > Ha egy keret érkezik hozzájuk, megnézik a forráscímet (feladót) és "megtanulják", hogy az melyik porton érhető el (ahonnan a keret jött), és ezt bejegyzik a táblázatukba.

-   Ismertesse a **feszítőfa protokoll** (STP) lépéseit?

    1. Az egyik bridge a gyökér
    2. Minden birdge megkeresi a legrövidebb utat hozzá
    3. Ezen utak uniója a feszítőfa

    > A faépítés során a bridgek BPDU-kat (Configuration Bridge Protocol Data Unit-okat) cserélnek

    > Bridge ID, Gyökér ID, költség rendelődik a gyökérhez

    > A fogadása után a bridge választ egy új gyökeret, megjegyzi a felé vezető portot és a következő bridge-t felé

## 6. lecture

-   Mi a **forgalomirányító algoritmusok** definiciója?

    > A hálózati réteg szoftverének azon része, amely eldönti, hogy a bejövő csomag melyik kimeneti vonalon kerüljön továbbításra.

    > táblázatok feltöltése, karbantartása + irányítás

-   Mi a **statikus (nem adaptív) forgalomirányító algoritmusok** fő jellemzője?

    > Offline meghatározza előre a döntéseket, a router indulásakor - nem befolyásolja a topológia és a forgalom változása

-   Mi az **adaptív forgalomirányító algoritmusok** fő jellemzője?

    > A topológia és a forgalom is befolyásolhatja a döntést

-   Mit mond ki az **optimalitási elv** (forgalomirányítás esetén)?

    > Ha J az I->K optimális útvonalon van, akkor J->K optimális útvonal is ugyanerre esik.

    > _Következmény_: az összes forrásból egy célba tartó optimális utak egy nyelőfát alkotnak, aminek a gyökere a cél.

-   Mi a **távolságvektor (distance vector) alapú forgalomirányítás** lényege?

    > A routerek karbantartanak egy táblázatot, amiben minden célhoz szerepel a legrövidebb ismert távolság, és annak a vonalnak az azonosítója, amelyiken a célhoz el lehet jutni. Ezt a táblát a szomszédoktól kapott infók alapján frissítik (a routerek periodikusan elküldik a szomszédaiknak a távolságvektorukat). amikor nem változik semmi már, az algónak vége.

-   Mi az **Elosztott Bellman-Ford algoritmus**?

    > **TODO**

-   Magyarázza el a **végtelenig számolás** problémáját!

    > Ha egy állomás (A) meghibásodik a közvetlen szomszédja (B) észleli, hogy a költség végtelen lett, mert nem érkezik A-tól csomag. B-nek egy szomszédja (C), amelyik korábban B-n keresztül érte el A-t, elküldi A elérési költségét. B azt fogja hinni, hogy C-n keresztül A elérhető, és a C-től kapott költséget megnöveli B-C költséggel, majd ezt küldi vissza C-nek.

    > Ezután mindketten folyamatosan azt fogják hinni, hogy a másikon keresztül A elérhető, és mindenlépésben B-C költséggel növelik A elérési költségét a táblázatukban.

-   Mik a **link-state (kapcsolatállapot) alapú forgalomirányítás** megvalósításának lépései?

    1. szomszédok címének felkutatása: HELLO csomag szórása, a szomszédok válaszolnak a saját címükkel
    2. késleltetés meghatározása: ECHO csomag küldése, a másik oldalnak azonnal vissza kell küldenie - körbeérési idő fele kb a késleltetés
    3. infócsomag összeállítása: feladó azon., sorszám, korérték és a szomszédok listája a késleltetésekkel.
    4. szétküldés elárasztással. a routerek megjegyeznek minden (sorszám,forrás) párt, és csak akkor küldik tovább, ha új
    5. Dijkstra algoritmus lefuttatása ha minden infó megérkezett

-   Hasonlítsa össze a **távolságvektor alapú** és a **link-state (kapcsolatállapot) alapú** forgalomirányítást.

    > Az első esetében a routerek minden más routerre vonatkozó általuk ismert költséget elküldenek, de csak a közvetlen szomszédaiknak, a második esetében csak a szomszédokra vonatkozó ismert költségeket küldik el mindenkinek.

-   Mi a **hierarchikus forgalomirányítás** lényege?

    > Nagy hálózatnál a forgalomirányító táblák arányosan nőnek ezért alkalmazzunk hierarchikus forgalomirányítást:

    > A routereket tartományokra osztjuk. Minden router ismeri a sajátját, de a többi belső szerkezetéről nem tud

    > Többszintű hierarchia is lehetséges:\
    > N routerből álló alhálózathoz optimálisan ln(N) szint kell, amely routerenként e\*ln(N) bejegyzést igényel

-   Mit nevezünk **broadcasting**nak (adatszórásnak)?

    > Egy csomag mindenhová történő egyidejű elküldése

-   Sorolja fel az **adatszórás megvalósítási lehetőségeit**.

    -   Külön csomag küldése minden egyes címzettnek

        > Sávszélt pazarol, lista kell

    -   Elárasztás

        > Kétpontos kommunikációhoz nem megfelelő

    -   többcélú forgalomirányítás (multidestination routing)

        > csomagban van egy lista a rendeltetési helyekről, a router a kimenő vonalakhoz készít egy másolatot, a másolatokba csak a megfelelő célcím listát írja be

    -   Forrás routerhez tartozó nyelőfa használata

        > Ha minden router ismeri, hogy mely vonalai tartoznak a feszfához, akkor csak azokon továbbítja az adatszóró csomagot (kivéve amelyen érkezett)

    -   Visszairányú továbbítás (reverse path forwarding)

        > A router ellenőrzi, hogy azon a vonalon kapta-e meg a csomagot, amelyen rendszerint ő szokott az adatszórás forrásához küldeni. ha igen, akkor valószínűleg a csomag a legjobb utat követte idáig a forrástól, így ez az első csomag, ami megjött, szóval kimásolja minden vonalra.

-   Mit nevezünk **multicastingnak** (többesküldésnek)?

    > Egy csomag meghatározott csoporthoz történő egyidejű elküldése csoportkezelés is kell hozzá:\
    > létrehozás, megszüntetés, csatlakozás, leválasztás a router a bejövő csomagot csak a feszítőfa azon élein küldi tovább, amelyek csoporton beüli hosthoz vezetnek

-   Mire szolgál a **DF bit** az IPv4 fejlécében?

    > Ne darabold, _don't fragment flag_ a routernek\
    > A beérkező datagramot ne darabolja fel

-   Mire szolgál a **MF bit** az IPv4 fejlécében?

    > _More fragment_, jelzi, hogy még az aktuális datagramhoz ez nem az utolsó darab, azaz van még több is. (sorszám)

-   Mire szolgál az **azonosító** (azonosítás) az IPv4 fejlécében?

    > _Datagram azonosítására_ szolgál, egy datagram összes darabja ugyanazt az azonosítót hordozza

-   Mire szolgál a **darabeltolás** (fragment offset) az IPv4 fejlécében?

    > _A darab helyét mutatja_ meg a datagramon belül

-   Mire szolgál az **élettartam** (TTL) mező az IPv4 fejlécében?

    > _Time To Live_, minden ugrásnál eggyel csökkenti a router az értékét, ha eléri a nullát, a csomagot eldobja

-   Mi az **IPv4** cím és hogyan ábrázoljuk?

    > Minden host és router az interneten rendelkezik egy IP címmel, amely a hálózat számát és a hoszt számát kódolja. ez a cím globálisan egyedi 4 bájton ábrázoljuk, leírni bájtonként decimálisan ábrázolva, a bájtokat pontokkal elválasztva szoktuk

-   Milyen **IP cím osztályok**at ismer? Jelemezze ezeket!

    > A: 0, hálózat(1), hoszt(3)\
    > B: 10, hálózat(2), hoszt(2)\
    > C: 110, hálózat(3), hoszt(1)\
    > D: 1110, multicast address\
    > E: 1111, jövőbeni felhasználásra

-   Milyen **speciális IPv4 címek** léteznek?

    -   0...0

        > Az aktuális host

    -   0...0, hoszt

        > Aktuális hálózaton lévő host

    -   1...1

        > Broadcast a helyi hálózaton

    -   hálózat, 1...1

        > Broadcast távoli hálózaton

    -   0111111, bármi (127. ...)

        > Visszacsatolás

-   Mi az **alhálózati maszk** és mire szolgál?

    > **TODO**

## 7. lecture

-   Mi az a **NAT doboz** és mire szolgál?

    > **TODO**

-   Mi az az **MTU** és mire szolgál?

    > **TODO**

-   Hogyan működik az **MTU felderítés**?

    > **TODO**

-   Hogyan ÉS hol történik az **fragmentált/darabolt IP csomagok** helyreállítása?

    > **TODO**

-   Mi az **IPv6** cím és hogyan ábrázoljuk?

    > **TODO**

-   Mi a **localhost IPv6** esetén?

    > **TODO**

-   Soroljon fel két olyan lehetőséget (az EA-on látott 4-ből), melyet **az IPv6 támogat, de az IPv4 esetén nem** találkoztunk vele?

    > **TODO**

-   Mi gátolja az **IPv6-ra való átállás**t?

    > **TODO**

-   Hogyan oldható meg az **IPv6 csomagok átvitele IPv4 hálózat felett**?

    > **TODO**

-   Mire szolgál az **ICMP** protokoll?

    > **TODO**

-   Mi lehet a hatása egy **ICMP forráslefojtás** csomagnak?

    > **TODO**

-   Mire szolgál az **ARP** és hogyan működik?

    > **TODO**

-   Mire szolgál a **RARP** és hogyan működik?

    > **TODO**

-   Mi az a **DHCP** és hogyan működik?

    > **TODO**

-   Milyen lehetőségeket támogat a **DHCP**?

    > **TODO**

-   Mi DHCP esetén a **cím bérlés**?

    > **TODO**

-   Mi az **AS** (Autonóm rendszer)?

    > Az interneten autonóm rendszer (Autonomous System, AS), önálló rendszer vagy útválasztási tartomány (routing domain) IP-hálózatok (IP routing-prefixek) olyan csoportja, melyen belül egyetlen, jól meghatározott útválasztási irányelv (routing policy) érvényesül.

-   Miért van szükségünk **AS**-ekre?

    > **TODO**

-   Mi azonosít egy **AS**-t?

    > **TODO**

-   Milyen routing megoldást/protokollt alakalmaz a **BGP**?

    > **TODO**

-   Hogyan működik az **útvonalvektor protokoll**?

    > **TODO**

-   Mit értünk az alatt, hogy minden AS **saját útválasztási politiká**t alkalmazhat?

    > **TODO**

-   Sorolja fel az **IGP**, **iBGP** és **eBGP** szerepét?

    > **TODO**

-   Mikor mondjuk két AS-ről, hogy azok össze vannak kötve?

    > **TODO**

-   Adjon meg 3 példát **forgalomirányítási korlátozás**ra AS-ek közötti routing esetén.

    > **TODO**

-   Mit nevez a **BGP csonka hálózat**nak?

    > Olyan hálózatok, amelyeknek csak egyetlen összeköttetésük van a BGP gráffal.

-   Mit nevez a **BGP többszörösen bekötött** hálózatnak?

    > Olyan hálózatok, amelyeket használhatna az átmenő forgalom, de ezek ezt megtagadják.

-   Mit nevez a **BGP tranzit hálózat**nak?

    > Olyan hálózatok, amelyek némi megkötéssel, illetve általában fizetség ellenében, készek kezelni harmadik fél csomagjait.

-   Mire szolgál és hogyan működik a **VPN** (virtuális magánhálózat)?

    > **TODO**

## 8. lecture

-   Mire szolgál a **TCP** protokoll? Mik a főbb jellemzői?

    > **TODO**

-   Mire szolgál az **UDP** protokoll? Mik a főbb jellemzői?

    > **TODO**

-   Hogyan történik egy **TCP kapcsolat** felépítése? Mik a lépései?

    > A felépítés 3 TCP csomaggal történik.

    > H1 -> SYN -> H2\
    > H1 <- SYN <- H2\
    > H1 <- ACK <- H2\
    > H1 -> ACK -> H2

-   Hogyan történik egy **TCP kapcsolat lezárása**? Hogyan bomlik le?

    > A küldő jelzi a kapcsolat befejezését egy FIN szegmensben, és vár a szegmens nyugtájára. Az ellenkező irányban továbbra is lehet küldeni. Két félig lezárás zárja le a kapcsolatot.

-   Mit mondhatunk a **TCP átvitel**éről az ablak és az **RTT** függvényében?

    > **TODO**

-   Mit jelent az **RTO**, és hol használják?

    > **TODO**

-   Hogyan történik az **RTT becslés** az eredeti TCP esetén?

    > **TODO**

-   Mit mondhatunk **TCP esetén a hibadetektálás**ról?

    > **TODO**

-   Mi a fogadó által felajánlott **ablakméret** (wnd)?

    > **TODO**

-   Mit jelent, ha a **fogadó wnd=0-át küld**?

    > **TODO**

-   Mit nevezünk **folyamvezérlés**nek?

    > **TODO**

-   Mit nevezünk **torlódásnak TCP esetén**?

    > Ha a terhelés túl nagy, túlcsordulnak a pufferek, csomagok vesznek el, újra kell küldeni, drasztikusan nő a válaszidő. Ezt a torlódásnak nevezzük.

-   Mi a **TCP Nagle** algoritmus működési alapelve?

    > **TODO**

-   Mi a **TCP Karn** algoritmusa? A kapcsolódó problémát is ismertesse!

    > **TODO**

-   Vázolja a **TCP Incast problémá**t!

    > **TODO**

## 9. lecture

-   Mi az a **torlódási ablak**? Mire szolgál?

    > Congestion window, cwnd slow startnál használt második ablak. kezdetben MSS méretű

-   Mi az a **slow start** TCP esetén?

    > Exponenciális növekedés (hisztórikus elnevezés: korábban még aggresszívebb sémák)

-   Mi az **AIMD TCP Tahoe** esetén?

    > **TODO**

-   Mi a gyors újraküldéss **TCP RENO** esetén?

    > **TODO**

-   Mit jelenthet az ha **három nyugta-duplikátum érkezik egymás után**?

    > **TODO**

-   Mi a gyors visszaállítás **TCP Reno** esetén?

    > **TODO**

-   Mivel több a **TCP NewReno**? Mi a problémája az alkalmazott megoldásnak?

    > **TODO**

-   Mi a probléma **nagy késleltetés-sávszélesség szorzatú hálózatok** esetén?

    > **TODO**

-   Mely **TCP variánsok használatosak napjainkban**?

    > **TODO**

-   Hogyan működik a **Compound TCP**?

    > **TODO**

-   Hogyan működik a **CUBIC TCP**?

    > **TODO**

-   Mik a TCP problémái kis folyamok esetén?

    > **TODO**

-   Mik a **TCP problémái vezetéknélküli hálózatok esetén**?

    > **TODO**

-   Mi a **DoS** támadás? Miért probléma ez TCP esetén?

    > **TODO**

## 10. lecture

-   Mit nevezünk **munkamenet**nek az ISO/OSI referencia modellben?

    > Egy munkamenet a egymással összefüggő hálózati interakciók sorozata egy alkalmazási feladat elvégzése során.

-   Mit tud a **DNS** tartománynevek (körzetnevek) rendszeréről?

    > **TODO**

-   Mik azok a **TLD**-k? Adjon meg 4 példát.

    > _Top Level Domain_

    > .com\
    > .edu\
    > .net\
    > .org\

-   Mik azok a **DNS erőforrás rekord**ok? Mit tárolnak (1-2 példa)?

    > **TODO**

-   Mit tud a (DNS) **zónák**ról?

    > **TODO**

-   A névfeloldásnál mit neveznek **iteratív lekérdezés**nek? Mik a jellemzői?

    > Ha a névszerver adja vissza a választ vagy legalább azt, hogy kitől kapható meg a következő válasz.

-   A névfeloldásnál mit neveznek **rekurzív lekérdezés**nek? Mik a jellemzői?

    > Ha a névszerver végzi el a névfeloldást, és tér vissza a válasszal.

-   Írja le a **lokális névszerver**ek legfőbb jellemzőit!

    > **TODO**

-   Mit jelent **DNS esetén a cache**? Mire jó?

    > **TODO**

-   Ismertesse egy **HTML** oldal lekérésének 5 lépését!

    > **TODO**

-   Mit nevezünk **statikus weboldal**nak?

    > A statikus weboldal tartalma nem változik csak manuális átszerkesztéssel.

-   Mit nevezünk **dinamikus weboldal**nak?

    > A dinamikus weboldal valamilyen kód végrehajtásaként keletkezik, mint például: javascript, PHP, vagy mindkettő egyszerre.

-   Mi az a **PLT**? Mit mérünk vele?

    > **TODO**

-   Mik azok a **párhuzamos és perzisztens kapcsolat**ok?

    > **TODO**

-   Hogyan működik a **cache HTTP esetén**?

    > **TODO**

-   Mire jó egy **HTTP proxy**? Hogyan működik?

    > **TODO**

-   Mi a **CDN**? Milyen problémát old meg? Hogyan valsítja ezt meg?

    > **TODO**

-   Mik a **p2p** hálózatok legfontosabb jellemzői?

    > **TODO**

-   Mi a szerepe egy **peer**-nek egy p2p hálózatban?

    > **TODO**

-   Mik egy **torrent** letöltésének lépései (4 lépés)?

    > **TODO**

-   Mit nevezünk **choke peer**-nek?

    > **TODO**

-   Mi az a **seed peer**?

    > **TODO**

# Index Mapping

## Keerukus

### Ruumikomplekssus:

Ruumikomplekssus sõltub 2D-massiivi (koodis nimetatud "array") suurusest, mille suurus on MAX + 1 korda 2 (veerud x read). Seega on ruumikomplekssus O(n).

### Ajaline keerukus:

- Funktsiooni insert ajaline keerukus on O(n)
- Funktsiooni search ajaline keerukus on O(1)

Kogu koodi ajaline keerukus on O(n), kus n on MAX + 1

## Indeksi kaardistamine reaalses maailmas

Esiteks on indeksi kaardistamine kasutusel peogrammeerimiskeeltes, mida kasutatakse erinevate funktsionaalsuste loomiseks kõikides valdkondades. Indeksi kaardistamine võib olla kasulik andmebaasides. Samuti võrguseadmete haldamisel, kus iga seadme kohta võib olla unikaalne id. Operatsioonisüsteemides kasutatakse indeksi kaardistamist, et kaardistada virtuaalsed mäluaadressid füüsilisteks mäluaadressiteks. 
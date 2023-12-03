#  Separate Chaining

## Separate Chaining vs Open Addressing

### Separate Chaining:

- Võtmed on salvestatud nii hash table sisse kui välja
- Võtmete arv hash tables võib olla suurem kui hash table suurus
- Lisaruum on vajalik pointerite jaoks, et salvestada võtmeid väljaspool hash tablet
- Vahemälu "performance" halb linked listi tõttu

Ajaline keerukuss:
- Otsimise keerukus on O(1 + a), kus a = n/m (m - konteinerite arv hash tables, n - võtmete arv)
- Halvimal juhul on otsimise keerukus O(n), mis juhtub kui ahel läheb väga pikaks

Ruumiline keerukus:
- Vajab lisaruumi iga eraldi ahela jaoks

### Open Addressing:

- Võtmed salvestatud ainult hash table sisse
- Võtmete arv hash tables ei saa olla suurem kui hash table suurus
- Lisaruum ei ole vajalik
- Vahemälu "performance" parem kui Separate Chaining puhul, kuna linked list ei ole kasutusel

Ajaline keerukus:
- Eeldatav otsimise ajaline keerukus on O(1), mis on parem kui Separate Chainingu puhul
- Samas halvimal juhul on samuti keerukus O(n)

Ruumiline keerukus:
- Ei vaja täiendavat mälu iga ahela kohta

## Separate Chaining'i plusse ja miinuseid:

Plussid:
- Separate Chaining on lihtne rakendada ja mõista.
- Tuleb toime kokkupõrgetega
- Võib ahelasse lõputult juurde lisada elemente
- Kui ahelad ei ole väga pikad on otsimine kiire

Miinused:
- Kuna võtmed on salvestatud linked listina, ei ole vahemälu "performance" nii hea. Open Addressing võiks pakkuda paremat tulemust selles osas.
- Kasutab lisaruumi linkimiseks
- Ruumi raiskamine, kuna mõned osad hash tabelist pole kunagi kasutatud
- Kui ahel muutub pikaks, siis otsimise keerukus muutub O(n) halvimal juhul

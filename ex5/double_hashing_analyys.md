# Double Hashing

## Ajaline ja ruumiline keerukus 

### Ajaline keerukus

- Mõlemad räsimisfunktsioonid 1 ja 2 on lihtsad, nende keerukus on O(1).
- While tsükliga otsimise keerukus on O(n), kus n on hash tabeli suurus.

### Ruumiline keerukus

Ruumiline keerukus on O(n). Topleträsimisel ei kasutata lisamälu.

## Topelt räsimine efektiivne

Double Hashing on kasulik kokkupõrgetel räsitabelist (kui mitu võtit määravad sama väärtuse). Topelträsimine suurendab  "performancet" ja vähendab kokkupõrkeid. Kuna teine hash funktsioon arvutab offseti, siis on vähem tõenäolisem, et samale kohale tuleb mitu väärtust.

Topelträsimise korral on võtmete hajuvus suurem. Samuti võivad olla mõlemad räsimise funktsioonid erinevad. 
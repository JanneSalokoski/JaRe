# JäRe Tietokanta

Tämä asiakirja dokumentoi JäRen tietokannan rakenteen ja toiminnan.

## Tietokannan tekninen toteutus

Tietokanta on tällä hetkellä Sqlite-tietokanta. Siitä on varmasti jollain aikataululla tarve siirtyä johonkin oikeaan tietokantaan mutta mennään nyt alkuun tällä. `server.py` tarjoaa rajapinnan, joka pysyy samana riippumatta tietokannan toteutuksesta.

## Tietokannan rakenne

Tietokannasta löytyy seuraavat taulut:
- `organisations`
- `org_classes`
- `org_info`
- `actors`

### `organisations`-taulu

Taulu `organisations` sisältää tiedon kaikista järjestöistä, jotka on kirjattu järjestelmään.

Taulu sisältää seuraavat kentät:
- `id`: Järjestön tunniste
- `name`: Järjestön nimi
- `class`: Järjestön luokka
- `accepted`: Milloin järjestö on hyväksytty HYYn piiriin
- `removed`: Milloin järjestö on poistettu HYYn piiristä

### `org_classes`-taulu

Taulu `org_classes` sisältää tiedon olemassaolevista järjestöluokista.

Taulu sisältää seuraavat kentät:
- `class`: Luokan nimi
- `number`: Järjestöluokan tunnistenumero

### `org_info`-taulu

Taulu `org_info` sisältää järjestöjen perustiedot.

Taulu sisältää seuraavat kentät:
- `id`: Järjestön tunniste
- `name`: Järjestön nimi
- `official_name`: Järjestön virallinen nimi
- `abbreviation`: Järjestön lyhenne
- `address`: Postiosoite
- `zip_code`: Postinumero
- `city`: Postitoimipaikka
- `website`: Järjestön verkkosivujen osoite
- `contact_email`: Hallituksen tai puheenjohtajan sähköposti

### `actors`-taulu

Taulu `actors` sisältää tiedot järjestöjen toimijoista

Taulu sisältää seuraavat kentät:
- `role`: Toimijan rooli
- `name`: Toimijan nimi
- `email`: Toimijan säköpostiosoite
- `phone`: Toimijan puhelinnumero


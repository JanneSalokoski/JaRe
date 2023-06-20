# JäRe - projektikartta

Tämä dokumentti pohjustaa, miten JäRen kehitystyötä on tarkoitus tehdä, milloin eri ominaisuuksien on tarkoitus olla valmiita, ja mitä tulevaisuudelta on odotettavissa. Isossa mittakaavassa vakaa versio 1.0. jossa kaikki perustoiminnallisuudet ovat käytettävissä, on tarkoitus saada valmiiksi vuoden 2023 aikana.

## Projektin aikataulu

1. 07/23 - Järjestörekisteri: Perustoiminnallisuus
	- Palvelimen perustoiminnallisuus & tietokanta
	- Käyttöliittymä tietojen lukemiseen ja muuttamiseen

2. 08/23 - Varausjärjestelmä: Alina-sali
	- Palvelimen ominaisuudet varauksiin liittyen
	- Käyttöliittymä Alina-vuorojen jakamiseen

3. 12/23 - Avustustyökalu: Toiminta-avustukset
	- Palvelimen ominaisuudet avustuksiin liittyen
	- Käyttöliittymä avstustusten jakamiseen

4. 2024 - Avustustyökalu: Geneerinen
	- Palvelimen ominaisuudet yleistettävyyteen
	- Käyttöliittymän ominaisuudet jotka mahdollistavat muiden avustusten jakamisen
	- Mallityökalun kehittäminen tukimallien joustavan päivittämisen mahdollistamiseksi

5. 2024 - Varausjärjestelmä: Geneerinen
	- Palvelimen ominaisuudet yleistettävyyteen (synergiaetu aiemmasta)
	- Käyttöliittymän ominaisuudet jotka mahdollistavat varausten toteuttamisen eri spekseillä

6. 24/25 - Palvelelimen refaktorointi
	- Palvelimen refaktorointi Rustilla (koska kaikki pitää kirjottaa uusiksi rustilla), ja koska tässä kohtaa varmasti vanha palvelin tuottaa kiukkua ja harmia. Uusi on myös halvempi, koska Rust on nopeampi. 

Tämä aikataulu on melko suurpiirteinen ja tulee todennäköisesti elämään koska niin se menee, mutta aina on hyvä olla suunitelma niin siitä voidaan sitten poiketa. Tässä suunnitelmassa ei myöskään ole kauhean tarkkaan rajattu sitä, mihinkin osa-alueeseen mikäkin ominaisuus kuuluu, sillä tarkka rakenne niiden osalta ei ole mitenkään varmaa. Monet ominaisuudet myös liittyvät osin toisiinsa. Eri toiminallisuuksien alla määritellään tarkemmin ominaisuuksien kehityspolusta.



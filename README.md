# CampusArt

### Sovelluksen tavoitteet

- Sovelluksessa käyttäjät pystyvät jakamaan opiskelija-aiheisia piirustuksia/taideteoksia, joita he ovat nähneet esim.
  valkotaululla tai liitutaululla.
- Sovellukseen voi luoda tilin ja kirjautua sisään.
- Käyttäjät voivat lisätä, muokata ja poistaa omia julkaisujaan.
- Käyttäjät voivat etsiä julkaisuja hakusanalla tai tagilla.
- Käyttäjät voivat tykätä julkaisuista.
- Käyttäjät voivat kommentoida julkaisuja.
- Julkaisuihin voi liittää tageja, jotka helpottavat julkaisujen löytämistä (esim. #valkotaulu, #piirustus, #vitsit).
- Käyttäjä voi nähdä tilastotietoja omista julkaisuistaan
- Käyttäjä voi selata tykkäämiään julkaisuja

### Nykyinen tilanne
- Rekistöröityminen ja kirjautuminen onnistuu
- Käyttäjä voi lisätä ja poistaa julkaisuja
- Käyttäjä voi selata julkaisuja
- Käyttäjä voi lisätä tai poistaa reaktioita julkaisuihin
- Käyttäjä voi hakea julkaisuja hakusanalla
- Julkaisussa näkee näyttökerrat ja reaktiot

## Sovelluksen asennus

1. Kloonaa tämä repositorio koneellesi
   ```
    git clone 
    ```
2. Asenna riippuvuudet
   ```
   pip install flask
   ```
3. Alusta tiedot tietokantaan
   ```bash
   sqlite3 data.db < schema.sql
   sqlite3 data.db < seed.sql
   ```

## Sovelluksen käynnistäminen

```
flask run
```
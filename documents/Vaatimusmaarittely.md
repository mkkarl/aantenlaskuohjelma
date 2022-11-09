# Vaatimusmäärittely

## Käyttöoikeudet

Käyttäjät voivat tehdä seuraavia asioita

### Admin

- [ ] (voi lisätä käyttäjän)
- [ ] voi antaa tai poistaa adminoikeuksia
- [ ] voi tarkastella kaikkia kokouksia
- [ ] voi tarkastella kaikkia vaaleja
- [x] voi luoda kokouksen
- [ ] voi lisätä kokoukselle virkailijoita

### Käyttäjä

- [x] voi rekisteröityä
- [x] voi kirjautua sisään
- [x] voi kirjautua ulos
- [ ] voi muuttaa salasanansa
- [ ] voi nähdä kokoukset, joihin oikeuksia

### Kokousvirkailija (kokouskohtainen)

- [ ] voi tarkastella kokousta ja sen vaaleja

### Ääntenlaskija (kokouskohtainen)

Samat kuin kokousvirkailijalla sekä

- [ ] voi luoda vaalin
- [ ] voi syöttää OpaVote-äänet
- [ ] voi syöttää paperiäänet
- [ ] voi tarkastaa äänet

## Ääntenlasku

1. Syötä äänet
    * OpaVote-äänet
        - syötä tiedosto
    * Lipukkeet
        - uusi lipuke
        - kirjaa ehdokasjärjestys
        - merkitse lipuke_id lipukkeeseen (tarkistuslaskentaa varten)
        - HUOM! useampi ääntenlaskija voi tehdä yhtäaikaa
2. Tarkista äänimäärä
3. Suorita laskenta ja julkista tulokset
    - tulokset kierroksittain
4. Tee tarkistuslaskenta (esim. seuraavana päivänä)
    - tarkista lipukkeet
    - tarvittaessa suorita laskenta uudestaan
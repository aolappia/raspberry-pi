# Kamera

Kamera asennetaan kameraliitäntään. Ole varovainen ettet riko lattakaapelia tai liitintä.

(kuva inc)

Avaa raspi-config komentoriviltä ajamalla komentoriviltä

```
sudo raspi-cofig
```

Ota käyttöön kamera

(kuva)

Ota valokuva ja video käyttämällä komentoja

```
raspistill -o kuva.jpg
raspivid
```

Tutki komentoja lisää esimerksi komennoilla

```
raspistill --help
raspivid --help
```

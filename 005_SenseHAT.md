# SenseHAT

![](https://aolappia.github.io/raspberry-pi/images/005/Sense-HAT-web.jpg)

SenseHAT on lisämoduuli Raspberry Pi minitietokoneeseen.

SenseHATissa on

- 8×8 RGB LED matrix näyttö
- Gyroskooppi
- Kiihtyvyysanturi
- Magnetometri
- Lämpötila-sensori
- Ilmanpainesensori
- Kosteusensori

Raspbian PIXELissä on oletuksena asennettuna SenseHAT kirjasto, mutta jos jostain syystä ei ole se asennetaan seuraavasti:

```
sudo apt-get update
sudo apt-get install sense-hat
sudo reboot
```

Seuraavana testataan toiminta python koodilla:

```
from sense_hat import SenseHat
sense = SenseHat()
sense.show_message("Hello world!")
```

Tallenna tiedosto nimellä **testi.py** ja aja se.

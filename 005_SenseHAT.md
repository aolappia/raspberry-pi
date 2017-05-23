SenseHAT
========

![](https://aolappia.github.io/raspberry-pi/images/005/Sense-HAT-web.jpg)

SenseHAT on lisämoduuli Raspberry Pi minitietokoneeseen.

SenseHATissa on

-   8×8 RGB LED matrix näyttö

-   Gyroskooppi

-   Kiihtyvyysanturi

-   Magnetometri

-   Lämpötila-sensori

-   Ilmanpainesensori

-   Kosteusensori

Raspbian PIXELissä on oletuksena asennettuna SenseHAT kirjasto, mutta jos
jostain syystä ei ole se asennetaan seuraavasti:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sudo apt-get update
sudo apt-get install sense-hat
sudo reboot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Seuraavana testataan toiminta python koodilla:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sense_hat import SenseHat
sense = SenseHat()
sense.show_message("Hello world!")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tallenna tiedosto nimellä **testi.py** ja aja se.

 

Avaa SenseHAT emulaattori ohjelmointivalikosta.

![](https://aolappia.github.io/raspberry-pi/images/005/2017-05-22_10_03_19.png)

Avautuvasta Sense HAT emulaattorista valitse File \> Open example \> Simple \>
temperature.py

![](https://aolappia.github.io/raspberry-pi/images/005/2017-05-22_10_03_35.png)

Avautuvassa ikkunassa näkyy python koodi jolla senhattia/emulaattoria ohjataan.

![](https://aolappia.github.io/raspberry-pi/images/005/2017-05-22_10_03_41.png)

Valitsle Run \> Run module

![](https://aolappia.github.io/raspberry-pi/images/005/2017-05-22_10_03_48.png)

![](https://aolappia.github.io/raspberry-pi/images/005/2017-05-22_10_04_08.png)

Python shell avautuu ja ohjelma käynnistyy. Nyt voit käyttää sensehatin säädintä
ja tarkkailla sensehatin palautetta ruudulta.

![](https://aolappia.github.io/raspberry-pi/images/005/2017-05-22_10_04_33.png)

Ohjelma suljetaan ottamalla esiin python shell ikkuna ja sulkemalla se. Vastaa
kysymykseen “OK”.

![](https://aolappia.github.io/raspberry-pi/images/005/2017-05-22_10_04_46.png)

Oletuksena esimerkkikoodit ajetaan sensehat emulaattorissa mutta voit vaihtaa
helposti koodin ajettavaksi oikeassa sensehatissa muuttamalla kommenttien
jälkeisen linjan

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sense_emu import SenseHat
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Muotoon

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sense_hat import SenseHat
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

![](https://aolappia.github.io/raspberry-pi/images/005/2017-05-22_10_05_49.png)

![](https://aolappia.github.io/raspberry-pi/images/005/2017-05-22_10_05_59.png)

Kokeile ja muokkaa esimerkkikoodeja ja aja niitä sensehatissasi.

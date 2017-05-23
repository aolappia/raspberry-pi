Kosteus- ja lämpötila-anturi
============================

![](https://aolappia.github.io/raspberry-pi/images/003/IMG_20170516_102914.jpg)

Mukana tulevalla AM2302 sensorilla voi mitata sekä kosteutta että lämpötilaa.
Anturi liitetään Raspberry Pi:n GPIO pinneihin.

![](https://aolappia.github.io/raspberry-pi/images/004/rpi_dht22.jpg)

Pinnit joihin AM2302 kytketään on + pinniin 1 OUT pinnin 7 ja - pinniin 9.

 

Raspberryn GPIO diagrammi alla.

![](https://aolappia.github.io/raspberry-pi/images/004/gpio.jpg)

Python kirjasto löytyy kansiosta 004_kosteus_ja_lampotila_anturi/Adafruit_Python_DHT/
 

 

Siihen pääsee käsiksi avaamalla terminaalin ja vaihtamalla kansioon komennolla

 

![](https://aolappia.github.io/raspberry-pi/images/004/2017-05-22_10_07_05.png)

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cd /home/pi/Downloads/raspberry-pi-master/004_kosteus_ja_lampotila_anturi/Adafruit_Python_DHT  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

![](https://aolappia.github.io/raspberry-pi/images/004/2017-05-22_10_07_13.png)

 

Kirjasto asennetaan seuraavasti  

 

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sudo apt-get update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

![](https://aolappia.github.io/raspberry-pi/images/004/2017-05-22_10_07_31.png)

![](https://aolappia.github.io/raspberry-pi/images/004/2017-05-22_10_07_39.png)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sudo apt-get install build-essential python-dev python-openssl  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

![](https://aolappia.github.io/raspberry-pi/images/004/2017-05-22_10_09_37.png)

Vastaa kysymykseen kyllä eli näppäin k jonka jälkeen enter.

Odota kunnes laite on valmis.

![](https://aolappia.github.io/raspberry-pi/images/004/2017-05-22_10_12_11.png)

`sudo python setup.py install  `

 

Seuraavana testataan sensorin toiminta.  

 

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cd examples  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
chmod +x AdafruitDHT.py  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sudo ./AdafruitDHT.py 2302 4  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

![](https://aolappia.github.io/raspberry-pi/images/004/2017-05-22_10_15_37.png)

 

Nyt sinun pitäisi nähdä ruudulla kosteus ja lämpötila arvot sensorilta.  

 

Testaa sensorin toimintaa lisää puhaltamalla kosteaa ilmaa sensoriin ja aja komento uudestaan.
 

 

Tutki koodia ja selvitä miten se toimii.  

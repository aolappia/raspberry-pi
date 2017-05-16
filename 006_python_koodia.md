Python koodia
=============

[5kertaa.py](006_python_koodia/5kertaa.py) tulostaa nimesi 5 kertaa

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tee ohjelma joka printtaa nimesi 5 kertaa.
for i in range(5):
        print("nimesi")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

[2numeroa.py](006_python_koodia/2numeroa.py) pyytää kahta numeroa ja laskee ne
yhteen

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tee ohjelma, joka kysyy kaksi lukua.
# Ohjelman tulee laskea luvut yhteen.

num1 = eval(input('Anna ensimmäinen numero: '))
num2 = eval(input('Anna toinen numero: '))

# Muutetaan numerot lennossa tyypille float ja lisätään yhteen, muodosaen muuttuja sum
sum = float(num1) + float(num2)

# Näytetään laskettu summa (sum)
print('Lukujen {0} ja {1} summa on {2}'.format(num1, num2, sum))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

[bday.py](006_python_koodia/bday.py) kysyy käyttäjältä syntymäpäivän ja vuoden.
Tämän jälkeen kertoo käyttäjän iän.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tee ohjelma, joka kysyy syntymävuotesi ja laskee sen perusteella ikäsi.

from datetime import datetime

my_date = input("Anna syntymäpäiväsi muodossa pp.kk.vvvv format: ")

b_date = datetime.strptime(my_date, '%d.%m.%Y')

print("Ikä: %d" % ((datetime.today() - b_date).days/365))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

[km2miles.py](006_python_koodia/km2miles.py) muuttaa kilometrit maileiksi

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ohjelma joka muuttaa kilometrit maileiksi.

# vihjataan pythonille muuttujien tyyppejä
mailit = float()
kilometrit = float()
muuntokerroin = float()

# Kilometrit
kilometrit = eval(input("Kuinka monta kilometriä: "))

# muunnoskerroin
muuntokerroin = 0.621371

# laske mailit
mailit = float(kilometrit * float(muuntokerroin))

# anna ulostulo
print('%0.3f kilometeriä vastaa %0.3f mailia' %(kilometrit,mailit))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

[euro2usd.py](006_python_koodia/euro2usd.py) muuttaa eurot dollareiksi

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ohjelma joka muuttaa eurot usan dollareiksi. 
# valuuttakurssi katsottu googlesta kirjoitushetkellä
# 1 euro to usd

# vihjataan pythonille muuttujien tyyppejä
usd = float()
euro = float()
muuntokurssi = float()

# Kilometrit
euro = eval(input("Euromäärä: "))

# muunnoskerroin
muuntokurssi = 1.1071

# laske mailit
usd = float(euro * float(muuntokurssi))

# anna ulostulo
print('%0.3f euroa on %0.3f dollaria' %(euro,usd))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

[numeronarvauspeli.py](006_python_koodia/numeronarvauspeli.py) arvuuttaa
numeroa, kunnes arvataan oikein

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# numeronarvauspeli

import random

# pienin luku
min = 1

# suurin luku
max = 10

# Arvotaan salainen numero
salainen_numero = random.randint(min, max)

# haastetaan pelaaja
print("Yritä arvata numero. Arvausalue on", min, "-", max)

# ensimmäinen kysymys
arvaus = int(eval(input("Arvaa numero: ")))

# otetaan silmukassa niin kauan kunnes arvataan oikein
# tässä täytyy huomata, että sisennyksillä on tärkeä rooli
while arvaus != salainen_numero:
        # jos arvaus on liian suuri, mainitaan siitä
        if arvaus > salainen_numero:
                print(arvaus, "on liian suuri.")
        #jos arvaus on liian pieni, mainitaan siitä
        if arvaus < salainen_numero:
                print(arvaus, "on liian pieni.")
        # pyydetään arvaamaan uudelleen
        arvaus = int(eval(input("Arvaa uudelleen: ")))
# arvaus oli oikein
print(arvaus, "oli oikea numero! Onneksi olkoon!")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

[korttipeli.py](006_python_koodia/korttipeli.py) on yksinkertainen korttipeli,
jossa pelaajalla ei ole vaikuttamisen mahdollisuutta

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# korttipeli

import random
# määritellään maat. Pelissä ne ovat vain tunnelmaa luomassa
maat = ["risti", "ruutu", "hertta", "pata"]

# määritellään arvot korteille. Pitkiä rivejä voi jakaa.
arvot = ["kakkonen", "kolmonen", "nelonen", "viitonen", 
		"kuutonen", "seiska", "kasi", "ysi", "kymppi", "jätkä", 
		"kuningas", "ässä"]

# määritellään arvo, joka päättää looppaako ohjelma
jatka = True

# itse pelin looppi
while jatka:
		# arvotaan tietokoneelle kortin arvo
        cpu_arvo = random.choice(arvot)

		# arvotaan tietokoneelle kortin maa
        cpu_maa = random.choice(maat)

		# arvotaan pelaajalle kortin arvo
        pelaaja_arvo = random.choice(arvot)

		# arvotaan pelaajalle kortin maa
        pelaaja_maa = random.choice(maat)

		# kerrotaan pelin tilanne
        print("Minulla on %s%s" %(cpu_maa, cpu_arvo))
        print("Sinulla on %s%s" %(pelaaja_maa, pelaaja_arvo))
		
		# tarkistetaan, onko korttien arvot (käyttäen arvojen indeksinumeroa)
		# ja kerrotaan kumpi voitti vai oliko tasapeli
        if arvot.index(cpu_arvo) > arvot.index(pelaaja_arvo):
                print("Minä voitin!")
        elif arvot.index(cpu_arvo) < arvot.index(pelaaja_arvo):
                print("Sinä voitit!")
        else:
                print("Tasapeli!")
		
		# huijataan pelaajaa kirjoittamaan jotain, jos peli päättyy
		# oikeasti minkä tahansa kirjoittaminen lopettaa
        vastaus = input("Pelkkä enter jatkaa. q lopettaa: ")
		
		# jatka saa muun arvon, jos pelaaja kirjoitti jotain 
		# ja while silmukan True vaihtuu (ja lopettaa pelin)
        jatka = (vastaus == "")

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

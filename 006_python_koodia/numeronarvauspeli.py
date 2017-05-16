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

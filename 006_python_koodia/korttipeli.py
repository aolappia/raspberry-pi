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


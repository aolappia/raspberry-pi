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

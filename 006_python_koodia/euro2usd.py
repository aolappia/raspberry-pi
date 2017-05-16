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

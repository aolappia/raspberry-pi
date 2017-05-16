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

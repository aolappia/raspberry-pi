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

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tee ohjelma, joka kysyy syntymävuotesi ja laskee sen perusteella ikäsi.

from datetime import datetime

my_date = input("Anna syntymäpäiväsi muodossa pp.kk.vvvv format: ")

b_date = datetime.strptime(my_date, '%d.%m.%Y')

print("Ikä: %d" % ((datetime.today() - b_date).days/365))

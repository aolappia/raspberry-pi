# Tee ohjelma, joka kysyy syntymavuotesi ja laskee sen perusteella ikasi.

from datetime import datetime

my_date = raw_input("Enter B'date in dd/mm/yyyy format:")

b_date = datetime.strptime(my_date, '%d/%m/%Y')

print "Age : %d" % ((datetime.today() - b_date).days/365)

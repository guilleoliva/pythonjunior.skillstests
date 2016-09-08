import sys
from re import findall
Path=sys.argv[1]
#print Path
archivo = open(Path, 'r' )
linea1 = archivo.readline()
print linea1
datos = linea1.split(' ')
#print datos	
#print len(datos)
consonantes = "bcdfghjklmnpqrstvxz"
nc = 0
for n in range(len(datos)):
    nc = len(findall('[%s]' % consonantes, datos[n]))   
    if nc > 2:
  		print(datos[n])	
    nc = 0


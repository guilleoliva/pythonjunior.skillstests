import sys
from re import findall
cant=int(sys.argv[1])
print (cant)
for n in range(cant-1, -1, -1):
   print ((2 * n + 1) * "*").center(2 *cant + 1)

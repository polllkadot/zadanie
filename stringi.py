zdanie = ("q->p^p=r")
lista_spójników = ['=', '->', '^', 'v']

for i in range(len(zdanie)):
 if lista_spójników[i]:
  zdanie.remove(lista_spójników[i])
 else:
  break

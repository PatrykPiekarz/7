#podaj sciezke do folderu
#wyswietl informacje - ilosc plikow, rozmiar plikow, ilosc folderow, rozmiar folderow, rozmiar calosciowy folderu
#przelicz na kilobajty i megabajty

from os import *
x=0
x=float(x)
sci=[]
ilep=[]
ilek=[]
rozmp=[]
rozmk=[]
for sciezka,podkatalogi,pliki in walk('./NUCLEARTESTZONE'):
    sci.append(sciezka)
    ilep.append(len(pliki))
    ilek.append(len(podkatalogi))
    rozmp.append(sum(path.getsize(path.join(sciezka,nazwa)) for nazwa in pliki))
    rozmk.append(sum(path.getsize(path.join(sciezka,nazwa)) for nazwa in pliki))
    print 'W katalogu %s znajduje sie %i plikow, w sumie posiadaja one %i bajtow. Istnieje tutaj %i katalogow o lacznym rozmiarze %i bajtow' \
    % (sciezka,len(pliki),sum(path.getsize(path.join(sciezka,nazwa)) for nazwa in pliki),len(podkatalogi),0)
    x+=sum(path.getsize(path.join(sciezka,nazwa))
                    for nazwa in pliki)


print "rozmiar calosciowy folderu %s to %i bajtow, czyli %f kilobajtow, czyli %f megabajtow." % ('NUCLEARTESTZONE',x,x/1024,x/1048576)

#operacje na plikach i katalogach

from os import *

#sprawdzenie w jakim aktualnie katalogu jestesmy
print getcwd()

#zmiana biezacego katalogu na inny
#chdir('Test')
print getcwd()

#zawartosc katalogu
print listdir('..')

#zawartosc katalogu - sciezka absolutna
print listdir(r'/home/piotr/PycharmProjects/Skrypty')

#filtrowanie plikow i katalogw wg okreslonego wzorca

import fnmatch
print fnmatch.fnmatch('Python','P*n')
print fnmatch.fnmatch('Python','P*e')

#lista plikow z rozszerzeniem py
print [x for x in listdir(r'/home/piotr/PycharmProjects/Skrypty') if fnmatch.fnmatch(x,'*.py')]

#lista plikow konczone na 6 lub l
print [x for x in listdir(r'/home/piotr/PycharmProjects/Skrypty') if fnmatch.fnmatch(x,'*[6l].*')]

import glob
for x in glob.glob(r'/home/piotr/PycharmProjects/Skrypty*[6l].*'):
    print x

#rozdzielenie sciezki absolutnej na katalog w ktorym znajduje sie plik oraz nazwa pliku
print path.split('/home/piotr/PycharmProjects/Skrypty/script25.py')

for x in glob.glob(r'../*[6l].*'):
    print path.split(x)[1]

#laczenie ciagu katalogow w sciezke
print path.join('/','home','piotr','PycharmProjects','Skrypty','script25.py')
print path.join(r'/home/piotr','PycharmProjects','Skrypty/script25.py')

#sprawdzenie czy sciezka jest absolutna
print path.isabs(r'../script25.py')
print path.isabs(r'/home/piotr/PycharmProjects/Skrypty/script25.py')

#sprawdzenie czy dany obiekt dyskowy istnieje
print path.exists(r'/home/piotr/PycharmProjects/Skrypty/script25.py')
print path.exists(r'/home/piotr/PycharmProjects/Skrypty1')

#zmiana nazwy katalogu lub pliku
#rename('../Test','../nTest')
print path.exists('nTest')
print listdir('.')

#sprawdzenie czy dany obiekt dyskowy jest plikiem
print path.isfile('nTest')
print path.isfile("script25.py")

#sprawdzenie czy dany obiekt dyskowy jest katalogiem
print path.isdir('nTest')
print path.isdir("script25.py")

#sprawdzenie czy dany obiekt dyskowy jest dyskiem
print path.ismount('nTest')
print path.ismount('/home')

#sprawdzenie dlugosci pliku w bajtach
print path.getsize('nTest')
print path.getsize("script25.py")

for x in listdir('.'):
    print x,path.getsize(x)

#czas stworzenia pliku
from time import ctime
print ctime(path.getctime('script25.py'))

#czas modyfikacji pliku
from time import ctime
print ctime(path.getmtime('script25.py'))

#rekursywne przechodzenie katalogow
for sciezka,podkatalogi,pliki in walk(r'./'):
    print 'W katalogu %s znajduje sie %i bajtow w %i plikach' \
    % (sciezka,sum(path.getsize(path.join(sciezka,nazwa))
                    for nazwa in pliki),len(pliki))
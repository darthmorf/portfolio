from os import listdir
from os.path import isfile, join
mypath = "./"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in onlyfiles:
    print('<a href="'+file+'" data-ngthumb="'+file+'" data-ngdesc="">'+file+'</a>')

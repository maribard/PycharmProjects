import os
import re

'''f = open('practise.txt', 'w+')
f.write('This is a test string')
f.close()

print(os.listdir('C:/Users/'))'''

import shutil

shutil.unpack_archive('unzip_me_for_instructions.zip', 'final_unzip', 'zip' )
s = '\\final_unzip'
lista = []
#print(s)
#print(os.getcwd() + s)
for folder, sub_folder, files in os.walk(os.getcwd()+ s):
    print(f"{folder}")

    for f in files:
        print(f"{f}".format(f))
        file = open(folder + '\\' + f, 'r')
        for line in file:
            if re.search("\d\d\d-\d\d\d-\d\d\d\d", line):
                print("True")
                lista.append(re.search("\d\d\d-\d\d\d-\d\d\d", line))
                print(lista)

                for r in lista:
                    if r != '':
                        print( r.group() )

from typing import TextIO

try:
    f = open('versions.txt', 'r')
    print(f.readline())
except:
    print("Exeptions")
finally:
    f.close()

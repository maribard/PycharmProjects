# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""
import re

file = open('file', 'r')

text = file.read()


string = "!@#%$^*&r%h#"
#wyraz = re.findall()
comments = re.findall("<!--([\w\n]*?)-->", string)
print(comments)
"""
import urllib.request
import re
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
data = re.findall("<!--(.*)-->", html, re.DOTALL)[-1]
potencjalne = re.findall("[A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z]", data)

lista_stringow = data.split()
print(potencjalne)
print(len(lista_stringow))
slowko = "SJFzWSG"
i = 1
for a in potencjalne:

    i = 1
    #print(a)
    while i < 1250:
        if a in lista_stringow[i]:
            #print("success1")
            result = lista_stringow[i].index(a)
            if re.match("[^A-Z]", lista_stringow[i][result -1]) and re.match("[^A-Z]", lista_stringow[i][result + 7]):
                #print("success")
                print(a)
        i += 1

"""
i = 0
tekst = []

while i < len(szryft):
    if szryft[i] == "." or szryft[i] == " " or szryft[i] == "(" or szryft[i] == ")" or szryft[i] == "'":
        tekst.append(szryft[i])
        i += 1
    elif szryft[i] == 'x':
            tekst.append('z')
            i += 1
    elif szryft[i] == 'y':
            tekst.append('a')
            i += 1
    elif szryft[i] == 'z':
            tekst.append('b')
            i += 1
    else:
        cyferka = ord(szryft[i]) + 2
        literka = chr(cyferka)
        tekst.append(literka)
        i += 1

my_lst_str = ''.join(map(str, tekst))
print(my_lst_str)
"""


szryft ="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
alfabet1 = "abcdefghijklmnopqrstuvwxyz"
alfabet2 = "cdefghijklmnopqrstuvwxyzab"
cos = szryft.maketrans(alfabet1, alfabet2)
print(cos)
print(len(alfabet1))
print("map".translate(cos))
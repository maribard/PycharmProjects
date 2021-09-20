moj_string = "7316717653133062491922511967442657474235534" \
             + "919493496983520312774506326239578318016984801869478851843" \
             + "85861560789112949495459501737958331952853208805511" \
             + "12540698747158523863050715693290963295227443043557" \
             + "66896648950445244523161731856403098711121722383113" \
             + "62229893423380308135336276614282806444486645238749" \
             + "30358907296290491560440772390713810515859307960866" \
             + "70172427121883998797908792274921901699720888093776" \
             + "65727333001053367881220235421809751254540594752243" \
             + "52584907711670556013604839586446706324415722155397" \
             + "53697817977846174064955149290862569321978468622482" \
             + "83972241375657056057490261407972968652414535100474" \
             + "82166370484403199890008895243450658541227588666881" \
             + "16427171479924442928230863465674813919123162824586" \
             + "17866458359124566529476545682848912883142607690042" \
             + "24219022671055626321111109370544217506941658960408" \
             + "07198403850962455444362981230987879927244284909188" \
             + "84580156166097919133875499200524063689912560717606" \
             + "05886116467109405077541002256983155200055935729725" \
             + "71636269561882670428252483600823257530420752963450"

dlugosc_stringa = len(moj_string)
a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
g = 6
h = 7
j = 8
k = 9
l = 10
m = 11
n = 12
najw_liczba = 0
while d != dlugosc_stringa - 1:
    if int(moj_string[a]) * int(moj_string[b]) * int(moj_string[c]) * int(moj_string[d]) \
            * int(moj_string[e]) * int(moj_string[f]) * int(moj_string[g]) * int(moj_string[h]) \
            * int(moj_string[j]) * int(moj_string[k]) * int(moj_string[l]) * int(moj_string[m]) \
            * int(moj_string[n]) > najw_liczba:
        najw_liczba = int(moj_string[a]) * int(moj_string[b]) * int(moj_string[c]) * int(moj_string[d]) \
                      * int(moj_string[e]) * int(moj_string[f]) * int(moj_string[g]) * int(moj_string[h]) \
                      * int(moj_string[j]) * int(moj_string[k]) * int(moj_string[l]) * int(moj_string[m]) \
                      * int(moj_string[n])
        print(moj_string[a] + moj_string[b] + moj_string[c] + moj_string[d] + moj_string[e] + moj_string[f]\
              + moj_string[g] + moj_string[h] + moj_string[j] + moj_string[k] + moj_string[l] + moj_string[m]\
              + moj_string[n] + "  Mnożenie:  " + str(najw_liczba))
    b += 1
    a += 1
    c += 1
    d += 1
    e += 1
    f += 1
    g += 1
    h += 1
    j += 1
    k += 1
    l += 1
    m += 1
    n += 1
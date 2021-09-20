
file = open('tekstplik.txt', "r")
import re

text = file.read()
print("".join(re.findall("[A-Za-z]", text)))

znaki = []
# iterate through each character
for char in text:
    if char not in znaki:
        znaki.append(char)

print(znaki)


def letterFrequency(fileName, letter):
    # open file in read mode
    file = open(fileName, "r")

    # store content of the file in a variable
    text = file.read()

    # declare count variable
    count = 0

    # iterate through each character
    for char in text:

        # compare each character with
        # the given letter
        if char == letter:
            count += 1

    # return letter count
    return count


for a in znaki:
    print(a + " wystepuje " + str(letterFrequency('tekstplik.txt', a)) + " razy")
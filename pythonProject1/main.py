# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


i = 1
suma = 0
while i < 1000:
  if i % 3 == 0:
    suma += i
  elif i % 5 == i % 3:
    i += 1
    continue
  else:
    if i % 5 == 0:
      suma += i
  i += 1

print("Suma to: " + str(suma))
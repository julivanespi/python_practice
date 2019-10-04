# below will show show break and continue looks like

word="python"

for letter in word:
    print(letter)
    if(letter=='t'):
        break

print("First part is done")

for letter in word:
    if(letter=='t'):
        continue
    print(letter)

print("Second part is done")
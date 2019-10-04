# this will show a simple example with nested while loops

i=0
j=0
while(i<5):
    print("Going through main loop {} times".format(i))
    i += 1
    while(j<5):
        print("Going through nested loop {} times".format(j))
        j += 1
    j = 0
    
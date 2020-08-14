i = 0
while i < 96:
    print("%5d - %s" % (i + 32, chr(i + 32)), end=' ')
    i += 1
    if i % 10 == 0:
        print()

print()

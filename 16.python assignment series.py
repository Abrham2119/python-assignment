a = float(0)
for i in range(99):
    if i%2 != 0 and i<100:
        a = a + i/(i+2)
print(a)
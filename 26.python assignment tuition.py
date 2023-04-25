tuition = 10000
counter = 0
four_yrs = 0
while True:
    tuition = tuition + (5*tuition/100)
    counter += 1
    if counter <= 4:
        four_yrs += tuition
    elif counter == 10:
        break
print(tuition,four_yrs)
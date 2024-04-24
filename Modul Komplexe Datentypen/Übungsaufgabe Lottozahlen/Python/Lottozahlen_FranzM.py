import random

ziehung=[]
rate=[]

def getrandomint(ziehung):
    x = random.randint(1, 24)
    return getrandomint(ziehung) if x in ziehung else x

for i in range(6): ziehung.append(getrandomint(ziehung))

for i in range(6): rate.append(int(input(f"Bitte die {i} Nummer raten: ")))

richtige_array=[]

for i in rate:
    if i in ziehung:
        richtige_array.append(i)
        break

print(len(richtige_array), "richtige.")
print("Richtige:", richtige_array)
print("Geratene: ", rate)
print("Ziehung: ", ziehung)
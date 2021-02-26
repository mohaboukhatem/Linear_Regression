tab = []
tab.append("1")
tab.append("1")
i =0

while i < 13 : 

    val = int(tab[-1]) + int(tab[-2])
    tab.append(val)
    i+=1

print(tab)
nb = int(input("donner nb : "))
nb +=1
for i in range(1,nb) :
    a = i*13
    if a % 7 == 0 :
        print(a)

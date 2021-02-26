tab,tab1 = [],[]
dicto = {}

def classer(nb):
    if nb < 0 :
        
        tab.append(nb)
        dicto['negative']= tab

    else : 

        tab1.append(nb)
        dicto['positive']= tab1
    return dicto

n = 0

for i in range(4): 
    
    a = int(input("donner le nb : "))
    sol=classer(a)
print(sol)
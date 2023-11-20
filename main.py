f = open('test.txt','r')
kumpulanpda = []
for i in f:
    kalimat = i
    kalimat = i.split("\n")
    for j in range(len(kalimat)) :
        kata = kalimat[j].split(";")
        if len(kata) > 1 :
            pda = []    
            for k in range(len(kata)) :
                pda.append(kata[k])
    kumpulanpda.append(pda)
print(kumpulanpda) 


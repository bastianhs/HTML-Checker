from bs4 import BeautifulSoup
with open("E:\\TBFO\\HTML-Checker\\tes.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    test = soup.prettify()
    komponenhtml = test.split("\n")

if komponenhtml[0] == "<!DOCTYPE html>" :
    komponenhtml.pop(0)
    
print(komponenhtml)
alltag = []
for i in range(len(komponenhtml)) :
    array = [0,0,0,0,0]
    angka = 0
    tags= []
    tag = ""
    isiparam = ""
    while angka < len(komponenhtml[i]) :
        while komponenhtml[i][angka] == " " :
            angka += 1
        if komponenhtml[i][angka] == "<" :
            tag += komponenhtml[i][angka]
            angka += 1 
            tags.append(tag)
            tag = ""
        elif komponenhtml[i][angka] == ">":
            tag += komponenhtml[i][angka]
            angka += 1
            tags.append(tag)
            tag = ""
        else :
            while angka < len(komponenhtml[i])-1 and komponenhtml[i][angka] != " " and komponenhtml[i][angka] != "=" and komponenhtml[i][angka] != ">":
                tag += komponenhtml[i][angka]
                angka += 1
            if komponenhtml[i][angka] == "=" :
                tag += komponenhtml[i][angka]
                while komponenhtml[i][angka] == " " :
                    angka += 1
                angka += 1
                if komponenhtml[i][angka] == '"' :
                    tag += komponenhtml[i][angka]
                    angka += 1
                while komponenhtml[i][angka] != '"' and angka < len(komponenhtml[i])-1 :
                    isiparam += komponenhtml[i][angka]
                    angka += 1
                if komponenhtml[i][angka] == '"' :
                    tag += komponenhtml[i][angka]
                    angka += 1
                tags.append(tag)
                tags.append(isiparam)
            elif komponenhtml[i][angka] == ">" :
                angka = angka
                tags.append(tag)
            else :
                tag += komponenhtml[i][angka]
                angka += 1
                tags.append(tag)
            tag = ""
            isiparam = ""
    alltag.append(tags)


print(alltag)
            
            
        # else :
        #     while angka < len(komponenhtml[i])  
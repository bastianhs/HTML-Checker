komponenhtml = []
with open('HTML-Checker\\tes.html', 'r') as file:
    # Baca file
    content = file.read()
    strFile = content
    komponenhtml.append(strFile)
komponenhtml = komponenhtml[0].split("\n")

if (komponenhtml[0] == "<!DOCTYPE html>") :
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
            if komponenhtml[i][angka] == "!" and komponenhtml[i][angka+1] == "-" and komponenhtml[i][angka+2] == "-" :
                tag += komponenhtml[i][angka]
                tag += komponenhtml[i][angka+1]
                tag += komponenhtml[i][angka+2]
                angka += 3
            tags.append(tag)
            tag = ""
        elif komponenhtml[i][angka] == ">":
            tag += komponenhtml[i][angka]
            angka += 1
            tags.append(tag)
            tag = ""
        else :
            while angka < len(komponenhtml[i])-1 and komponenhtml[i][angka] != " " and komponenhtml[i][angka] != "=" and komponenhtml[i][angka] != ">" and komponenhtml[i][angka] != "-":
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
            elif komponenhtml[i][angka] == "-" :
                print("OK")
                if komponenhtml[i][angka+1] == "-" and komponenhtml[i][angka+2] == ">" :
                    tags.append(tag)
                    tag = ""
                    tag += komponenhtml[i][angka]
                    tag += komponenhtml[i][angka+1]
                    tag += komponenhtml[i][angka+2]
                    angka += 3
                    print("OK2")
                    print(tag)
                tags.append(tag)
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
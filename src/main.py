# Fungsi-Fungsi yang dibutuhkan untuk pemrosesan PDA
def Top(stack):
# mengembalikan elemen puncak dari stack
    return stack[len(stack)-1]

def Split_String(string):
# memisahkan string yang terdapat spasi di dalamnya menjadi beberapa string
    list_of_string = []
    temp = ''
    for i in range(len(string)):
        if string[i] != ' ':
            temp += string[i]
        else:
            list_of_string.append(temp)
            temp = ''
    list_of_string.append(temp)
    return list_of_string

def Transisi(stack, rule):
# melakukan proses perubahan pada stack berdasarkan rule yang diberikan
    proses_stack = Split_String(rule[4])
    
    if (len(proses_stack) == 1 and proses_stack[0] != 'epsilon'):
        if (Top(stack) != proses_stack[0]):         # top stack perlu diganti dengan proses stack
            stack[len(stack)-1] = proses_stack[0]
    elif (len(proses_stack) == 1 and proses_stack[0] == 'epsilon'): # top stack perlu dihapus
        stack.pop()
    else:   # len(proses_stack) = 2
        stack.append(proses_stack[0]) # stack perlu ditambah dengan proses stack, top stack yang lama tidak dihapus
    
    return stack

# Fungsi-Fungsi yang dibutuhkan untuk parsing dan tokenisasi
def parsing_space(tag):
# memisahkan spasi yang terdapat setelah tag
    hasil = []

    for i in range(len(tag)):
        if ' ' in tag[i]:
            newstr = tag[i].replace(' ', "")
            hasil.append(newstr)
            hasil.append(' ')
        else:
            hasil.append(tag[i])

    return hasil

def isAllBlankSpace(string):
# mengecek apakah string yang diberikan hanya berisi spasi atau kosong
    if string == '':
        return True
    for i in range(len(string)):
        if string[i] != " ":
            return False
    return True

def delete_last_space(string):
# menghapus semua spasi di akhir string
    if (string != ''):
        while ((len(string) > 0) and (string[len(string)-1] == ' ')):
            string = string[:-1]
    return string

def tokenisasi_atribut(tag):
# Menghapus beberapa parameter atribut yang tidak memedulikan nilai parameternya (atribut global, rel, href, scr, alt, action)
# Menggabungkan atribut dan parameter yang nilainya diperhatikan (type, method)
# Mengubah tokenisasi class="", id="", style="" menjadi atribut_global
    hasil = []
    i = 0
    while i < (len(tag)):
        if ((tag[i] == 'class=""') or (tag[i] == 'id=""') or (tag[i] == 'style=""')):   # menghapus bagian parameter yang tidak diperhatikan
            hasil.append('atribut_global')
            i += 2
        elif ((tag[i] == 'rel=""') or (tag[i] == 'href=""') or (tag[i] == 'src=""') or (tag[i] == 'alt=""') or (tag[i] == 'action=""')):  # menghapus bagian parameter yang tidak diperhatikan
            hasil.append(tag[i])
            i += 2
        elif ((tag[i] == 'type=""') or (tag[i]) == 'method=""'):    # menggabungkan atribut dan parameter yang nilainya diperhatikan
            newstr = ''
            j = 0
            while tag[i][j] != '"':
                newstr += tag[i][j]
                j += 1
            newstr += '"'
            newstr += tag[i+1]
            newstr += '"'
            hasil.append(newstr)
            i += 2
        else:       # bukan atribut
            hasil.append(tag[i])
            i += 1

    return hasil

""" ******************** Meminta inputan nama file ******************** """
FILE_PDA = input("Silahkan masukkan nama file PDA: ")
FILE_HTML = input("Silahkan masukkan nama file HTML: ")

""" ******************** Membaca file PDA.txt ******************** """
f = open(FILE_PDA,'r')
Rule_of_PDA = []

for i in range(38):         # mengabaikan 38 baris pertama
    rule = f.readline()

rule = f.readline()
while rule != '.':          # mengambil rule dari file PDA
    if rule == '\n':
        rule = f.readline()

    kalimat = rule.split("\n")
    for j in range(len(kalimat)) :
        kata = kalimat[j].split(";")
        if len(kata) > 1 :
            pda = []    
            for k in range(len(kata)) :
                pda.append(kata[k])
    Rule_of_PDA.append(pda)
    rule = f.readline()

f.close()

""" ******************** Membaca file HTML ******************** """
komponenhtml = []
with open("../test/" + FILE_HTML, 'r') as file:          # Baca file
    content = file.read()
    strFile = content
    komponenhtml.append(strFile)
komponenhtml = komponenhtml[0].split("\n")

current_line = 1
if (komponenhtml[0] == "<!DOCTYPE html>") :
    komponenhtml.pop(0)
    current_line += 1
alltag = []

list_of_X_location = []             # menyimpan lokasi currentline setiap kali X dipush ke stack
list_of_X = []                      # menyimpan semua input yang menyebabkan X dipush ke stack
current_condition = ['','','']      # menyimpan kondisi saat ini (state, input, top stack)
stack = ['Z0']                      # start stack
current_state = 'HTML'              # start state
current_token = ''                  # menyimpan input saat ini

is_in_rule = False
isSesudahTag = False

for i in range(len(komponenhtml)):
    angka = 0
    tags= []
    tag = ""
    isiParam = ""
    komponenhtml[i] = delete_last_space(komponenhtml[i])

    """ ***** proses tokenisasi per line ***** """
    while (angka < len(komponenhtml[i])) and (not isAllBlankSpace(komponenhtml[i])):
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
            if komponenhtml[i][angka] == ' ':
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
            while angka < len(komponenhtml[i])-1 and komponenhtml[i][angka] != " " and komponenhtml[i][angka] != "=" and komponenhtml[i][angka] != ">" and komponenhtml[i][angka] != "-" and komponenhtml[i][angka] != "<":
                tag += komponenhtml[i][angka]
                angka += 1
            if komponenhtml[i][angka] == "=" :
                tag += komponenhtml[i][angka]
                while komponenhtml[i][angka] == " ":
                    angka += 1
                angka += 1
                if komponenhtml[i][angka] == '"' :
                    tag += komponenhtml[i][angka]
                    angka += 1
                while komponenhtml[i][angka] != '"' and angka < len(komponenhtml[i])-1 :
                    isiParam += komponenhtml[i][angka]
                    angka += 1
                if komponenhtml[i][angka] == '"' :
                    tag += komponenhtml[i][angka]
                    angka += 1
                tags.append(tag)
                tags.append(isiParam)
            elif komponenhtml[i][angka] == "-" :
                if komponenhtml[i][angka+1] == "-" and komponenhtml[i][angka+2] == ">" :
                    tags.append(tag)
                    tag = ""
                    tag += komponenhtml[i][angka]
                    tag += komponenhtml[i][angka+1]
                    tag += komponenhtml[i][angka+2]
                    angka += 3
                else:
                    tag += komponenhtml[i][angka]
                    angka += 1
                tags.append(tag)
            elif komponenhtml[i][angka] == ">" :
                angka = angka
                tags.append(tag)
            elif komponenhtml[i][angka] == "<" and komponenhtml[i][angka+1] == "/" :
                tags.append(tag)
                tag = ""
                tag += "<"
                angka += 1
                tags.append(tag)
                tag = ""
            else :
                tag += komponenhtml[i][angka]
                angka += 1
                tags.append(tag)
            tag = ""
            isiParam = ""
    tags = parsing_space(tags)
    tags = tokenisasi_atribut(tags)

    for j in range(len(tags)):
        """ ***** proses tokenisasi per input simbol ***** """
        if isSesudahTag & (tags[j] != '<') & (tags[j] != '>') & (tags[j] != '<!--') & (tags[j] != '-->'):
        # mengubah string apapun yang berada diantara tag menjadi SIGMA (semua string yang berada diantara tag merupakan anggota Σ*)
            current_condition[0] = current_state
            current_condition[1] = 'SIGMA'
            current_condition[2] = Top(stack)
        else:
            current_condition[0] = current_state
            current_condition[1] = tags[j]
            current_condition[2] = Top(stack)

        """ ***** proses pengecekan ke dalam PDA untuk setiap input simbol ***** """
        for k in Rule_of_PDA:
            if current_condition[0] == k[0] and current_condition[1] == k[1] and current_condition[2] == k[2]:
                is_in_rule = True
                break
        
        # print(current_condition[1])
        if is_in_rule:
            stack = Transisi(stack, k)
            current_state = k[3]
            if (current_condition[1] == '>'):
                isSesudahTag = True
            if (current_condition[1] == '<'):
                isSesudahTag = False
            current_token = ''
            is_in_rule = False
            if Top(stack) == 'X':
                list_of_X_location.append(current_line)
                list_of_X.append(current_condition[1])
        else:
            stack.append('X')
            list_of_X_location.append(current_line)
            list_of_X.append(current_condition[1])
        # print(stack)
    current_line += 1

if (stack == ['Z0']):
    print("Valid")
else:
    print("Tidak Valid")
    print("Terdapat kesalahan pada line:", list_of_X_location[0])
    print("Kesalahan:", list_of_X[0])
a = [("HTML", "html", "<", "HTML", "html <"), ("HTML", "<", "Z0", "HTML", "< Z0")]
b = "html"
c = "head"

for i in a:
    if b in i:
        print("yes")
        break
    
print(i)
import time as t
a = "NİLDA NE OLURSUN ÇOK YORULDUM BIRAK YATAYIM LOO"
b= [" ","A","B","C","Ç","D","E","F","G","H","I","İ","J","K","L","M","N""","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
z=""
for i in a:
    for j in b:
        print(z, end=(""))
        print(j)
        if i == j:
            z+=j
            break
        print("\033c", end="")
        t.sleep(0.02)

# I just bored, ı need this basic thing and I had time
def kisi():
    lis=[]
    a=int(input("Kaç Kişi Gezdiniz: "))
    for i in range(a):
        b=input("{}. kişi: ".format(i+1))
        lis.append(b)
    return lis

def para(l):
    mo=[]
    for i in l:
        b=float(input("{} Ne kadar harcadı: ".format(i)))
        mo.append(b)
    return mo

def main():
    Bakiye=[]
    isim=kisi()
    harcanan=para(isim)
    s=sum(harcanan)/len(isim) #money for every people 
    for i in range(len(isim)):
        Bakiye.append(harcanan[i]-s)

    for borclu in range(len(isim)):
        if Bakiye[borclu]<0:
            for alacak in range(len(isim)):
                if alacak==borclu:
                    continue
                if Bakiye[alacak]>0:
                    d=Bakiye[borclu]
                    f=Bakiye[alacak]
                    if (d*-1)>f:
                        d+=f
                        print("{}----> {}, {} TL verecek".format(isim[borclu],isim[alacak],f))
                        Bakiye[borclu]=d
                        Bakiye[alacak]=0
                    else:
                        f+=d
                        Bakiye[borclu]=0
                        Bakiye[alacak]=f
                        print("{}----> {}, {} TL verecek".format(isim[borclu],isim[alacak],d*-1))
                        print("{} tüm borcunu verdi borcu kalmadı".format(isim[borclu]))
                        break
            print("------------------------------")
                

    print("---------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx---------------")

    
""" for list not sure
    for i in range(len(isim)):
        print("--------------------------------")
        if Bakiye[i]>0:
            print(isim[i],Bakiye[i]," TL Alacak")
        elif Bakiye[i]==0:
            print(isim[i]," Tam ödeme yapmış alacak verecek yok")
        else:
            print(isim[i],Bakiye[i]*-1," TL Verecek")
    print("--------------------------------")
"""

if __name__=="__main__":
    while True:
        main()
        if "q"==input("Tekrar için enter çıkış için q"):
            break







# I just bored, I need this basic thing and I had time
def hesap():
    try:
        lis=[]
        a=int(input("Kaç Kişi Gezdiniz: "))
        for i in range(a):
            b=input("{}. kişi: ".format(i+1))
            c=float(input(f"{b} ne kadar harcama yaptı: "))
            lis.append({"isim":b,
                        "harcama" : c,
                        "bakiye":0})
        return lis
    except:
        print("lüfen kişi sayısını ve mikktarları doğru formatta giriniz :)")
#isim, ödenen, bakiye
def main():
    bilgi=hesap()
    if len(bilgi)==0:
        print("gezi yok, perogram sonlandırılıyor...")
    else:
        s=sum(i["harcama"] for i in bilgi)/len(bilgi) #money for every people 
        for i in bilgi:
            i["bakiye"] = i["harcama"]-s
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        for borclu in bilgi:
            if borclu["bakiye"]<0:
                print("--------------------------------------------")
                for alacak in bilgi:
                    if alacak==borclu:continue
                    if alacak["bakiye"]>0:
                        borc_bakiye=borclu["bakiye"]
                        alacak_bakiye=alacak["bakiye"]
                        if (borc_bakiye*-1)>alacak_bakiye:
                            borc_bakiye+=alacak_bakiye
                            print("{}----> {}, {} TL verecek".format(borclu["isim"],alacak["isim"],alacak_bakiye))
                            borclu["bakiye"]=borc_bakiye
                            alacak["bakiye"]=0
                        else:
                            alacak_bakiye+=borc_bakiye
                            borclu["bakiye"]=0
                            alacak["bakiye"]=alacak_bakiye
                            print("{}----> {}, {} TL verecek".format(borclu["isim"],alacak["isim"],borc_bakiye*-1))
                            print("{} tüm borcunu verdi borcu kalmadı".format(borclu["isim"]))
                            break

if __name__=="__main__":
    while True:
        main()
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        if "q"==input("Tekrar için enter çıkış için q"):
            break







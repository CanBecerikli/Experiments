import random, time
while True:
    print("************TOMBALAYA HOŞGELDİNİZ********")
    def kutu(ad,maho):
        import random
        sayı=[]
        for i in range(1,maho+1):
            sayı.append(i)
        ad=[]
        a=0
        while a<=14:
            t=random.choice(sayı)
            ad.append(t)
            sayı.remove(t)
            a+=1
        return ad
    torba=[]
    d=int(input("kaç sayıyla tombala oynamak istersiniz: "))
    for i in range(1,d+1):
            torba.append(i)
    sayı=[]
    kartlar=[]
    ks=int(input("kişi sayısı: "))
    for i in range(1,ks+1):
        isim=input("oyuncu {} adı: ".format(i))
        sayı.append(isim)
    t=0
    for i in range(0,ks):
        i=kutu(sayı[i],d)
        print(sayı[t],"oyuncusunun kartı: ",i)
        t+=1
        kartlar.append(i)
    k=0
    print("\nkartların mevcut durumu için: kart\n\nTorbada kalan sayılar için: torba")
    while True:
        for i in range(0,ks):
                if len(kartlar[i])<=3:
                    print(sayı[i]," oyuncusunun kazanması için sadece {} sayı kaldı".format(len(kartlar[i])))
                    time.sleep(1)
        r=input("\nSayı Çek: ")
        if r=="kart":
            print("\n")
            for i in range(0,ks):
                print(sayı[i],"oyuncusunun kartı: ",kartlar[i])
        elif r=="torba":
            print("\n")
            print(torba)
        else:
            print("\n")
            f=random.choice(torba)
            torba.remove(f)
            ğ=0
            for i in range(ks):
                if f in kartlar[i]:
                    kartlar[i].remove(f)
                    print(f)
                    time.sleep(0.5)
                    print(sayı[i],"oyuncusu {} sayısına sahip. Bravoo!!!!!!".format(f))
                else:
                    ğ+=1
            if ğ==ks:
                print("{} sayısı kimsede yok :(".format(f))
            for i in range(ks):
                if kartlar[i]==[]:
                    print("VE KAZANAN!!!!!!")
                    time.sleep(0.3)
                    print("...")
                    time.sleep(0.3)
                    print("...")
                    time.sleep(0.3)
                    print("...")
                    time.sleep(0.3)
                    print("BRAVOOOOOOOOO",sayı[i],"KAZANDIIIIIIIIII\n","{} ".format(sayı[i])*999)
                    k=2
        if k==2:
            break
    time.sleep(4)
    input("tekrar oynamak için herhnagi bir tuş: ")
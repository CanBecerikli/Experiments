import random,time
class tel():
    def __init__(self,pil=100,parlaklık=50,şifre=1234,uy=["ayarlar","google"]):
        self.pil=pil
        self.parlaklık=parlaklık
        self.uygulamalar=uy
        self.şifre=şifre
        
        
    def __str__(self):
        return "şarjı: {}\nparlaklığı: {}\nuygulamalar: {}\nşifre: {}".format(self.pil,self.parlaklık,self.uygulamalar,self.şifre)       
                  
    def şarj(self):
        if self.pil==100:
            print("şarj tam dolu")
        else:
            print(self.pil)
            print("şarj ediliyor...")
            time.sleep(2)
            print("şarj edildi")
            self.pil+=10
            print("şarj = ",self.pil)
        
        
    def ekran(self):
        while True:
            print("====ekran parlaklığı: {}====".format(self.parlaklık),)
            a=input("parlaklığı arttırmak için : +\nazaltmak için: -\nçıkmak için: çıkış\n  =  ")
            if a=="+":
                if self.parlaklık==100:
                    print("\n======daha fazla arttırılamaz=====\n")
                    continue
                self.parlaklık+=10
            elif a=="-":
                if self.parlaklık==0:
                    print("\n====daha fazla azaltılamaz ====\n")
                    continue
                self.parlaklık-=10
            elif a=="çıkış":
                break


    def kilit(self):
        print("mevcut şifre: ",self.şifre)
        f=input("şifre değiştirmek için: 1\nçıkmak için: ç\n: ")
        if f=="ç":
            print("çıkış yapılıyor...")
        elif f=="1":
            h=5
            k=0
            for i in range(6):
                if k==1:
                    break
                mev=int(input("mevcut şifre: "))
                if mev == self.şifre:
                    while True:
                        y=int(input("yeni şifre: "))
                        t=int(input("yeni şifre tekrar: "))
                        if t==y:
                            k=1
                            self.şifre=y
                            print("şifreniz {} olarak güncellendi".format(self.şifre))
                            break
                        else:
                            print("şifreler uyumlu değil")
                else:
                    print("şifre hatalı lütfen tekrar deneyiniz kalan deneme sayısı: ",h-1)
                    h-=1
                
    def len(self):
        return len(self.uygulamalar)

iphone=tel()
print("""
      
      1.pil gücü öğrenme
      
      2.parlaklık işlemleri
      
      3.uygulama işlemleri
      
      4.şifre ve güvenlik
      
      5.rastgele uygulama açma
      
      6.cihaz durumu
      
      """)
input("açmak için herhangi bir tuş: ")
while iphone.pil!=0:
    işlem=input("\nişlem: ")
    if işlem=="1":
        iphone.şarj()
        continue
        
    elif işlem=="2":
        iphone.ekran()
        
    elif işlem=="3":
        print("\neklemek için: ekle\nsilmek için: sil\nçıkış için: ")
        while True:
            print("uygulama sayısı: ",iphone.len(),"\nuygulamalar: ",iphone.uygulamalar)
            s=input("uygulama işlemi: ")
            if s=="ekle":
                uygadı=input("eklenecek uygulamalar ',' bırakılarak yazılsın: ")
                us=uygadı.split(",")
                for ı in us:
                    iphone.uygulamalar.append(ı)
                    print(ı,"uygulaması eklendi")
                    time.sleep(0.5)
            elif s=="sil":
                p=input("silinecek uygulamalar ',' : ")
                su=p.split(",")
                for i in su: 
                    iphone.uygulamalar.remove(i)
                    print(i,"uyglaması silindi")
                    time.sleep(0.5)
            else:
                break
    elif işlem=="4":
        iphone.kilit()
    elif işlem=="5":
        print(random.choice(iphone.uygulamalar))
    elif işlem=="6":
        print(iphone)
        continue
    else:
        print("lütfen geçerli bir işlem giriniz")
    
    iphone.pil-=10
print("şarj = 0 \ncihaz kapanıyor...")
time.sleep(4)
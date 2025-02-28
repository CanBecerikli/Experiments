def main():
    birler=["","Bir","iki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
    onlar=["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
    yüzler=["","yüz","ikiyüz","Üçyüz","Dörtyüz","Beşyüz","Altıyüz","Yediyüz","Sekizyüz","Dokuzyüz"]
    canımsıkıldı = [
    "",
    "",
    "",
    "bin",
    "milyon",
    "milyar",
    "trilyon",
    "katrilyon",
    "kentilyon",
    "sekstilyon",
    "septilyon",
    "oktilyon",
    "nonilyon",
    "desilyon",
    "andesilyon",
    "dodesilyon",
    "tredesilyon",
    "katordesilyon",
    "kendesilyon",
    "seksdesilyon",
    "septendesilyon",
    "oktodesilyon",
    "novemdesilyon",
    "vicintilyon",
    "anvicintilyon",
    "dovicintilyon",
    "trevicintilyon",
    "katorvicintilyon",
    "kenkavicintilyon",
    "sesvicintilyon",
    "septemvicintilyon",
    "oktovicintilyon",
    "novemvicintilyon",
    "tricintilyon",
    "antricintilyon",
    ]
    
    def read(li):
        if len(li)==3:
            return yüzler[int(li[2])]+" "+onlar[int(li[1])]+" "+birler[int(li[0])]
        elif len(li)==2:
            return onlar[int(li[1])] + " " + birler[int(li[0])]
        elif len(li)==1:
            return birler[int(li[0])]
    def control(grup,küme=""):
        try:
            if grup[1]=="0" and grup[2]=="0" and grup[0]=="0":
                return ""
            else:
                return read(grup) +" "+ küme
        except:
            return read(grup) +" "+ küme
    while True:
        try:
            h=input("sayı: ")
            li = []
            for i in h:
                li.append(i)
            li == li.reverse()
            lo=[]
            u=[]
            a=2
            for i in li:
                if len(u)==3:
                    lo.append(control(u,canımsıkıldı[a]))
                    u=[]
                    a+=1
                u.append(i)
            lo.append(control(u,canımsıkıldı[a]))
            lo==lo.reverse()
            r=""
            for i in lo:
                r+=i
                r+=" "
            print(r)
        except IndexError:
            print("Henüz bu basamakta bir sayıyı okuyamıyorum, Lütfen abartmayın")
        except ValueError:
            print("yazdığın sayının içinde 'sayı' olmayan bir şeyler var. Onları düzelt tekrar yaz")

if __name__ == "__main__":
    main()
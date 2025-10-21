import os

def bul(dizin):
    textler = []  # txt dosyalarını burada toplayacağız
    try:
        for i in os.listdir(dizin):
            tam_yol = os.path.join(dizin, i)

            if i.endswith(".txt"):
                textler.append(tam_yol) # txt dosyasını listeye ekliyoruz (eğer yol olarak eklemek isterseniz *tam_yol* değişkenini ekleyebilirsiniz)

            elif os.path.isdir(tam_yol):
                textler.extend(bul(tam_yol))  # Recursive olarak alt klasörleri de tarıyoruz

    except Exception as e:
        print(f"Hata oluştu: {e}")
    return textler

def main():
    b = "C:\Program Files"  # Ana dizini belirle (r: raw string), (dilediğiniz bir dizin olabilir, dilerseniz tüm diskleri tarayabilirsiniz)  
    a=bul(b)
    print("########################-------BULUNAN-DOSYALAR---------##############################")
    for i in a: # .txt dosyalarını bul
        print("------------")
        print(i)

if __name__ == "__main__":
    main()  # Sadece doğrudan çalıştırıldığında çalışsın (import edilince çalışmasın)

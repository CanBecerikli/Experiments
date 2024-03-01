import math
print("toplama için 1\nçıkarma 2\nçarpma 3\nbölme 4\nsonuç için enter")
print("İşlem önceliği yoktur yazdığınız tüm işlemler soldan sağa doğru uygulanacaktır")
işlem=[]
def okuma(küme):
    for i in küme:
        print(i, end=" ")
while True:
    a=int(input("\nsayı: "))
    işlem.append(a)
    while True:
        b=input("\nişlem: ")
        if b=="1":
            işlem.append("+")
            okuma(işlem)
            t=int(input("\nsayı 2: "))
            a+=t   
            işlem.append(t)
        elif b=="2":
            işlem.append("-")
            okuma(işlem)
            t=int(input("\nsayı 2: "))
            a-=t   
            işlem.append(t)
        elif b=="3":
            işlem.append("*")
            okuma(işlem)
            t=int(input("\nsayı 2: "))
            a*=t   
            işlem.append(t)
        elif b=="4":
            işlem.append("/")
            okuma(işlem)
            t=int(input("\nsayı 2: "))
            a/=t   
            işlem.append(t)
        elif b=="":
            print("\nsonuç: ",a)
            break
        okuma(işlem)

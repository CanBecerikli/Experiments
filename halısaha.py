import random
def dağıtım(power,g1,g2):
    import random
    while True:
        if power==[]:
            break
        if len(g2)>len(g1):
            f=random.choice(power)
            g1.append(str(f))
            power.remove(f) 
        elif len(g1)>len(g2):
            f=random.choice(power)
            g2.append(str(f))
            power.remove(f) 
        if power==[]:
            break          
        f=random.choice(power)
        g1.append(f)
        power.remove(f)
        if power!=[]:
            f=random.choice(power)
            g2.append(str(f))
            power.remove(f)      

def main():
    while True:
            on=["Messi","Ronaldo","Fenomeno","Neymar"]
            dokuz=["Khan","casillas"]
            sekiz=["De bruyne","Özil","Müllere","maldini"]
            yedi=["Alex","Haigi","Kaka","Pirlo"]
            altı=["Arda güler","arda turna"]
            beş=["abdulekro","yavuz","gökhan","emre"]
            dört=["aliko.","dursun"]
            üç=[]
            iki=[]
            bir=[]
            takım1=[]
            takım2=[]
            input("\n\ntekrarla: ")
            dağıtım(on,takım1,takım2)
            dağıtım(dokuz,takım1,takım2)
            dağıtım(sekiz,takım1,takım2)
            dağıtım(yedi,takım1,takım2)
            dağıtım(altı,takım1,takım2)
            dağıtım(beş,takım1,takım2)
            dağıtım(dört,takım1,takım2)
            dağıtım(üç,takım1,takım2)
            dağıtım(iki,takım1,takım2)
            dağıtım(bir,takım1,takım2)
            print("\n",takım1,"\n",takım2)         

if __name__ == "__main__":
    main()
def yaz(test):
    for i in test:
            for j in i:
                print(j,end=" ")
            print()
    print("\n\n")

def rule(sud,sat,sut,sayi):
    if sayi in sud[sat]:
        return False
    for j in range(0,9):
        if sayi == sud[j][sut]:
            return False
    a=sat%3
    b=sut%3
    for j in range(3):
        if sayi==sud[sat-a][sut-b+j] or sayi==sud[sat-a+j][sut-b+1] or sayi == sud[sat-a+j][sut-b+2]:
            return False
    return True

def at(sud,i=0,j=0):
    lo=[]
    for sayi in range(1,10):
        if rule(sud,i,j,sayi):
            lo.append(sayi)
    if len(lo)==1:
        sud[i][j]=lo[0]
    return de(i,j,sud)

def de(sat,sut,sud):
    sut+=1
    if sut==9:
        sat+=1
        sut=0
        if sat==9:
            for i in range(9):
                for j in range(9):
                    if sud[i][j]==0:
                        return at(sud,i,j)
            
            print("ÇÖZÜLDÜÜÜÜÜÜÜÜÜ")

            return yaz(sud)
        if sud[sat][sut]==0:
            return at(sud,sat,sut)
        else:
            return de(sat,sut,sud)
    if sud[sat][sut]==0:
        return at(sud,sat,sut)
    else:
        return de(sat,sut,sud)
        

def main():

    sud=[[0,3,6,0,5,0,7,9,8],
         [0,4,0,0,3,7,0,2,0],
         [2,0,0,8,0,1,0,0,6],
         [0,8,0,7,0,0,2,5,0],
         [3,0,4,0,2,0,8,0,0],
         [0,0,5,1,0,3,0,0,4],
         [5,1,0,0,7,6,4,0,0],
         [6,0,2,0,0,0,0,8,1],
         [0,0,0,5,0,8,0,7,0]]
    yaz(sud)


    de(0,-1,sud)

if __name__=="__main__":
    main()
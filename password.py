import random
a = input("DO You Want to generate password ? (YES/NO)")
dect = {}
A = ["1","2","3","4","5","6","7","8","9","0"]
B = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","K","L","Z","X","C","V","B","N","M"]
C = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","l","z","x","c","v","b","n","m"]
D = ["qM","wN","eB","rV","tC","yX","uZ","iL","oK","pJ","aH","sG","dF","fD","gS","hA","jP","kO","lI","lU","zY","xR","cE","vT","bW","nE","mQ"]
E = ["!","@","#","$","%","^","&","*","(",")","-","=","+"]
six = random.choice(A)+random.choice(B)+random.choice(C)+random.choice(D)+random.choice(E)
seven = random.choice(A)+random.choice(B)+random.choice(C)+random.choice(D)+random.choice(E)+random.choice(A)
eight = random.choice(A)+random.choice(B)+random.choice(C)+random.choice(D)+random.choice(E)+random.choice(B)+random.choice(E)
if a.upper() == "YES":
    x1 = input("For Which website ?")
    p1 = input("How many letters/numbers password is required (6/7/8)")
    if p1 == "6" :
        print(six)
    elif p1 == "7":
        print(seven)
    elif p1 == "8":
        print(eight)
    else :
        print("ONLY 6-8")
    s = input("Do you want to store this password")
    if s.upper() == "YES":
        if p1 == "6":
            dect[x1]=six
            print(dect)
        elif p1 == "7":
            dect[x1]=seven
            print(dect)
        elif p1 == "8":
            dect[x1]=eight
            print(dect)
    else :
        print("Thank You Visit Again")
else :
    print("Wheneever you need we are here !!")
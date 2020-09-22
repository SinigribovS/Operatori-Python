n=int(input("Numar natural mai mic ca 10000: "))
if (n<10000):
    print("ultima cifra este",n%10)
    print("penultima cifra este",n//10%10)
    print("catul impartirii la 9 este",n//9)
    print("restul impartirii la 9 este",n%9)
    a=n//1000
    b=n//100%10
    c=n//10%10
    d=n%10
    print("suma cifrelor=",a+b+c+d)
    print("rasturnatul numarului este ",d,c,b,a,sep="")
else:
    print("""Eroare: numarul natural introdus e mai mare ca 10000. 
Introduceti un numar mai mic ca 10000 si repetati executia programului.""") 


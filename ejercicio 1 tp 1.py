def estricto(a,b,c):
    mayor=c
    if a>b:
        if a!=b: 
            if a!=c:
                if a>c:
                    mayor=a
    elif b!=c:
        if b>c:
            mayor=b
    else:
        mayor="No existe mayor estricto"
    return mayor

num1=int(input("num1: "))
while (num1) <= 0:        
    num1=int(input("num1: "))
num2=int(input("num2: "))
while (num2) <= 0:        
    num2=int(input("num2: "))
num3=int(input("num3: "))
while (num3) <= 0:        
    num3=int(input("num3: "))

print(estricto(num1,num2,num3))

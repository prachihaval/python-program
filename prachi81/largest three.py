a =int(input("enter first number: "))
b =int(input("enter second number: "))
c =int(input("enter thrid number: "))

if a>b: 
    if a>c:
        print(a,"is largest number")
        print("other are smaller num")
    else:
         print(c,"is largest number")
else:
    if b>c:
            print(b,"is largest number")
    else:
             print(c,"is largest number")
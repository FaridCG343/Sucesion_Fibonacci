def fibonacci(n, x=1, y=1):
    if n > 0:
        print(x)
        z=x+y
        x=y
        y=z
        fibonacci(n-1,x,y)
    else:
        print("Se terminó la susecion usando finciones =D")


fibonacci(20)
x = 1
y = 1
for i in range(20):
    z = x+y
    print(x)
    x = y
    y = z
else:
    print("Se terminó la sucesion usando for =D")


n = 20
f=(pow(1+pow(5,1/2),n)- pow(1-pow(5,1/2),n))/(pow(2,n)*pow(5,1/2))
print(f)

x=int(input("Ingrese un número entre 1 y 8 "))

while(x<1 or x>8):
    print("Ingrese un número entero entre 1 y 8 ")
    x=int(input("Ingrese un número entre 1 y 8 "))

for i in range(1,x+1,1):
    print(" "*(x+1-i)+"#"*i)
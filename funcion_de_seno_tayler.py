x = float(input("Ingrese el valor de x en radianes: "))

for n in range(1, 10):  # 10 términos para aproximar
    fact = 1
    for k in range(1, 2*n+2):
        fact = fact * k
    termino = ((-1)**n) * (x**(2*n+1)) / fact
    
  
print("Seno aproximado:", termino)
print("Seno en grados: ", termino * (180/3.1416))
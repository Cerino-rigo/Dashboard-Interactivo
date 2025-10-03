print("Hola de nuevo, este es un repositorio creado desde Github")

print("Hola de regreso")

a = 89
b = 52
c = 23

def suma():
    print("Suma total: ", a + b + c)

suma()

import matplotlib.pyplot as plt 

def graficar_ventas(dias, ventas):
    plt.figure(figsize=(8, 4))
    plt.plot(dias, ventas, marker = "o", linestyle = "-", color = "blue")
    plt.title("Ventas diarias")
    plt.xlabel("Día")
    plt.ylabel("Ventas")
    plt.grid(True)
    
    plt.show()

def main_frontend():
    dias = ["Lun", "Mar", "Mie", "Jue", "Vie"]
    ventas = [120, 500, 230, 289, 310]
    graficar_ventas(dias,ventas)

main_frontend()

print("Despliegue de datos")
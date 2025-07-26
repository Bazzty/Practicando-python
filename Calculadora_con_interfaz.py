import tkinter as tk

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura_cm = float(entry_altura.get())
        altura_m = altura_cm / 100
        imc = peso / (altura_m ** 2)
        resultado_label.config(text=f"Tu IMC es: {imc:.2f}")
    except ValueError:
        resultado_label.config(text="Por favor, ingresa valores válidos.")

ventana = tk.Tk()
ventana.title("Calculadora IMC")
ventana.geometry("350x400")

# Título
titulo = tk.Label(ventana, text="Calculadora de IMC", font=("Arial", 16, "bold"))
titulo.pack(pady=20)

# Peso
etiqueta_peso = tk.Label(ventana, text="Peso (kg):", font=("Arial", 12))
etiqueta_peso.pack()
entry_peso = tk.Entry(ventana, font=("Arial", 12))
entry_peso.pack(pady=5)

# Altura
etiqueta_altura = tk.Label(ventana, text="Altura (cm):", font=("Arial", 12))
etiqueta_altura.pack()
entry_altura = tk.Entry(ventana, font=("Arial", 12))
entry_altura.pack(pady=5)

# Botón Calcular
boton_calcular = tk.Button(ventana, text="Calcular IMC", font=("Arial", 12), command=calcular_imc)
boton_calcular.pack(pady=10)

# Resultado
resultado_label = tk.Label(ventana, text="", font=("Arial", 12))
resultado_label.pack(pady=10)

ventana.mainloop()
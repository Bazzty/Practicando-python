import tkinter as tk

def sumar():
    resultado = float(entrada1.get()) + float(entrada2.get())
    resultado_label.config(text=f"Resultado: {resultado}")

def restar():
    resultado = float(entrada1.get()) - float(entrada2.get())
    resultado_label.config(text=f"Resultado: {resultado}")

def multiplicar():
    resultado = float(entrada1.get()) * float(entrada2.get())
    resultado_label.config(text=f"Resultado: {resultado}")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora Simple")

# Entradas
entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)

entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

# Botones
tk.Button(ventana, text="Sumar", command=sumar).pack(pady=5)
tk.Button(ventana, text="Restar", command=restar).pack(pady=5)
tk.Button(ventana, text="Multiplicar", command=multiplicar).pack(pady=5)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="Resultado:")
resultado_label.pack(pady=10)

# Ejecutar la app
ventana.mainloop()
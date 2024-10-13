import os 
os.system("cls")

import tkinter as tk

def main():
    ventana = tk.Tk()
    for i in range(10):
        tk.Button(ventana, text=f'Botón {i+1}').pack(pady=5)
    ventana.mainloop()

if __name__ == "__main__":
    main()
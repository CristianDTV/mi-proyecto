#main.py
import tkinter as tk
from tkinter import filedialog
from braille_conversion import texto_a_braille
from pdf_generation import generar_pdf_espejo

def convertir_a_braille():
    texto = text_input.get("1.0", tk.END).strip()
    if texto:  # Verificar que el texto no esté vacío
        texto_braille = texto_a_braille(texto)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, texto_braille)

def guardar_como_pdf_espejo():
    texto_braille = text_output.get("1.0", tk.END).strip()
    if texto_braille:  # Verificar que el texto no esté vacío
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            generar_pdf_espejo(texto_braille, file_path)

def crear_gui():
    window = tk.Tk()
    window.title("Traductor de Braille")

    global text_input, text_output
    text_input = tk.Text(window, height=10, width=50)
    text_input.pack(pady=10)
    text_input.bind("<KeyRelease>", lambda event: convertir_a_braille())  # Actualización automática al soltar la tecla

    text_output = tk.Text(window, height=10, width=50)
    text_output.pack(pady=10)


    btn_guardar_pdf_espejo = tk.Button(window, text="Guardar como PDF Espejo", command=guardar_como_pdf_espejo)
    btn_guardar_pdf_espejo.pack(side=tk.RIGHT, padx=5, pady=5)

    window.mainloop()


if __name__ == "__main__":
    crear_gui()

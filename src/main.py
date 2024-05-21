import tkinter as tk
from tkinter import filedialog, simpledialog
from braille_conversion import texto_a_braille
from pdf_generation import generar_pdf

def convertir_a_braille():
    texto = text_input.get("1.0", tk.END)
    texto_braille = texto_a_braille(texto)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, texto_braille)

def guardar_como_pdf():
    texto_braille = text_output.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        generar_pdf(texto_braille, file_path)
        tk.messagebox.showinfo("Éxito", "El archivo PDF ha sido generado con éxito.")

def crear_gui():
    window = tk.Tk()
    window.title("Traductor de Braille")

    global text_input, text_output
    text_input = tk.Text(window, height=10, width=50)
    text_input.pack(pady=10)

    btn_convertir = tk.Button(window, text="Convertir a Braille", command=convertir_a_braille)
    btn_convertir.pack(pady=5)

    text_output = tk.Text(window, height=10, width=50)
    text_output.pack(pady=10)

    btn_guardar_pdf = tk.Button(window, text="Guardar como PDF", command=guardar_como_pdf)
    btn_guardar_pdf.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    crear_gui()

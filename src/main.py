import tkinter as tk
from tkinter import filedialog, messagebox
from braille_conversion import texto_a_braille
from pdf_generation import generar_pdf_espejo

def convertir_a_braille(event=None):
    texto = text_input.get("1.0", tk.END).strip()
    texto_braille = texto_a_braille(texto)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, texto_braille)

def guardar_como_pdf_espejo():
    texto_braille = text_output.get("1.0", tk.END).strip()
    if texto_braille:  # Verificar que el texto no esté vacío
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            generar_pdf_espejo(texto_braille, file_path)
            messagebox.showinfo("Éxito", "Se ha creado el PDF correctamente.")

def mostrar_acerca_de():
    messagebox.showinfo("Acerca De", "Traductor de Braille\nVersión Z\nDesarrollado por: CristianDTV\nEPN 2024")

def crear_gui():
    window = tk.Tk()
    window.title("Traductor de Braille")
    window.geometry("900x700")
    window.configure(bg="#F0F0F0")

    # Menú
    menu_bar = tk.Menu(window)
    window.config(menu=menu_bar)

    menu_ayuda = tk.Menu(menu_bar, tearoff=0)
    menu_ayuda.add_command(label="Acerca De", command=mostrar_acerca_de)
    menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)

    # Frame izquierdo para el menú interactivo
    frame_menu = tk.Frame(window, bg="#D9EAD3", width=200, height=600)
    frame_menu.pack(side=tk.LEFT, fill=tk.Y)
    frame_menu.pack_propagate(False)

    label_menu = tk.Label(frame_menu, text="Menú", bg="#D9EAD3", font=("Helvetica", 16))
    label_menu.pack(pady=10)

    # Frame derecho para la funcionalidad principal
    frame_main = tk.Frame(window, bg="#FFFFFF", width=600, height=600)
    frame_main.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    frame_main.pack_propagate(False)

    global text_input, text_output

    label_input = tk.Label(frame_main, text="Texto a Convertir", bg="#FFFFFF", font=("Helvetica", 14))
    label_input.pack(pady=5)

    text_input = tk.Text(frame_main, height=10, width=50, font=("Helvetica", 16))
    text_input.pack(pady=10)
    text_input.bind("<KeyRelease>", convertir_a_braille)  # Actualización automática al soltar la tecla

    label_output = tk.Label(frame_main, text="Texto en Braille", bg="#FFFFFF", font=("Helvetica", 14))
    label_output.pack(pady=5)

    text_output = tk.Text(frame_main, height=10, width=50, font=("Helvetica", 16), bg="#E0E0E0")
    text_output.pack(pady=10)

    btn_guardar_pdf_espejo = tk.Button(frame_main, text="Guardar como PDF Espejo", command=guardar_como_pdf_espejo, bg="#4CAF50", fg="#FFFFFF", font=("Helvetica", 12))
    btn_guardar_pdf_espejo.pack(pady=20)

    window.mainloop()

if __name__ == "__main__":
    crear_gui()

import customtkinter as ctk
from tkinter import filedialog, messagebox

from braille_conversion import texto_a_braille
from pdf_generation import generar_pdf_espejo

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def convertir_a_braille(event=None):
    texto = text_input.get("1.0", "end-1c").strip()
    texto_braille = texto_a_braille(texto)
    text_output.delete("1.0", "end")
    text_output.insert("1.0", texto_braille)

def guardar_como_pdf_espejo():
    texto_braille = text_output.get("1.0", "end-1c").strip()
    if texto_braille:
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            generar_pdf_espejo(texto_braille, file_path)
            messagebox.showinfo("Éxito", "Se ha creado el PDF correctamente.")

def mostrar_acerca_de():
    messagebox.showinfo("Acerca De", "Traductor de Braille\nVersión Z\nDesarrollado por: CristianDTV\nEPN 2024")

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')

def crear_gui():
    window = ctk.CTk()
    window.title("Traductor de Braille")
    window.geometry("1000x800")
    centrar_ventana(window, 900, 700)
    window.resizable(True, True)

    frame_menu = ctk.CTkFrame(window, width=200, height=800, corner_radius=0)
    frame_menu.pack(side="left", fill="y")

    label_menu = ctk.CTkLabel(frame_menu, text="Menú", font=("Helvetica", 18))
    label_menu.pack(pady=20)
    
    btn_acerca_de = ctk.CTkButton(frame_menu, text="Acerca De", command=mostrar_acerca_de)
    btn_acerca_de.pack(fill="x", padx=20, pady=10)

    frame_main = ctk.CTkFrame(window, width=800, height=800, corner_radius=0)
    frame_main.pack(side="right", fill="both", expand=True)

    global text_input, text_output

    label_input = ctk.CTkLabel(frame_main, text="Texto a Convertir", font=("Helvetica", 16))
    label_input.pack(pady=10)

    text_input = ctk.CTkTextbox(frame_main, height=200, width=500, font=("Helvetica", 16))
    text_input.pack(pady=10)
    text_input.bind("<KeyRelease>", convertir_a_braille)

    label_output = ctk.CTkLabel(frame_main, text="Texto en Braille", font=("Helvetica", 16))
    label_output.pack(pady=10)

    text_output = ctk.CTkTextbox(frame_main, height=200, width=500, font=("Helvetica", 16))
    text_output.pack(pady=10)

    btn_guardar_pdf_espejo = ctk.CTkButton(frame_main, text="Guardar como PDF Espejo", command=guardar_como_pdf_espejo)
    btn_guardar_pdf_espejo.pack(pady=20)

    window.mainloop()

if __name__ == "__main__":
    crear_gui()

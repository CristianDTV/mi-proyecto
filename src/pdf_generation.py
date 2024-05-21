
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Ruta a la fuente de braille, ajusta según la ubicación en tu proyecto
FONT_PATH = 'assets/fonts/ONCE_CBE_6.ttf'

def generar_pdf(texto_braille, nombre_archivo):
    """ Genera un archivo PDF con el texto braille proporcionado. """
    # Registrar la fuente de Braille
    pdfmetrics.registerFont(TTFont('Braille', FONT_PATH))

    # Configurar la página
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont("Braille", 20)  # Ajustar el tamaño de la fuente según sea necesario

    # Preparar el texto para la impresión en el PDF
    lineas = texto_braille.strip().split('\n')
    x, y = 30, 750  # Ajustar la posición inicial según sea necesario

    for linea in lineas:
        c.drawString(x, y, linea)
        y -= 30  # Ajustar el espacio entre líneas según sea necesario

    c.save()

def generar_pdf_espejo(texto_braille, nombre_archivo):
    """ Genera un archivo PDF en modo espejo con el texto braille proporcionado. """
    # Registrar la fuente de Braille
    pdfmetrics.registerFont(TTFont('Braille', FONT_PATH))

    # Configurar la página
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont("Braille", 20)  # Ajustar el tamaño de la fuente según sea necesario

    # Aplicar transformación para modo espejo
    c.translate(letter[0], 0)
    c.scale(-1, 1)

    # Preparar el texto para la impresión en el PDF
    lineas = texto_braille.strip().split('\n')
    x, y = 30, 750  # Ajustar la posición inicial según sea necesario

    for linea in lineas:
        c.drawString(x, y, linea)
        y -= 30  # Ajustar el espacio entre líneas según sea necesario

    c.save()



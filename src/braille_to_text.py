# braille_to_text.py
import cv2
import pytesseract

def image_to_braille(image_path):
    """Convierte una imagen a texto braille utilizando OCR."""
    # Leer la imagen
    img = cv2.imread(image_path)
    # Convertir a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Aplicar OCR
    braille_text = pytesseract.image_to_string(gray, lang='braille')
    return braille_text

def pdf_to_image(pdf_path):
    """Convierte la primera página de un PDF a imagen."""
    # Aquí puedes usar PyMuPDF (fitz) para extraer imágenes de PDFs
    import fitz  # PyMuPDF
    doc = fitz.open(pdf_path)
    page = doc[0]  # Asume que vamos a trabajar solo con la primera página
    pix = page.get_pixmap()
    img_path = "output_image.png"
    pix.save(img_path)
    doc.close()
    return img_path

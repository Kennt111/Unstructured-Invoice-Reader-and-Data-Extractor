import os
import shutil
import fitz  # PyMuPDF

SOURCE_DIR = r"C:\Users\Kenzo\Documents\Python\Facturas\Invoid_PDF"

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Crear carpetas de meses si no existen
for month in months:
    os.makedirs(os.path.join(SOURCE_DIR, month), exist_ok=True)

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Procesar PDFs
for filename in os.listdir(SOURCE_DIR):
    if not filename.lower().endswith(".pdf"):
        continue

    pdf_path = os.path.join(SOURCE_DIR, filename)
    text = extract_text_from_pdf(pdf_path)

    moved = False
    for month in months:
        if month in text:
            dest_folder = os.path.join(SOURCE_DIR, month)
            shutil.move(pdf_path, os.path.join(dest_folder, filename))
            print(f"📄 {filename} → {month}")
            moved = True
            break

    if not moved:
        print(f"⚠️ Mes no encontrado en: {filename}")

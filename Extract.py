import os
import fitz  # PyMuPDF

# Carpeta raíz donde están las subcarpetas de enero a diciembre
root_dir = r"C:\Users\Kenzo\Documents\Python\Facturas\Invoid_PDF"

# Carpeta donde se guardarán TODOS los textos (FUERA de Invoid_PDF)
output_dir = r"C:\Users\Kenzo\Documents\Python\Facturas\texto"
os.makedirs(output_dir, exist_ok=True)

# Recorrer cada carpeta de mes
for month_folder in os.listdir(root_dir):
    month_path = os.path.join(root_dir, month_folder)

    if os.path.isdir(month_path):
        for file in os.listdir(month_path):
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(month_path, file)

                doc = fitz.open(pdf_path)
                text = ""

                for page in doc:
                    text += page.get_text()

                # Guardar cada factura como archivo de texto en /texto
                output_file = os.path.join(
                    output_dir, f"{month_folder}_{file[:-4]}.txt"
                )

                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(text)

print("✅ Extracción completada. Todos los TXT están en C:\\Users\\Kenzo\\Documents\\Python\\Facturas\\texto")

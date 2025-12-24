
import os
import json
import pandas as pd
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="OPENAI_API_KEY"  
)

FOLDER_PATH = r"C:\Users\Kenzo\Documents\Python\Facturas\texto"

def extract_invoice_data(text):
    prompt = f"""
Del siguiente texto de una FACTURA, extrae la información solicitada.

Devuelve EXCLUSIVAMENTE un JSON válido con esta estructura exacta:

{{
  "names": [string],
  "dates": [string],
  "total_amount": number | null,
  "product_name": string | null,
  "country": string | null
}}

Reglas:
- "names": nombres completos de personas (no empresas)
- "dates": fechas encontradas CONVERTIDAS AL FORMATO YYYY-MM-DD
- "total_amount": el VALOR TOTAL de la factura (no subtotal, no impuestos)
- "product_name": nombre del PRODUCTO PRINCIPAL comprado
- "country": país de origen del producto o del proveedor
- Si no existe un campo, usa [] o null
- No inventes información
- No agregues texto fuera del JSON

Texto:
{text}
"""

    response = client.chat.completions.create(
        model="allenai/olmo-3.1-32b-think:free",
        messages=[{"role": "user", "content": prompt}]
    )

    return json.loads(response.choices[0].message.content)


rows = []

# 👉 HEADER DEL CSV (se imprime una sola vez)
print("file,person_name,invoice_date,total_amount,product_name,country")

for filename in os.listdir(FOLDER_PATH):
    if filename.endswith(".txt"):
        file_path = os.path.join(FOLDER_PATH, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        data = extract_invoice_data(text)

        invoice_date = data["dates"][0] if data["dates"] else None

        for name in data["names"]:
            row = {
                "file": filename,
                "person_name": name,
                "invoice_date": invoice_date,
                "total_amount": data["total_amount"],
                "product_name": data.get("product_name"),
                "country": data.get("country")
            }

            rows.append(row)

            # 👉 PRINT EXACTO COMO CSV
            print(
                f'{row["file"]},'
                f'{row["person_name"]},'
                f'{row["invoice_date"]},'
                f'{row["total_amount"]},'
                f'{row["product_name"]},'
                f'{row["country"]}'
            )

        print(f"✅ Procesado: {filename}")

# Crear DataFrame final
df = pd.DataFrame(rows)

OUTPUT_FILE = "facturas_powerbi.csv"
df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

print(f"\n📊 Tabla creada correctamente: {OUTPUT_FILE}")

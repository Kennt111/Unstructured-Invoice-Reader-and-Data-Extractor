# Unstructured-Invoice-Reader-and-Data-Extractor
This project implements an end-to-end automated pipeline for extracting structured data from unstructured invoice PDFs using AI.
The system processes raw invoice PDFs with no predefined format, automatically extracts their textual content, organizes files by month, and leverages a Large Language Model (LLM) to identify and structure key invoice information. The final output is a clean, analytics-ready dataset designed for direct consumption in Power BI or other BI tools.

🔹 Key Features

PDF text extraction using PyMuPDF (fitz)
Automatic invoice classification by month based on detected text
AI-powered information extraction from unstructured invoice text using LLMs via OpenRouter

Extraction of:
Personal names (excluding companies)
Invoice dates (normalized to YYYY-MM-DD)
Total invoice amount
Main product purchased
Country of origin (product or supplier)

Strict JSON validation to ensure reliable downstream processing
CSV generation optimized for Power BI
Fully automated batch processing for large volumes of invoices

🔹 Data Pipeline Overview

PDF ingestion from a raw invoices directory
Text extraction from each PDF
Automatic month-based file organization
LLM-based semantic extraction from invoice text
Data normalization and validation
CSV export for Power BI visualization and analysis

🔹 Technologies Used

Python
PyMuPDF (fitz) for PDF parsing
Pandas for data structuring
LLMs (via OpenRouter / OpenAI-compatible API) for semantic extraction
Power BI for data visualization and reporting

🔹 Use Cases

Financial data analysis
Invoice automation and accounting workflows
AI-assisted document understanding
Business intelligence and reporting

import os
import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
from docx import Document
from io import BytesIO

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = "\n".join([page.extract_text() for page in reader.pages])
    return text

# Function to extract text from a DOC/DOCX file
def extract_text_from_doc(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Streamlit app starts here
st.title("Document Processing to Excel")

uploaded_folder = st.file_uploader("Upload a folder containing PDF or DOC/DOCX files", accept_multiple_files=True)

if uploaded_folder:
    data = []

    for uploaded_file in uploaded_folder:
        file_name = uploaded_file.name
        file_extension = os.path.splitext(file_name)[1].lower()

        if file_extension == ".pdf":
            text = extract_text_from_pdf(uploaded_file)
        elif file_extension in [".doc", ".docx"]:
            text = extract_text_from_doc(uploaded_file)
        else:
            st.warning(f"Unsupported file type: {file_name}")
            continue

        data.append({"File Name": file_name, "Extracted Text": text})

    if data:
        # Create a DataFrame
        df = pd.DataFrame(data)

        # Convert DataFrame to Excel
        excel_file = BytesIO()
        with pd.ExcelWriter(excel_file, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="Processed Data")

        excel_file.seek(0)

        st.success("Processing complete! Download the Excel file below.")
        st.download_button(
            label="Download Excel File",
            data=excel_file,
            file_name="processed_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.warning("No valid files were processed.")

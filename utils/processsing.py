from PyPDF2 import PdfReader
from docx import Document


# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    """
    Helps to extract text from a PDF file
    :param file_path: Path to the PDF file
    """
    
    reader = PdfReader(file_path)
    text = "\n".join([page.extract_text() for page in reader.pages])
    return text



# Function to extract text from a DOC/DOCX file
def extract_text_from_doc(file_path):
    """
    Helps to extract text from a DOC/DOCX file
    :param file_path: Path to the DOC/DOCX file
    """
    
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text



# Function to process the text using the Gemini API
def process_text_with_gemini(text):
    """
    Helps to process the text using the Gemini API
    :param text: Text to be processed
    """
    
    # Call the Gemini API to process the text
    process_data = {
        "name" : "Gemini API",
        "ATS" : 81,
        "Proficiency" : 100,
        "lacks" : ["react", "angular", "vue"],
        "skills" : ["python", "sql"],
        "experience" : 3, 
    }
    return 


#Function to get the data as a list of dictionaries and call the gemini api to process the text
def process_data(data):
    """
    Helps to process the extracted text data using the Gemini API
    :param data: List of dictionaries containing file name and extracted text
    """
    
    # Call the Gemini API to process the text
    processed_data = []
    for item in data:
        file_name = item["File Name"]
        extracted_text = item["Extracted Text"]
        
        # Call the Gemini API to process the text
        processed_text = process_text_with_gemini(extracted_text)
        
        processed_data.append({"File Name": file_name, "Processed Text": processed_text})
    
    return processed_data








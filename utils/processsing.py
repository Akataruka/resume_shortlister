from PyPDF2 import PdfReader
from docx import Document
import os
import streamlit as st
import json


def process_data(uploaded_folder,job):
    '''
    Function to process the extracted data
    :param uploaded_folder: List of uploaded files
    :param job: Job object
    '''
    
    #extract the data  as a dictionary from teh different files
    data = get_data(uploaded_folder)
    
    #jsonify the data and the job title
    json_data = create_json(data,job)
    
    #response is a list of dictionary objects
    '''
    response = [
        {
            "name": "John Doe",
            "score": 0.8,
            "contact": "",
            "email": "",
            "resume": "file name",
            "skills": [],
            "experience": 0,
            "proficiency": 0,
            "education": "",
            "projects": [],
            "languages": [],
            "lacks: [],
            "recommendations": [],
            "comments": []
        }
    '''
    
    #get the response from the gemini api
    response = gemini_call(json_data)
    
    #return the response as a list of dictionary objects
    return response
    
    



def create_json(data,job):
    '''
    Function to create a json object from the extracted data
    :param data: List of extracted data
    :param job: Job object
    '''
    
    job_data = {
        "job_title": job.job_title,
        "job_description": job.job_description,
        "job_skills": job.job_skills,
        "job_experience": job.job_experience,
        "job_proficiency": job.job_proficiency,
        "candidates": []
    }
    
    for candidate in data:
        job_data["candidates"].append(candidate)
        
    return json.dumps(job_data)


def gemini_call(json_data):
    '''
    Function to call the Gemini API
    :param json_data: Json object to be sent to the API
    '''
    
    #API call code here
    return "API call successful"



    
    



def get_data(uploaded_folder):
    '''
    function to extract the data from the uploaded folder
    :param uploaded_folder: List of uploaded files
    '''
    
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
        
    return data
    

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










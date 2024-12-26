import os
import streamlit as st
import pandas as pd
from io import BytesIO
from utils.processsing import extract_text_from_pdf, extract_text_from_doc
from utils.helper import set_job_description
from model.job import job
from data.info import software_positions, technology_stacks
from template.markdown import generate_job_html


#job initialisation
current_job = job(
    job_title="software Engineer",
    job_description="",
    job_skills=[],
    job_experience=0,
    job_proficiency=0
)

# Streamlit app starts here
st.title("Resume Shortlister")

with st.sidebar:
    with st.form(key="job_description_form", border=False, enter_to_submit=False):
        st.title("Job Description")
        
        #job title input field
        job_title = st.selectbox(
        label = "Select a job title",
        index=None,
        options = software_positions,
        label_visibility="collapsed",
        placeholder="Select a job title"
        )
        
        #Job Description input field
        job_description = st.text_area(
        label = "Job Description",
        placeholder = "Enter the job description here",
        label_visibility="collapsed"
        )
        
        #Input field for the skill set
        job_skills = st.multiselect(
            label= "Select the required skills",
            options=technology_stacks,
            placeholder="Select the required skills",
            label_visibility="collapsed",
            default=None
        )
        
        #input field for experience
        st.write("Required Experience")
        job_experience = st.slider(
            key="experience",
            label="Required Experience",
            min_value=0,
            max_value=10,
            value=0,
            step=1,
            label_visibility="collapsed",
            # format="%d",
            # help="Select the required experience in years",
        )
        
        #input field for Proficiency
        st.write("Rate the proficiency level")
        job_proficiency = st.slider(
            key="proficiency",
            label="Required Experience",
            label_visibility="collapsed",
            min_value=0,
            max_value=5,
            value=0,
            step=1,
        )
        
        #Submit button to set the job description
        submitted = st.form_submit_button(
            label="Set Job",
            help="Click to set the job description",
            on_click=set_job_description(job_title, job_description, job_skills, job_experience, job_proficiency, current_job),
            use_container_width=True,
        )
        
#Description of the job on main screen
markdown = generate_job_html(current_job)
print(current_job)
with st.empty():
    st.markdown(body = markdown, unsafe_allow_html=True)   
#upload menu to upload a folder containing the resumes
uploaded_folder = st.file_uploader("Upload a folder containing PDF or DOC/DOCX files", accept_multiple_files=True)



'''
Rest of the code goes here
1. api calling the gemini api to process the text
2. processing the data
3. downloading the processed data
4. displaying the processed data
5. displaying the shortlisted resumes
'''
    
    
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
        
        
    #here the data contents the filename and the extracted raw text
    #we need to call the gemini api here to convert and process the text
    
    data = [{"File Name": "file1.pdf", "Extracted Text": "This is the extracted text from file1.pdf"}, {"File Name": "file2.docx", "Extracted Text": "This is the extracted text from file2.docx"}]
    

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

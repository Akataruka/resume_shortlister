from typing import List
from model.job import job
import streamlit as st

# Function to set the job description in main page
def set_job_description(job_title:str, job_description:str, job_skills:List[str], job_experience:int, job_proficiency:int,current_job: job):
    """
    Helps to set the job description in the main page
    :param job_title: Job title
    :param job_description: Job description
    :param job_skills: List of required skills
    :param job_experience: Required experience in years
    :param job_proficiency: Required proficiency level
    """
    
    current_job.job_title = job_title
    current_job.job_description = job_description
    current_job.job_skills = job_skills
    current_job.job_experience = job_experience
    current_job.job_proficiency = job_proficiency
    
    
    
def candidate_row(candidate):
    '''
    Function to create a row for the candidate
    :param candidate: Candidate object
    '''
    with st.expander(f"Name: {candidate.name} | Score: {candidate.score}", expanded=False):
        st.write(f"Email: {candidate.email}")
        st.write(f"Phone: {candidate.phone}")
        st.write(f"Experience: {candidate.experience}")
        st.write(f"Proficiency: {candidate.proficiency}")
        st.write(f"Skills: {candidate.skills}")
        st.write(f"Resume: {candidate.resume}")
        st.write(f"Matched Skills: {candidate.matched_skills}")
        st.write(f"Matched Experience: {candidate.matched_experience}")
        st.write(f"Matched Proficiency: {candidate.matched_proficiency}")
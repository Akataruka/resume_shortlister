
from model.job import job

    
def generate_job_html(curr_job: job):
    """
    Helps to create a markdown string for the job description
    :param job_title: Job title
    :param job_description: Job description
    :param job_skills: List of required skills
    :param job_experience: Required experience in years
    :param job_proficiency: Required proficiency level
    """
    
    html_template = f"""
    Job Title: :red[{curr_job.job_title}]    
    Job Description: :red[{curr_job.job_description}] &emsp;
    Required Skills: :red[{", ".join(curr_job.job_skills)}]<br>
    Required Experience:&ensp;  :red[{curr_job.job_experience}] &emsp;
    Required Proficiency:&ensp;  :red[{curr_job.job_proficiency}]
    
    
    """
    return html_template

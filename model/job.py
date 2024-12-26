from pydantic import BaseModel
from typing import List

class job(BaseModel):
    job_title: str
    job_description: str
    job_skills: List[str]
    job_experience: int 
    job_proficiency: int        
    
from pydantic import BaseModel , EmailStr , AnyUrl , Field
from typing import List , Dict , Optional , Annotated

class Patient(BaseModel):
    name: Annotated[str , Field(max_length=50 , title='Name of the patient' , description='Give the name of the patient in less than 50 character' , examples=['nitish' , 'Amit'])]
    email : EmailStr
    linkedin_url : AnyUrl
    age: int
    weight : Annotated[float , Field(gt=0 , strict=True)]
    married : Annotated[bool , Field(default = none , description='Is this person married or not')]
    allergies :Optional[List[str]] = None  # allerigies khud mein list hai but uska saara element string honga isliye hmlog typing se import kiye List , Dict
    contact_details : Dict[str , str]

def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.email)
    print(patient.linkedin_url)
    print('inserted')

patient_info = {"name" : "Nitish" , 'email': 'abc@gmail.com' , 'linkedin_url' : 'http://linkedin.com/112' ,"age" : 30 , 'weight' : 75.2 , 'married': True , 'allergies' : ['Pollen' , 'dust'] , 'contact_details' :{'email' : 'abc123@example.com' , 'phone' : '900000000'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)




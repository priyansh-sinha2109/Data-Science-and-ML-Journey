from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator
from typing import List , Dict , Optional , Annotated 

class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight: float
    married : bool
    allergies: List[str]
    contact_details : Dict[str , str]
    linkedin_url : AnyUrl

    @field_validator('email')
    @classmethod
    def email_validator(cls , value):
         valid_domains = ['hdfc.com' , 'icici.com']
         domain_name = value.split('@')[-1]

         if domain_name not in valid_domains:
              raise ValueError('Not a valid domain')

    @field_validator('name' , mode='before')
    @classmethod
    def transform_name(cls , value):
         return value.upper()
    @field_validator('age' , mode='after')
    @classmethod
    def validate_age(cls , value):
         if 0 < value:
              return value
         else:
              raise ValueError('Age Should be in 0 to 100')

def update_patient_data(patient : Patient):
      print(patient.name)
      print(patient.age)
      print(patient.weight)
      print(patient.married)
      print(patient.allergies)
      print(patient.contact_details)
      print(patient.email)
      print(patient.linkedin_url)
      print('Updated')

Patient_info = {"name" : "Nitish" , 'email': 'abc@icici.com' , 'linkedin_url' : 'http://linkedin.com/112' ,"age" : '30' , 'weight' : 75.2 , 'married': True , 'allergies' : ['Pollen' , 'dust'] , 'contact_details' :{'email' : 'abc123@example.com' , 'phone' : '900000000'}}


patient1 = Patient(**Patient_info)  #validation -> type coercion

update_patient_data(patient1)

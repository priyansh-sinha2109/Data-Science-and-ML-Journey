from pydantic import BaseModel , EmailStr , model_validator
from typing import List , Dict

class Pateint(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight: float
    married : bool
    allergies: List[str]
    contact_details : Dict[str , str]

    @model_validator(mode= 'after')
    def validate_emergency_contact(cls , model):
         if model.age > 60 and 'emergency' not in model.contact_details:
              raise ValueError('patients older than 60 must have an emergency contact')

def update_patient_data(patient : Pateint):
      print(patient.name)
      print(patient.age)
      print(patient.weight)
      print(patient.married)
      print(patient.allergies)
      print(patient.contact_details)
      print(patient.email)
      print('Updated')


Patient_info = {"name" : "Nitish" , 'email': 'abc@icici.com' , "age" : '65' , 'weight' : 75.2 , 'married': True , 'allergies' : ['Pollen' , 'dust'] , 'contact_details' :{'email' : 'abc123@example.com' , 'phone' : '900000000' , 'emergency' : '234567'}}


patient1 = Pateint(**Patient_info)  #validation -> type coercion

update_patient_data(patient1)
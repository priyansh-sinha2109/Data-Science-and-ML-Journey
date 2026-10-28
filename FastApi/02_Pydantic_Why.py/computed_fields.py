from pydantic import BaseModel , EmailStr , computed_field
from typing import List , Dict

class Pateint(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float #kg
    height : float #mtr
    weight: float
    married : bool
    allergies: List[str]
    contact_details : Dict[str , str]

    @computed_field
    @property
    def bmi(self) -> float:
         bmi = round(self.weight/(self.height**2), 2)
         return bmi


def update_patient_data(patient : Pateint):
      print(patient.name)
      print(patient.age)
      print(patient.weight)
      print(patient.married)
      print(patient.allergies)
      print(patient.contact_details)
      print('BMI' ,patient.bmi)
      print(patient.email)
      print('Updated')


Patient_info = {"name" : "Nitish" , 'email': 'abc@icici.com' , "age" : '65' , 'weight' : 75.2 , 'height' : 1.72 , 'married': True , 'allergies' : ['Pollen' , 'dust'] , 'contact_details' :{'email' : 'abc123@example.com' , 'phone' : '900000000' , 'emergency' : '234567'}}


patient1 = Pateint(**Patient_info)  #validation -> type coercion

update_patient_data(patient1)
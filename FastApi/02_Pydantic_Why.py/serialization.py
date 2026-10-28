from pydantic import BaseModel

class Address(BaseModel):

    city : str
    state : str
    pin : str

class Pateint(BaseModel):

    name : str
    gender: str
    age: int
    address : Address


address_dict = {'city' : 'Gurgaon' , 'state' : 'Haryana' , 'pin' : '122001'}

address_1 = Address(**address_dict)

patient_dict = {'name' : 'nitish' , 'gender' : 'Male' , 'age' : 35 , 'address' : address_1}

patient_1 = Pateint(**patient_dict)


print(patient_1)


temp = patient_1.model_dump(exclude=['name' , 'gender'])

print(temp)
print(type(temp))

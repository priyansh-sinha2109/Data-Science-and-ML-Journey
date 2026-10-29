def insert_patient_data(name: str , age: int):

    if type(name) == str and type(age) == int:
     if age < 0:
            raise ValueError("Age can't be negative")
     else:
        print(name)
        print(age)
        print('inserted into database')
    else:
        raise TypeError('Incorrect Data type')

def update_patient_data(name: str , age: int):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('updated')
    else:
        raise TypeError('Incorrect Data type')


insert_patient_data('nitish' , 30)
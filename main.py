from gender_enum import Gender
from user import User

user_dic = {
    "first_name" : "Dadfar",
    "last_name": "Momeni",
    "mobile_number": "09376408840",
    "email": "dadfar.momeni@gmail.com",
    "national_id": "0521040469",
    "username": "dadfar98",
    "birthdate": "1998-01-11",
    "gender": Gender.Male
}


user_obj = User(user_dic)
print(user_obj)
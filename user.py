from gender_enum import Gender
class User:
    def __init__(self, user_dic):
        # super().__init__()
        self.fist_name = user_dic["first_name"]
        self.last_name = user_dic["last_name"]
        self.national_id = user_dic["national_id"]
        self.mobile_number = user_dic["mobile_number"]
        self.email = user_dic["email"]
        self.birthdate = user_dic["birthdate"]
        self.gender = user_dic["gender"]
        self.username = user_dic["username"]

    def __str__(self):
        return str(self.__dict__)
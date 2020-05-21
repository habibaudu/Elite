import re

class ValidateUser:
    def __init__(self):
        self.err_list = []
 
    def validate_register(self,**kwargs):
        first_name = self.validate_name(kwargs.get("first_name"), 'first_name')
        last_name = self.validate_name(kwargs.get('last_name'), 'last_name')
        email = self.validate_email(kwargs.get('email'))
        password = self.validate_password(kwargs.get('password'))

        if len(self.err_list):
            return self.err_list

        return {
            "email": email,
            "password": password,
            "first_name": first_name,
            "last_name": last_name
        }


    def validate_name(self, name, field_name):
        if name is not None:
            if len(name.strip()) < 2:
                self.err_list.append({f"{field_name}": "{} must be two (2) and above characters".format(name)})
        name_regex = re.search(r'[^a-zA-Z\-]+', name)
        if name_regex is not None:
            self.err_list.append(
                {f"{field_name}": f"{name} can only contain alphabets and hyphens."})

        return name
    

    def validate_email(self, email):
        email = email.strip()
        if re.match(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]{2,5}$',
                    email) is None:
            self.err_list.append({"email": "Please input a valid email"})
        return email.lower()

    def validate_password(self, password):
        password = password.strip()
        if re.match('(?=.{8,32})(?=.*[A-Z])(?=.*[0-9])', password) is None:
            self.err_list.append(
                {"password": "password must have at least 8 characters, a number and a capital letter"})
        return password
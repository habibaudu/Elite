import re
from users_app.models import(State)

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

    def validate_invention(self, **kwargs):
        about_invention = self.validate_about_invention(kwargs.get("about_invention"),'about_invention')
        title = self.validate_title(kwargs.get('title'),'title')

        if len(self.err_list):
            return self.err_list

        return {
            "about_invention": about_invention,
            "title": title
        }

    def validate_title(self,title,field):
        if len(title.strip()) < 5:
            self.err_list.append({f"{field}": "{} must be five (5) and above characters".format(field)})
        title_regex = re.search(r'[^a-zA-Z\-\s]+', title)
        if title_regex is not None:
            self.err_list.append({f"{field}": f"{field} can only contain alphabets and hyphens."})
        return title

    def validate_about_invention(self, about_invention,field):
        if len("".join(about_invention.split())) < 50:
            self.err_list.append({f"{field}": "{} must be fifty (50) and above characters".format(field)})
        invent_regex = re.search(r'[^a-zA-Z0-9\-\s]+',about_invention)
        if invent_regex is not None:
            self.err_list.append({f"{field}":f"{field} can only contain numbers and alphabets"})
        return about_invention

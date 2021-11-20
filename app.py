from names import names as name_string
from surnames import surnames as surname_string
from passwords import passwords as password_string
from mail_providers import mail_providers as mail_provider_string
from random import *

def get_arrays():
    arr_names = name_string.split(";")
    arr_surnames = surname_string.split(";")
    arr_passwords = password_string.split(";")
    arr_mail_providers = mail_provider_string.split(";")

    return [arr_names, arr_surnames, arr_passwords, arr_mail_providers]


def lowercase_arrays():
    lower_names = []
    lower_surnames = []

    email_data_arrays = get_arrays()

    names = email_data_arrays[0]
    surnames = email_data_arrays[1]
    passwords = email_data_arrays[2]
    mail_providers = email_data_arrays[3]

    for name in names:
        lower_names.append(name.lower())
    
    for surname in surnames:
        lower_surnames.append(surname.lower())
    

    return [lower_names, lower_surnames, passwords, mail_providers]


def get_email():
    email_data = lowercase_arrays()

    names = email_data[0]
    surnames = email_data[1]
    passwords = email_data[2]
    mail_providers = email_data[3]

    random_name_index = randint(0, len(names) -1)
    random_surname_index = randint(0, len(surnames) -1)
    random_passwords_index = randint(0, len(passwords) -1)
    random_mail_providers_index = randint(0, len(mail_providers) -1)
    

    email_name = names[random_name_index]
    email_surname = surnames[random_surname_index]
    email_password = passwords[random_passwords_index]
    email_provider = mail_providers[random_mail_providers_index]

    email = f"{email_name}{email_surname}@{email_provider}.com"
    password = email_password

    return [email, password]

result = get_email()

email = result[0]
password = result[1]

print("")
print("Email:")
print(email)
print("")
print("Password:")
print(password)
print("")
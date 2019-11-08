import re
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, MinValueValidator, RegexValidator

def validate_password(password):
        password_length = MinValueValidator(8)
        password_valid = password_length.compare(8, len(password))
        if password_valid == False:
            raise ValidationError("Password must be at least 8 characters")
        # add regex for making sure password has characters and symbols
        return password

def validate_email(email):
    email_validator = EmailValidator(email)
    if email_valid == False:
        raise ValidationError()
    return email

'''Validate a username and make sure it contains only alphanumeric characters and special characters'''
def validate_username(username):
    username_validator = RegexValidator(
        r"(^[~0-9A-Za-z]*)",
        "Username must contain only alphanumeric characters and special characters",
        None,
        re.IGNORECASE)
    valid_username = username_validator(username)
    if valid_username == True:
        raise ValidationError()
    return username

def validate_name(name):
    if name.isalnum() == False:
        raise ValidationError("Name must contain only alphanumeric characters")
    return name

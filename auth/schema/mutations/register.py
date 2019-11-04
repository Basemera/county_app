import graphene
import re
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, MinValueValidator, RegexValidator
from django.contrib.auth.validators import UnicodeUsernameValidator

class RegisterUser(graphene.Mutation):
    user_id = graphene.Int()
    first_name = graphene.String()
    last_name = graphene.String()
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()

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

    def mutate(self, info, **kwargs):
        raw_first_name = kwargs.get('first_name')
        raw_last_name = kwargs.get('last_name')
        username = kwargs.get('username')
        raw_email = kwargs.get('email')
        raw_password = kwargs.get('password')
        valid_password = RegisterUser.validate_password(raw_password)
        email = RegisterUser.validate_email(raw_email)
        # username = RegisterUser.validate_username(raw_username)
        first_name = RegisterUser.validate_name(raw_first_name)
        last_name = RegisterUser.validate_name(raw_last_name)
        User = get_user_model()
        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(valid_password)
        user.save()

        return RegisterUser(
            user_id=user.id,
            username=user.username,
            password=user.password,
            last_name=user.last_name,
            first_name=user.first_name,
            email=user.email
        )

class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()


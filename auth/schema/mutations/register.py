import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, MinValueValidator
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
        return password

    def validate_email(email):
        email_validator = EmailValidator()
        email_valid = email_validator.__call__(email)
        if email_valid == False:
            raise ValidationError()
        return email
        
    def mutate(self, info, **kwargs):
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')
        username = kwargs.get('username')
        email = kwargs.get('email')
        raw_password = kwargs.get('password')
        valid_password = RegisterUser.validate_password(raw_password)
        email = RegisterUser.validate_email(email)
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


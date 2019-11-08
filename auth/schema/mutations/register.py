import graphene
import re
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
# from county_app.utils.validations
from utils.validations import validate_email, validate_name, validate_password, validate_username
# from ....utils.validations import validate_username, validate_email, validate_name, validate_password
# from ....utils.validations import validations

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

    def mutate(self, info, **kwargs):
        raw_first_name = kwargs.get('first_name')
        raw_last_name = kwargs.get('last_name')
        username = kwargs.get('username')
        raw_email = kwargs.get('email')
        raw_password = kwargs.get('password')
        valid_password = validate_password(raw_password)
        email = validate_email(raw_email)
        # username = validations.validate_username(raw_username)
        first_name = validate_name(raw_first_name)
        last_name = validations.validate_name(raw_last_name)
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


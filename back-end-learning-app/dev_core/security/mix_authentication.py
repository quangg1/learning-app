from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from dev_core.types.export import *




'''
    TSJ: Token, Session, JWT
'''
MIX_AUTHEN_TSJ: List[
    Union[BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication]
] = [BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication]


'''
     
    
    
    
'''

# Importing necessary type hints from typing module
from typing import Optional, Literal

# Defining a class for user sign-in request
class UserSignInRequest(object):
    # Username and password fields with str type hint
    username: str
    password: str

# Defining a class for user sign-in response
class UserSignInResponse(object):
    # Token field with str type hint
    token: str

# Defining a class for user sign-up request
class UserSignUpRequest(object):
    # Username, password, email, and full name fields with str type hint
    username: str
    password: str
    email: str
    full_name: str

# Defining a class for user sign-up response
class UserSignUpResponse(object):
    # Token field with str type hint
    token: str

# Defining a class for user sign-out request
class UserSignOutRequest(object):
    # Token field with str type hint
    token: str

# Defining a class for user forgot password request
class UserForgotPasswordRequest(object):
    # Email field with str type hint
    email: str

# Defining a class for user forgot password response
class UserForgotPasswordResponse(object):
    # Message field with str type hint
    message: str

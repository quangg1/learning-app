'''
    Main Purpose:
    => Implementing the AuthAPI class to handle user authentication API requests.
'''
from typing import (
    Optional,
    Literal
)

from requests import (
    get,
    post,
)

from app.schema import (
    UserSignInRequest
)

from app import (
    DOMAIN_API
)

from app.util import (
    LocalStore
)


from app.hook import (
    AuthHook
)

class AuthAPI:   
    @staticmethod 
    def get_token(payload: UserSignInRequest):
        '''
        Sends a POST request to retrieve a token based on the provided user sign-in payload. Returns the token if successful, otherwise returns an error code.
        '''
        response = post(f'{DOMAIN_API}/api/token/', json=payload)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {
                'code': 'res_error'
            }
        
    @staticmethod
    def get_user_by_token(token: str):
        '''
        Sends a GET request to fetch user information using the provided token. Returns user data if successful, otherwise returns an error code.
        '''
        response = get(f'{DOMAIN_API}/users/get-user-by-token', headers={
            'Authorization': f'TokenByAnhTuDev {token}'
        })
        
        if response.status_code == 200:
            return response.json()
        else:
            return {
                'code': 'res_error'
            }
            

    @staticmethod
    def check_auth():
        '''
        Checks if the user is authenticated by attempting to retrieve the token from local storage and verifying it with the server. Returns True if authenticated, otherwise False.
        '''
        token = LocalStore.get_data('access', 'token')
        if token:
            user = AuthAPI.get_user_by_token(token)
            if user.get('code') == 'res_error':
                return False
            else:
                AuthHook.set_authenticated(user.get('data'))
                return True
        else:
            return False
        
    @staticmethod
    def sign_up(payload: dict):
        '''
        Sends a POST request to sign up a new user with the provided payload. Returns the server response.
        '''
        try:
            response = post(f'{DOMAIN_API}/api-view/sign-up/', json=payload)
            print(f"Response status: {response.status_code}")
            print(f"Response content: {response.content}")
            
            if response.status_code == 200:
                return response.json()
            else:
                error_msg = f'Server returned status code {response.status_code}'
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        error_msg = error_data.get('message', error_msg)
                except:
                    pass
                return {
                    'code': 'res_error',
                    'message': error_msg
                }
        except Exception as e:
            print(f"Exception during signup: {str(e)}")
            return {
                'code': 'res_error',
                'message': str(e)
            }
    
    @staticmethod
    def sign_in(payload: dict):
        '''
        Sends a POST request to sign in a user with the provided payload. Returns the server response.
        '''
        response = post(f'{DOMAIN_API}/api-view/sign-in/', json=payload)
        return response.json()

    
    @staticmethod
    def forgot_password(payload: dict):
        '''
        Sends a GET request to initiate the forgot password process with the provided payload. Returns the server response.
        '''
        response = get(f'{DOMAIN_API}/api-view/common/forgot-password/', json=payload)
        return response.json()
    
    @staticmethod
    def refresh_token(refresh_token: str):
        '''
        Sends a POST request to refresh the token using the provided refresh token. Returns the server response.
        '''
        response = post(f'{DOMAIN_API}/api/token/refresh/', json={'refresh': refresh_token})
        return response.json()
    
    @staticmethod
    def auth_by_email(email: str):
        '''
        Sends a POST request to authenticate a user by email. Returns the server response.
        '''
        response = post(f'{DOMAIN_API}/api-view/token/', json={'email': email})
        return response.json()
    
    @staticmethod
    def check_token_of_email(token: str):
        '''
        Sends a POST request to check the token of an email. Returns the server response.
        '''
        response = get(f'{DOMAIN_API}/api-view/token/', headers={
            'Authorization' : f'TokenByAnhTuDev {token}'
        })
        return response.json()
    
    
        

    
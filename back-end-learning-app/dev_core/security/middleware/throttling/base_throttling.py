from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from typing import *
from dev_core.types.export import HTTP_METHOD_NAME_TYPE


class BaseUnauthenUser(AnonRateThrottle):
    scope = 'get_unauthen_user'
    setup_rate_by_anhtudev = {
        'GET': '500/h',
        'POST': '100/h',
        'PUT': '100/h',
        'DELETE': '100/h',
        'PATCH': '100/h',
    }



class BaseAuthenUser(UserRateThrottle):
    scope = 'get_authen_user'
    setup_rate_by_anhtudev = {
        'GET': '1000/h',
        'POST': '500/h',
        'PUT': '500/h',
        'DELETE': '500/h',
        'PATCH': '500/h',
    }


def generate_throttle_classes(
    authen: bool = False,
    http_method_names: HTTP_METHOD_NAME_TYPE = ['GET'],
    time_period: Literal['s', 'm', 'h', 'd', 'w', 'y'] = 'h',
    throttle_rate: int = 100,
    throttle_scope: Optional[str] = None
) -> List[Union[BaseUnauthenUser, BaseAuthenUser]]:
    '''
        Generate the throttle classes for the viewset
        Detail:
            - authen: bool = False: Check if the user is authen or not
            - http_method_names: HTTP_METHOD_NAME_TYPE = ['GET']: The list of the HTTP methods
            - time_period: str = 'day': The time period for the throttle rate
            - throttle_rate: int = 100: The throttle rate
            - throttle_scope: Optional[str] = None: The throttle scope
    '''
    throttle_classes = []
    if authen==False:
        #* Generate the throttle classes for the unauthen user
        for http_method_name in http_method_names:
            class_name = f'{throttle_scope.title()}HttpUnauthenUser' if throttle_scope is not None else 'HttpUnauthenUser'
            scope = f'{http_method_name.lower()}_http_unauthen_user' if throttle_scope is None else http_method_name.lower()+str(throttle_scope).lower()
            throttle_class = type(
                class_name, #* The name of the class
                (BaseUnauthenUser,), #* The base class
                { #* The class attributes static
                    'scope': scope,
                    'THROTTLE_RATES': {
                        scope: BaseUnauthenUser.setup_rate_by_anhtudev[http_method_name] if throttle_scope==None else f'{throttle_rate}/{time_period}'
                    },
                },
                
            )
            throttle_classes.append(throttle_class)
    else:
        #* Generate the throttle classes for the authen user
        for http_method_name in http_method_names:
            class_name = f'{throttle_scope.title()}HttpAuthenUser' if throttle_scope is not None else 'HttpAuthenUser'
            scope = f'{http_method_name.lower()}_http_authen_user' if throttle_scope is None else http_method_name.lower()+str(throttle_scope).lower()
            throttle_class = type(
                class_name,
                (BaseAuthenUser,),
                {
                    'scope': scope,
                    'THROTTLE_RATES': {
                        scope: BaseAuthenUser.setup_rate_by_anhtudev[http_method_name] if throttle_scope==None else f'{throttle_rate}/{time_period}'
                    }
                }
            )
            throttle_classes.append(throttle_class)
    # print('UnauthenUser:', throttle_classes) if authen==False else print('AuthenUser:', throttle_classes)
    return throttle_classes


UNTHENTHROTTLE={
    'GET': generate_throttle_classes(authen=False, http_method_names=['GET']),
    'POST': generate_throttle_classes(authen=False, http_method_names=['POST']),
    'PUT': generate_throttle_classes(authen=False, http_method_names=['PUT']),
    'DELETE': generate_throttle_classes(authen=False, http_method_names=['DELETE']),
    'PATCH': generate_throttle_classes(authen=False, http_method_names=['PATCH']),
}

AUTHENTHROTTLE={
    'GET': generate_throttle_classes(authen=True, http_method_names=['GET']),
    'POST': generate_throttle_classes(authen=True, http_method_names=['POST']),
    'PUT': generate_throttle_classes(authen=True, http_method_names=['PUT']),
    'DELETE': generate_throttle_classes(authen=True, http_method_names=['DELETE']),
    'PATCH': generate_throttle_classes(authen=True, http_method_names=['PATCH']),
}







    
    
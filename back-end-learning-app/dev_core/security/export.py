
#* Authentification and permission export
from dev_core.security.mix_authentication import *
from dev_core.security.mix_permission import *


#* Export all the security module
from dev_core.security.middleware.login_mw import *
from dev_core.security.middleware.hidden_info_mw import *




#* Export all the throttling module
from dev_core.security.middleware.throttling.base_throttling import (
    BaseUnauthenUser,
    generate_throttle_classes,
    UNTHENTHROTTLE,
    AUTHENTHROTTLE
)

#* Manage using design pattern Singleton and Factory
from dev_core.security.cache.cache_dev import (
    cache_decorator_factory as cache_decorator_factory_anhtudev
)

#* Strict router
from dev_core.security.strict_router.base_strict_router import (
    BaseStrictModelViewSet,
    AdminStrictModelViewSet,
    AuthenStrictModelViewSet,
    UnauthenStrictModelViewSet,
)
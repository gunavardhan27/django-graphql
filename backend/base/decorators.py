from functools import wraps
from graphql import GraphQLError
from .models import User
def login_required(resolver):
    @wraps(resolver)
    def wrapped_function(root, info, *args, **kwargs):
        user = info.context.user
        if user and user.is_authenticated:
            return resolver(root, info, *args, **kwargs)
        else:
            raise GraphQLError('Please Login')
    return wrapped_function

def allowed_roles(allowed_users=[]):
    def decorator(resolver):
        @wraps(resolver)
        def wrapper_function(root,info,*args,**kwargs):
            user = info.context.user
            if user:
                userInfo = User.objects.get(id=user.id)
                if str(userInfo.role) in allowed_users:
                    return resolver(root,info,*args,**kwargs)
            raise GraphQLError('not authorized to perform this operation')
        return wrapper_function
    return decorator
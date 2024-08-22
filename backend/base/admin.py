from django.contrib import admin
from .models import User,Post,UserRole
# Register your models here.
from django.apps import apps
admin.site.register(User)
admin.site.register(Post)
admin.site.register(UserRole)
app = apps.get_app_config('graphql_auth')

for model_name,model in app.models.items():
    admin.site.register(model)
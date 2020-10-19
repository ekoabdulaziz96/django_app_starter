from django.contrib import admin

from .models_role import Role
from .models import User

admin.site.register([User,Role])
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
class UserAdmin(UserAdmin):

	fieldsets=(
		('User',{'fields': ('username', 'password')}),
		('Persona Info', {'fields': ('first_name', 'last_name',
											'email')})

,
		)




admin.site.register(User, UserAdmin)


# Register your models here.

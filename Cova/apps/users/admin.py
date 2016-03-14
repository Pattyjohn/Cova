from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, MedicalProfile,PatientProfile
# Register your models here.

admin.site.register(User)
admin.site.register(MedicalProfile)
admin.site.register(PatientProfile)
# class UserAdmin(UserAdmin):

# 	fieldsets=(
# 		('User',{'fields': ('username', 'password')}),
# 		('Persona Info', {'fields': ('first_name', 'last_name',
# 											'email')})

# ,
# 		)




# admin.site.register(User, UserAdmin)


# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, MedicalProfile,PatientProfile
from .actions import export_as_excel
# Register your models here.

# admin.site.register(User)
# admin.site.register(MedicalProfile)
# admin.site.register(PatientProfile)

@admin.register(User)

class UserAdmin(admin.ModelAdmin):

	list_display= ('username', 'first_name', 'last_name', 'email',)
	search_fields = ('username','email',)
	list_filter=('is_medical','is_patient','is_superuser','is_staff', )
	ordering = ('username',)
	filter_horizontal = ('groups', 'user_permissions')
	actions=[export_as_excel]

	fieldsets=(
			('User',{'fields':('username', 'password')}),
			('Personal Info',{'fields':('first_name', 'last_name',
										'email', 'num_cole', 'num_hist',
										)}),
			('Permissions',  {'fields':('is_active', 'is_staff', 'is_superuser','is_medical', 'is_patient', 'groups', 'user_permissions',)}),
		)

# class UserAdmin(UserAdmin):

# 	fieldsets=(
# 		('User',{'fields': ('username', 'password')}),
# 		('Persona Info', {'fields': ('first_name', 'last_name',
# 											'email')})

# ,
# 		)




# admin.site.register(User, UserAdmin)


# Register your models here.

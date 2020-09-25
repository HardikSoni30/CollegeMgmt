from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, StudentProfile, StaffProfile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm  # Create view
    form = UserChangeForm  # Update view
    # model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # ('Personal Info', {'fields': ('date_of_birth', )}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(StudentProfile)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'enroll_num', 'first_name', 'last_name', 'gender', 'birthdate',)
    list_filter = ('gender', 'birthdate', )
    readonly_fields = ['user']
    search_fields = ('enroll_num', 'first_name', 'last_name')
    ordering = ('first_name', 'last_name',)
    # fieldsets = (
    #     ('Personal Info', {'fields': ('enroll_num', 'first_name', 'last_name', 'gender', 'birthdate', )}),
    #
    # )


@admin.register(StaffProfile)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'gender', 'birthdate', 'date_joined')
    list_filter = ('first_name', 'date_joined',)
    readonly_fields = ['user']
    search_fields = ('first_name', 'last_name')
    ordering = ('first_name', 'last_name',)
    # fieldsets = (
    #     ('Personal Info', {'fields': ('first_name', 'last_name', 'gender', 'birthdate', 'date_joined',)}),
    #
    # )


# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
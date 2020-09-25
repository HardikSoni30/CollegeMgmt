from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
# from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from accounts.models import StudentProfile, StaffProfile

User = get_user_model()


class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm):
        model = User
        fields = ('email', 'is_staff')
        # widgets = {
        #     'date_of_birth': DatePickerInput(format='%Y-%m-%d'),  # default date-format %m/%d/%Y will be used
        # }

    def clean(self):
        data = super(UserCreationForm, self).clean()
        if data['is_staff']:
            if "cpi.edu.in" not in data.get('email'):
                raise forms.ValidationError(
                    "Sorry, the email must be registered on cpi.edu.in for Staff User.")


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=50, label="Email",
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control',
                                        'placeholder': 'Email'}
                             )
                             )
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control',
                                          'placeholder': 'Password'}),
                               required=True, max_length=30)


class BaseProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseProfileForm, self).__init__(*args, **kwargs)
        # self.fields['enroll_num'].widget.attrs['readonly'] = True
        self.fields['user'].disabled = True

    class Meta:
        abstract = True


class StudentProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm):
        model = StudentProfile
        fields = '__all__'
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y')
                }


class StaffProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm):
        model = StaffProfile
        fields = '__all__'
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'),
                    'date_joined': DatePickerInput(format='%d/%m/%Y')
                }

from django.contrib.auth.views import (LogoutView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView)
from django.urls import path
from .views import (SignUpView, SignInView,
                    StaffProfileView, StudentProfileView)

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', SignInView.as_view(), name='login'),
    path('change-password/', PasswordChangeView.as_view(template_name='password_change_form.html'), name='change_password'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='change_password_done'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/<int:user_id>/', StaffProfileView.as_view(), name='profile_staff'),
    path('profile-student/<int:user_id>/', StudentProfileView.as_view(), name='profile_student'),
]
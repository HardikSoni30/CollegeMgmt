from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import (SignUpView, SignInView,
                    StaffProfileView, StudentProfileView)

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/<int:user_id>/', StaffProfileView.as_view(), name='profile_staff'),
    path('profile-student/<int:user_id>/', StudentProfileView.as_view(), name='profile_student'),
]
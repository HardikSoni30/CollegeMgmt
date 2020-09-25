from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# from django.utils.translation import gettext_lazy as _

from django.urls import reverse

from django.utils import timezone
from random import randint
from .managers import UserManager
from .choices import *
from .validators import validate_image, validate_age


def upload_image_path(instance, filename):
    ext = filename.split('.')[-1]
    # print(instance)
    # print(instance.user.is_staff)
    if instance.user.is_staff:
        final_filename = f"{instance.first_name}.{ext}"
        return f"Staff/{final_filename}"
    else:
        final_filename = f"{instance.enroll_num}.{ext}"
        return f"Students/{final_filename}"


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    # user_type = models.PositiveSmallIntegerField(choices=POSITION_CHOICES,
    #                                              default=POSITION_CHOICES[2][0])
    is_active = models.BooleanField(default=True)  # ---> activate user ---
    date_joined = models.DateTimeField(default=timezone.now)
    # notice the absence of a "Password field", that is built in
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    objects = UserManager()

    def __str__(self):
        return self.email


class BaseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30, verbose_name='first name', null=True)
    last_name = models.CharField(max_length=150, verbose_name='last name', null=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, default=GENDER_CHOICES[0][0])
    birthdate = models.DateField(null=True, blank=True, validators=[validate_age])
    profile_pic = models.ImageField(upload_to=upload_image_path, validators=[validate_image],
                                    blank=True, null=True,
                                    help_text='Maximum file size allowed is 150KB')

    def __str__(self):
        return self.user.email

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now =True)

    class Meta:
        abstract = True


class StudentProfile(BaseProfile):
    enroll_num = models.BigIntegerField(unique=True, default=randint(18535693001, 18535693200),
                                        validators=[MaxValueValidator(999999999999)])

    # address = models.TextField()
    # course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    student = models.Manager()

    def __str__(self):
        return self.user.email

    def get_absolute_url(self):
        return reverse('accounts:profile_student', kwargs={'user_id': self.user_id})


class StaffProfile(BaseProfile):
    role = models.PositiveSmallIntegerField(choices=POSITION_CHOICES,
                                            default=POSITION_CHOICES[2][0])
    department = models.CharField(max_length=10,
                                  verbose_name='Department',
                                  choices=DEPARTMENTS_TYPE,
                                  null=True)
    date_joined = models.DateField(null=True, blank=True)

    staff = models.Manager()

    def __str__(self):
        return self.user.email

    def get_absolute_url(self):
        return reverse('accounts:profile_staff', kwargs={'user_id': self.user_id})


# class Profile(StaffProfile, StudentProfile, BaseProfile):
#     pass


# class BaseProfile(models.Model):
#         USER_TYPES = (
#                       (0, 'Ordinary'),
#                       (1, 'SuperHero'),
#                      )
#         user = models.OneToOneField(User, primary_key=True)
#         user_type = models.IntegerField(max_length=1, null=True,
#         choices=USER_TYPES)
#         bio = models.CharField(max_length=200, blank=True, null=True)
#         def __str__(self):
#             return "{}: {:.20}". format(self.user, self.bio or "")
#         class Meta:
#             abstract = True
# if __name__ == "__main__":
   

